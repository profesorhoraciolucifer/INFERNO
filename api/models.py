"""Modelos de datos para la API."""

from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime


class HealthCheckResponse(BaseModel):
    """Respuesta de health check."""
    status: str = Field(description="Estado de la aplicación")
    app: str = Field(description="Nombre de la aplicación")
    version: str = Field(description="Versión de la aplicación")


class ChatMessage(BaseModel):
    """Mensaje de chat."""
    role: str = Field(description="Rol del mensaje (user, assistant)")
    content: str = Field(description="Contenido del mensaje")
    timestamp: Optional[datetime] = Field(default_factory=datetime.utcnow)


class AgentChatRequest(BaseModel):
    """Solicitud de chat con agente."""
    message: str = Field(description="Mensaje del usuario")
    agent_id: Optional[str] = Field(default="default", description="ID del agente")
    session_id: Optional[str] = Field(default=None, description="ID de sesión")
    history: Optional[List[ChatMessage]] = Field(default=None, description="Historial de chat")


class AgentChatResponse(BaseModel):
    """Respuesta de chat con agente."""
    message: str = Field(description="Respuesta del agente")
    agent_id: str = Field(description="ID del agente")
    session_id: str = Field(description="ID de sesión")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class DownloadRequest(BaseModel):
    """Solicitud de descarga."""
    url: str = Field(description="URL a descargar")
    filename: Optional[str] = Field(default=None, description="Nombre del archivo")
    destination: Optional[str] = Field(default="./downloads", description="Destino de descarga")


class DownloadResponse(BaseModel):
    """Respuesta de descarga."""
    id: str = Field(description="ID de descarga")
    url: str = Field(description="URL descargada")
    status: str = Field(description="Estado de la descarga")
    filename: str = Field(description="Nombre del archivo descargado")
    progress: int = Field(default=0, description="Progreso en porcentaje")


class ErrorResponse(BaseModel):
    """Respuesta de error."""
    detail: str = Field(description="Detalles del error")
    error: Optional[str] = Field(default=None, description="Tipo de error")
