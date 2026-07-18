"""Rutas de la API REST con Supervisión de Apps."""

import logging
import uuid
from typing import Optional, List

from fastapi import APIRouter, HTTPException, Query

from api.models import (
    AgentChatRequest, AgentChatResponse, ChatMessage,
    DownloadRequest, DownloadResponse, ErrorResponse
)
from agents.llm_agent import INFERNOAgent, create_example_tools
from wisdom.ceremony import Ceremony
from integrations.supervisor import AppSupervisor

logger = logging.getLogger(__name__)
router = APIRouter()

# Almacenamiento en memoria (en producción usar BD)
agents_store = {}
sessions_store = {}
ceremony = Ceremony()
supervisor = AppSupervisor()


@router.get("/status", tags=["health"])
async def get_status():
    """Obtener estado de la API."""
    return {
        "status": "operational",
        "agents": len(agents_store),
        "sessions": len(sessions_store),
        "ceremony": "active",
        "supervisor": "monitoring"
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


# ===== FLUJOS CEREMONIALES =====

@router.post("/viva/{agent_id}", tags=["ceremony", "viva"])
async def execute_viva_action(
    agent_id: str,
    action: str = Query(..., description="Acción a ejecutar"),
    parameters: Optional[dict] = None
):
    """Ejecutar una acción en el flujo VIVA (tiempo real).
    
    Args:
        agent_id: ID del agente
        action: Acción a ejecutar
        parameters: Parámetros de la acción
    
    Returns:
        Resultado de la acción
    """
    try:
        logger.info(f"🔥 VIVA: Ejecutando {action} por {agent_id}")
        
        result = await ceremony.viva.execute_action(
            agent_id=agent_id,
            action=action,
            parameters=parameters or {}
        )
        
        return result
    except Exception as e:
        logger.error(f"Error en VIVA: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/sabia/{agent_id}", tags=["ceremony", "sabia"])
async def consult_sabia_wisdom(
    agent_id: str,
    query: str = Query(..., description="Consulta de sabiduría")
):
    """Consultar el flujo SABIA (sabiduría y reflexión).
    
    Args:
        agent_id: ID del agente consultante
        query: Consulta de sabiduría
    
    Returns:
        Sabiduría y recomendaciones
    """
    try:
        logger.info(f"🧠 SABIA: Consulta de {agent_id}")
        
        wisdom = await ceremony.sabia.consult_wisdom(query, agent_id)
        
        return wisdom
    except Exception as e:
        logger.error(f"Error en SABIA: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/ceremony/{agent_id}", tags=["ceremony"])
async def perform_full_ceremony(
    agent_id: str,
    action: str = Query(...),
    parameters: Optional[dict] = None
):
    """Realizar una ceremonia completa: Guardianía > Viva > Sabia.
    
    Args:
        agent_id: ID del agente
        action: Acción ceremonial
        parameters: Parámetros
    
    Returns:
        Resultado ceremonial completo
    """
    try:
        logger.info(f"🔥 CEREMONIA COMPLETA: {action}")
        
        ceremony_result = await ceremony.perform_ceremony(
            agent_id=agent_id,
            action=action,
            parameters=parameters or {}
        )
        
        return ceremony_result
    except Exception as e:
        logger.error(f"Error en ceremonia: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/oracle/{agent_id}", tags=["ceremony", "oracle"])
async def consult_oracle(
    agent_id: str,
    query: str = Query(..., description="Consulta al oráculo")
):
    """Consultar al oráculo de sabiduría.
    
    Args:
        agent_id: ID del agente
        query: Consulta
    
    Returns:
        Respuesta del oráculo
    """
    try:
        logger.info(f"🔮 ORÁCULO: Consulta de {agent_id}")
        
        oracle_response = await ceremony.ask_oracle(query, agent_id)
        
        return oracle_response
    except Exception as e:
        logger.error(f"Error consultando oráculo: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


# ===== SUPERVISIÓN DE APPS EN BASE44 =====

@router.get("/supervisor/apps", tags=["supervisor", "base44"])
async def get_all_apps():
    """Obtener todas las aplicaciones en Base44 (@horacio-luciani).
    
    Returns:
        Lista de aplicaciones
    """
    try:
        logger.info("🔥 Obteniendo todas las apps de Base44")
        apps = await supervisor.get_all_apps()
        return {
            "total": len(apps),
            "apps": apps
        }
    except Exception as e:
        logger.error(f"Error obteniendo apps: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/supervisor/monitor/all", tags=["supervisor", "monitoring"])
async def monitor_all_apps():
    """Monitorear TODAS las aplicaciones en tiempo real.
    
    Returns:
        Estado de todas las apps
    """
    try:
        logger.info("🔥 INICIANDO MONITOREO TOTAL DE APPS")
        monitoring = await supervisor.monitor_all_apps()
        return monitoring
    except Exception as e:
        logger.error(f"Error en monitoreo: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/supervisor/monitor/{app_id}", tags=["supervisor", "monitoring"])
async def monitor_single_app(app_id: str):
    """Monitorear una aplicación específica.
    
    Args:
        app_id: ID de la aplicación
    
    Returns:
        Estado y métricas de la app
    """
    try:
        logger.info(f"🔥 Monitoreando app: {app_id}")
        status = await supervisor.monitor_app(app_id)
        return status
    except Exception as e:
        logger.error(f"Error monitoreando app: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/supervisor/report", tags=["supervisor", "monitoring"])
async def get_monitoring_report():
    """Obtener reporte de monitoreo.
    
    Returns:
        Reporte completo con alertas
    """
    try:
        logger.info("📊 Generando reporte de monitoreo")
        report = supervisor.get_monitoring_report()
        return report
    except Exception as e:
        logger.error(f"Error generando reporte: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/supervisor/restart/{app_id}", tags=["supervisor", "actions"])
async def restart_app(app_id: str):
    """Reiniciar una aplicación.
    
    Args:
        app_id: ID de la aplicación
    
    Returns:
        Resultado del reinicio
    """
    try:
        logger.info(f"🔄 Reiniciando app: {app_id}")
        result = await supervisor.restart_app(app_id)
        return result
    except Exception as e:
        logger.error(f"Error reiniciando app: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/supervisor/logs/{app_id}", tags=["supervisor", "logs"])
async def get_app_logs(app_id: str, limit: int = Query(100, ge=1, le=1000)):
    """Obtener logs de una aplicación.
    
    Args:
        app_id: ID de la aplicación
        limit: Número de logs a obtener
    
    Returns:
        Lista de logs
    """
    try:
        logger.info(f"📝 Obteniendo logs de {app_id}")
        logs = await supervisor.get_app_logs(app_id, limit)
        return {
            "app_id": app_id,
            "logs_count": len(logs),
            "logs": logs
        }
    except Exception as e:
        logger.error(f"Error obteniendo logs: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/memory/status", tags=["wisdom"])
async def get_memory_status():
    """Obtener estado de la memoria del INFERNO.
    
    Returns:
        Estado de la memoria acumulada
    """
    return {
        "memory_path": "./memoria",
        "archive": ceremony.archive.get_patterns(),
        "error_summary": ceremony.archive.get_error_summary(),
        "security_status": ceremony.guardian.get_security_status()
    }


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
