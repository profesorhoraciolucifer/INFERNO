#!/usr/bin/env python3
"""
INFERNO - Sistema de Programación de Alto Nivel para Descargar y Usar Unido a la Red

Punto de entrada principal de la aplicación.
"""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from config.settings import settings
from api.routes import router
from integrations.replit import setup_replit_environment

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Maneja el ciclo de vida de la aplicación.
    """
    # Startup
    logger.info("🔥 INFERNO iniciando...")
    logger.info(f"Ambiente: {settings.environment}")
    logger.info(f"Debug: {settings.debug}")
    
    # Setup Replit if needed
    if settings.replit_environment:
        setup_replit_environment()
        logger.info("✅ Entorno de Replit configurado")
    
    yield
    
    # Shutdown
    logger.info("🛑 INFERNO apagando...")


# Crear aplicación FastAPI
app = FastAPI(
    title=settings.app_name,
    description="Sistema de Programación de Alto Nivel para Descargar y Usar Unido a la Red",
    version=settings.app_version,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check endpoint
@app.get("/health")
async def health_check():
    """Verificar estado de la aplicación."""
    return {
        "status": "healthy",
        "app": settings.app_name,
        "version": settings.app_version
    }


# Root endpoint
@app.get("/")
async def root():
    """Endpoint raíz."""
    return {
        "message": "Bienvenido a INFERNO 🔥",
        "app": settings.app_name,
        "version": settings.app_version,
        "docs": "/docs",
        "environment": settings.environment
    }


# Incluir rutas
app.include_router(router, prefix="/api", tags=["api"])


# Error handler global
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Manejador global de excepciones."""
    logger.error(f"Error no manejado: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Error interno del servidor", "error": str(exc)}
    )


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        log_level=settings.log_level.lower()
    )
