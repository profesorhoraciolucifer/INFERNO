"""Servicio de descargas."""

import logging
import asyncio
from typing import Optional, Callable
import aiohttp
from pathlib import Path

logger = logging.getLogger(__name__)


class DownloadService:
    """Servicio para gestionar descargas."""
    
    def __init__(self, destination: str = "./downloads"):
        """Inicializar servicio de descargas.
        
        Args:
            destination: Directorio de destino para descargas
        """
        self.destination = Path(destination)
        self.destination.mkdir(parents=True, exist_ok=True)
        self.downloads = {}
    
    async def download_file(
        self,
        url: str,
        filename: Optional[str] = None,
        on_progress: Optional[Callable] = None
    ) -> str:
        """Descargar un archivo.
        
        Args:
            url: URL del archivo a descargar
            filename: Nombre del archivo (opcional)
            on_progress: Callback para progreso de descarga
        
        Returns:
            Ruta del archivo descargado
        """
        try:
            filename = filename or url.split("/")[-1]
            filepath = self.destination / filename
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        raise Exception(f"Error descargando: {response.status}")
                    
                    total_size = int(response.headers.get('content-length', 0))
                    downloaded = 0
                    
                    with open(filepath, 'wb') as f:
                        async for chunk in response.content.iter_chunked(8192):
                            f.write(chunk)
                            downloaded += len(chunk)
                            
                            if on_progress and total_size > 0:
                                progress = (downloaded / total_size) * 100
                                on_progress(progress)
            
            logger.info(f"Archivo descargado: {filepath}")
            return str(filepath)
        except Exception as e:
            logger.error(f"Error descargando archivo: {str(e)}")
            raise
