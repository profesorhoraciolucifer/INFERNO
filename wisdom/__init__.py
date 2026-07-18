"""Módulo Wisdom - Sistema de flujos ceremoniales AUTÓNOMO.

Conecta los flujos vivos (/viva) con los flujos sabios (/sabia).
El diálogo entre acción y reflexión SIN depender de APIs externas.
"""

from wisdom.viva import VivaFlow
from wisdom.sabia import SabiaFlow
from wisdom.ceremony import Ceremony

__all__ = ["VivaFlow", "SabiaFlow", "Ceremony"]
