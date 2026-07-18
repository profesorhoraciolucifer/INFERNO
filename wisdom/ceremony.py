"""Ceremony - Orquestador ceremonial de Viva y Sabia AUTÓNOMO.

Conecta los flujos vivos con los flujos sabios en un diálogo ceremonial.
Sistema completamente autónomo sin dependencias externas.
"""

import logging
from typing import Dict, Any
from wisdom.viva import VivaFlow
from wisdom.sabia import SabiaFlow
from nodriza.archive import Archive
from nodriza.guardian import Guardian

logger = logging.getLogger(__name__)


class Ceremony:
    """Ceremonia que une Viva y Sabia en armonía - SISTEMA AUTÓNOMO."""
    
    def __init__(self):
        """Inicializar la ceremonia AUTÓNOMA."""
        self.archive = Archive()
        self.viva = VivaFlow()
        self.sabia = SabiaFlow(self.archive)
        self.guardian = Guardian()
        logger.info("🔥 CEREMONIA INICIADA - Viva y Sabia en diálogo AUTÓNOMO")
    
    async def perform_ceremony(
        self,
        agent_id: str,
        action: str,
        parameters: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Ejecutar una ceremonia completa: Guardianía > Viva > Sabia (AUTÓNOMO).
        
        Args:
            agent_id: ID del agente
            action: Acción a ejecutar
            parameters: Parámetros de la acción
        
        Returns:
            Resultado ceremonial
        """
        logger.info(f"🔥 Ceremonia: {action} por {agent_id}")
        
        ceremony_result = {
            "agent_id": agent_id,
            "action": action,
            "phases": {},
            "autonomous": True
        }
        
        # Fase 1: GUARDIANÍA - Validar
        validation = self.guardian.validate_action(agent_id, action, parameters)
        ceremony_result["phases"]["guardian"] = validation
        
        if not validation["valid"]:
            logger.warning(f"Acción rechazada por el guardián: {validation.get('reason')}")
            return ceremony_result
        
        # Fase 2: VIVA - Ejecutar acción en tiempo real
        task = await self.viva.execute_action(agent_id, action, parameters)
        ceremony_result["phases"]["viva"] = task
        
        # Registrar intento
        self.guardian.record_attempt(
            agent_id=agent_id,
            success=task["status"] == "completed",
            action=action
        )
        
        # Fase 3: SABIA - Reflexionar y aprender
        reflection = await self.sabia.reflect_on_action(
            action=action,
            result=task.get("result", {}),
            agent_id=agent_id
        )
        ceremony_result["phases"]["sabia"] = reflection
        
        logger.info("🔥 Ceremonia completada")
        
        return ceremony_result
    
    async def ask_oracle(
        self,
        query: str,
        agent_id: str
    ) -> Dict[str, Any]:
        """Consultar al oráculo de sabiduría (AUTÓNOMO).
        
        Args:
            query: Consulta al oráculo
            agent_id: ID del agente consultante
        
        Returns:
            Respuesta del oráculo
        """
        logger.info(f"🔮 Consulta al oráculo: {query}")
        
        wisdom = await self.sabia.consult_wisdom(query, agent_id)
        
        return wisdom
    
    def get_system_status(self) -> Dict[str, Any]:
        """Obtener estado completo del sistema AUTÓNOMO.
        
        Returns:
            Estado del sistema
        """
        return {
            "status": "operational",
            "autonomous": True,
            "components": {
                "viva": {
                    "active_tasks": len(self.viva.get_active_tasks()),
                    "completed_tasks": len(self.viva.get_completed_tasks()),
                    "status": "running"
                },
                "sabia": {
                    "patterns_learned": len(self.archive.get_patterns()),
                    "errors_recorded": sum(self.archive.get_error_summary().values()),
                    "status": "analyzing"
                },
                "guardian": self.guardian.get_security_status()
            },
            "memory": {
                "archive_path": str(self.archive.archive_path),
                "patterns": len(self.archive.get_patterns()),
                "errors": self.archive.get_error_summary()
            }
        }
    
    async def get_full_report(self) -> Dict[str, Any]:
        """Obtener reporte completo del sistema.
        
        Returns:
            Reporte completo
        """
        wisdom_analysis = await self.sabia.analyze_memory()
        insights = await self.sabia.get_local_insights()
        
        return {
            "timestamp": wisdom_analysis.get("exported_at", ""),
            "system_status": self.get_system_status(),
            "wisdom_report": wisdom_analysis,
            "insights": insights,
            "autonomous": True,
            "external_dependencies": []
        }
