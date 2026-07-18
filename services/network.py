"""Servicio de operaciones de red."""

import logging
from typing import Dict, Any, Optional
import aiohttp

logger = logging.getLogger(__name__)


class NetworkService:
    """Servicio para operaciones de red."""
    
    @staticmethod
    async def get(url: str, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """Realizar petición GET.
        
        Args:
            url: URL destino
            headers: Headers personalizados
        
        Returns:
            Respuesta JSON
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    return {
                        "status": response.status,
                        "data": await response.json()
                    }
        except Exception as e:
            logger.error(f"Error en GET {url}: {str(e)}")
            raise
    
    @staticmethod
    async def post(
        url: str,
        data: Dict[str, Any],
        headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """Realizar petición POST.
        
        Args:
            url: URL destino
            data: Datos a enviar
            headers: Headers personalizados
        
        Returns:
            Respuesta JSON
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=data, headers=headers) as response:
                    return {
                        "status": response.status,
                        "data": await response.json()
                    }
        except Exception as e:
            logger.error(f"Error en POST {url}: {str(e)}")
            raise
