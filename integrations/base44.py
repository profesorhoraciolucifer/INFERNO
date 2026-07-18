"""Integración con Base44."""

import logging
from typing import Optional, Dict, Any

import requests
from config.settings import settings

logger = logging.getLogger(__name__)


class Base44Client:
    """Cliente para Base44 API."""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        api_url: Optional[str] = None
    ):
        """Inicializar cliente de Base44.
        
        Args:
            api_key: API key de Base44
            api_url: URL de la API de Base44
        """
        self.api_key = api_key or settings.base44_api_key
        self.api_url = api_url or settings.base44_api_url
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        })
    
    def get_data(self, endpoint: str) -> Dict[str, Any]:
        """Obtener datos de Base44.
        
        Args:
            endpoint: Endpoint a consultar
        
        Returns:
            Datos de Base44
        """
        try:
            url = f"{self.api_url}/{endpoint}"
            response = self.session.get(url)
            response.raise_for_status()
            logger.info(f"Datos obtenidos de Base44: {endpoint}")
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error obteniendo datos de Base44: {str(e)}")
            raise
    
    def post_data(
        self,
        endpoint: str,
        data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Enviar datos a Base44.
        
        Args:
            endpoint: Endpoint destino
            data: Datos a enviar
        
        Returns:
            Respuesta de Base44
        """
        try:
            url = f"{self.api_url}/{endpoint}"
            response = self.session.post(url, json=data)
            response.raise_for_status()
            logger.info(f"Datos enviados a Base44: {endpoint}")
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error enviando datos a Base44: {str(e)}")
            raise
    
    def health_check(self) -> bool:
        """Verificar conexión con Base44.
        
        Returns:
            True si la conexión es exitosa
        """
        try:
            response = self.session.get(f"{self.api_url}/health")
            logger.info("Conexión con Base44 verificada")
            return response.status_code == 200
        except requests.RequestException as e:
            logger.error(f"Error verificando conexión con Base44: {str(e)}")
            return False
