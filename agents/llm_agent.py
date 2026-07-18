"""Agentes LLM usando LangChain."""

import logging
from typing import Optional, List, Dict, Any

from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.tools import Tool

from config.settings import settings

logger = logging.getLogger(__name__)


class INFERNOAgent:
    """Agente principal de INFERNO."""
    
    def __init__(self, model: str = "gpt-4"):
        """Inicializar el agente.
        
        Args:
            model: Modelo de OpenAI a usar
        """
        self.model = model
        self.llm = ChatOpenAI(
            api_key=settings.openai_api_key,
            model=model,
            temperature=0.7
        )
        self.tools: List[Tool] = []
        self.executor: Optional[AgentExecutor] = None
    
    def add_tool(self, tool: Tool) -> None:
        """Agregar una herramienta al agente.
        
        Args:
            tool: Herramienta a agregar
        """
        self.tools.append(tool)
        logger.info(f"Herramienta '{tool.name}' agregada al agente")
    
    def setup(self) -> None:
        """Configurar el agente."""
        prompt = ChatPromptTemplate.from_messages([
            ("system", "Eres INFERNO, un asistente de programación de alto nivel. Ayuda a los usuarios con descargas, integración en red y programación."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])
        
        agent = create_openai_functions_agent(
            self.llm,
            self.tools,
            prompt
        )
        
        self.executor = AgentExecutor(
            agent=agent,
            tools=self.tools,
            verbose=settings.debug
        )
        logger.info("Agente configurado exitosamente")
    
    async def run(self, input_text: str, chat_history: List[Dict[str, str]] = None) -> str:
        """Ejecutar el agente.
        
        Args:
            input_text: Texto de entrada del usuario
            chat_history: Historial de chat
        
        Returns:
            Respuesta del agente
        """
        if not self.executor:
            self.setup()
        
        try:
            result = await self.executor.ainvoke({
                "input": input_text,
                "chat_history": chat_history or []
            })
            return result.get("output", "No se pudo generar una respuesta")
        except Exception as e:
            logger.error(f"Error ejecutando agente: {str(e)}", exc_info=True)
            return f"Error: {str(e)}"


# Herramientas de ejemplo
def create_example_tools() -> List[Tool]:
    """Crear herramientas de ejemplo.
    
    Returns:
        Lista de herramientas
    """
    return [
        Tool(
            name="get_info",
            func=lambda query: f"Información sobre: {query}",
            description="Obtener información sobre un tema"
        ),
        Tool(
            name="search_docs",
            func=lambda query: f"Resultados de búsqueda: {query}",
            description="Buscar en la documentación"
        )
    ]
