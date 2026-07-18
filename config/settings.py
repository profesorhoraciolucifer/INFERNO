"""Configuración centralizada de la aplicación."""

from typing import List
from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Configuración de la aplicación."""
    
    # App
    app_name: str = Field(default="INFERNO", description="Nombre de la aplicación")
    app_version: str = Field(default="0.1.0", description="Versión de la aplicación")
    debug: bool = Field(default=False, description="Modo debug")
    environment: str = Field(default="development", description="Ambiente de ejecución")
    
    # Server
    host: str = Field(default="0.0.0.0", description="Host del servidor")
    port: int = Field(default=8000, description="Puerto del servidor")
    allowed_origins: List[str] = Field(
        default=["*"],
        description="Origins permitidos para CORS"
    )
    
    # LangChain
    langchain_api_key: str = Field(default="", description="API key de LangChain")
    langchain_environment: str = Field(default="development", description="Ambiente de LangChain")
    langchain_tracing: bool = Field(default=False, description="Habilitar tracing de LangChain")
    
    # Base44
    base44_api_key: str = Field(default="", description="API key de Base44")
    base44_api_url: str = Field(default="https://app.base44.com/api", description="URL de API de Base44")
    base44_environment: str = Field(default="development", description="Ambiente de Base44")
    
    # OpenAI
    openai_api_key: str = Field(default="", description="API key de OpenAI")
    
    # Database
    database_url: str = Field(
        default="sqlite:///./inferno.db",
        description="URL de conexión a base de datos"
    )
    
    # Security
    secret_key: str = Field(default="secret-key-change-in-production")
    algorithm: str = Field(default="HS256")
    access_token_expire_minutes: int = Field(default=30)
    
    # Replit
    replit_environment: bool = Field(default=False, description="¿Ejecutando en Replit?")
    
    # Logging
    log_level: str = Field(default="INFO", description="Nivel de logging")
    
    class Config:
        """Configuración de Pydantic."""
        env_file = ".env"
        case_sensitive = False


@lru_cache
def get_settings() -> Settings:
    """Obtener instancia de configuración cacheada."""
    return Settings()


# Instancia global
settings = get_settings()
