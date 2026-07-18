"""Rutas de la API REST."""

import logging
import uuid
from typing import Optional, List

from fastapi import APIRouter, HTTPException, Query

from api.models import (
    AgentChatRequest, AgentChatResponse, ChatMessage,
    DownloadRequest, DownloadResponse, ErrorResponse
)
from agents.llm_agent import INFERNOAgent, create_example_tools

logger = logging.getLogger(__name__)
router = APIRouter()

# Almacenamiento en memoria (en producción usar BD)
agents_store = {}
sessions_store = {}


@router.get("/status", tags=["health"])
async def get_status():
    """Obtener estado de la API."""
    return {
        "status": "operational",
        "agents": len(agents_store),
        "sessions": len(sessions_store)
    }


@router.post("/agents/create", response_model=dict, tags=["agents"])
async def create_agent(
    agent_id: Optional[str] = Query(None),
    model: str = Query("gpt-4")
):
    """Crear un nuevo agente.
    
    Args:
        agent_id: ID personalizado del agente (opcional)
        model: Modelo de OpenAI a usar
    
    Returns:
        Información del agente creado
    """
    try:
        agent_id = agent_id or str(uuid.uuid4())
        
        agent = INFERNOAgent(model=model)
        
        # Agregar herramientas de ejemplo
        for tool in create_example_tools():
            agent.add_tool(tool)
        
        agent.setup()
        agents_store[agent_id] = agent
        
        logger.info(f"Agente '{agent_id}' creado exitosamente")
        
        return {
            "agent_id": agent_id,
            "model": model,
            "status": "ready",
            "tools_count": len(agent.tools)
        }
    except Exception as e:
        logger.error(f"Error creando agente: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/agents/list", tags=["agents"])
async def list_agents():
    """Listar agentes disponibles.
    
    Returns:
        Lista de agentes
    """
    return {
        "agents": list(agents_store.keys()),
        "total": len(agents_store)
    }


@router.post("/agents/chat", response_model=AgentChatResponse, tags=["agents"])
async def agent_chat(request: AgentChatRequest) -> AgentChatResponse:
    """Chat con un agente.
    
    Args:
        request: Solicitud de chat
    
    Returns:
        Respuesta del agente
    """
    try:
        agent_id = request.agent_id
        session_id = request.session_id or str(uuid.uuid4())
        
        # Obtener o crear agente
        if agent_id not in agents_store:
            agent = INFERNOAgent()
            for tool in create_example_tools():
                agent.add_tool(tool)
            agent.setup()
            agents_store[agent_id] = agent
        
        agent = agents_store[agent_id]
        
        # Preparar historial
        chat_history = []
        if request.history:
            chat_history = [
                {"role": msg.role, "content": msg.content}
                for msg in request.history
            ]
        
        # Ejecutar agente
        response = await agent.run(request.message, chat_history)
        
        return AgentChatResponse(
            message=response,
            agent_id=agent_id,
            session_id=session_id
        )
    except Exception as e:
        logger.error(f"Error en chat con agente: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/download", response_model=DownloadResponse, tags=["downloads"])
async def download(
    request: DownloadRequest
) -> DownloadResponse:
    """Iniciar una descarga.
    
    Args:
        request: Solicitud de descarga
    
    Returns:
        Información de la descarga
    """
    try:
        download_id = str(uuid.uuid4())
        filename = request.filename or download_id
        
        # Aquí iría la lógica real de descarga
        logger.info(f"Descarga iniciada: {download_id} desde {request.url}")
        
        return DownloadResponse(
            id=download_id,
            url=request.url,
            status="pending",
            filename=filename,
            progress=0
        )
    except Exception as e:
        logger.error(f"Error iniciando descarga: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/download/{download_id}/status", tags=["downloads"])
async def download_status(download_id: str):
    """Obtener estado de una descarga.
    
    Args:
        download_id: ID de la descarga
    
    Returns:
        Estado de la descarga
    """
    return {
        "id": download_id,
        "status": "pending",
        "progress": 0
    }
