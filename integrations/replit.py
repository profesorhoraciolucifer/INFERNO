"""Utilidades para Replit."""

import os
import logging

logger = logging.getLogger(__name__)


def setup_replit_environment() -> None:
    """Configurar entorno de Replit."""
    logger.info("Configurando entorno de Replit...")
    
    # Obtener variables de entorno de Replit
    replit_user = os.getenv("REPLIT_USER")
    replit_db = os.getenv("REPLIT_DB_URL")
    
    if replit_user:
        logger.info(f"Usuario de Replit: {replit_user}")
    
    if replit_db:
        logger.info("Base de datos de Replit detectada")


def is_replit() -> bool:
    """Verificar si se está ejecutando en Replit.
    
    Returns:
        True si se está ejecutando en Replit
    """
    return "REPLIT_ENVIRONMENT" in os.environ or "REPLIT_USER" in os.environ


def get_replit_url() -> str:
    """Obtener URL pública de Replit.
    
    Returns:
        URL pública del proyecto en Replit
    """
    user = os.getenv("REPLIT_USER")
    repl_slug = os.getenv("REPLIT_SLUG")
    
    if user and repl_slug:
        return f"https://{repl_slug}.{user}.repl.co"
    
    return "http://localhost:8000"
