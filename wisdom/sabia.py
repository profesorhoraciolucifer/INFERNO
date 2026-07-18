"""SabiaFlow - Flujo de consulta y sabiduría AUTÓNOMO.

Aquí se reflexiona, se analiza y se aprende de lo vivo.
Sin dependencia de servicios externos.
"""

import logging
from typing import Dict, Any
from nodriza.oracle import Oracle
from nodriza.archive import Archive

logger = logging.getLogger(__name__)


class SabiaFlow:
    """Flujo de sabiduría y reflexión - SISTEMA AUTÓNOMO."""
    
    def __init__(self, archive: Archive):
        """Inicializar el flujo sabio.
        
        Args:
            archive: Instancia del archivo de memoria
        """
        self.archive = archive
        self.oracle = Oracle(archive)
        logger.info("🧠 SabiaFlow activado - Sistema AUTÓNOMO")
    
    async def consult_wisdom(
        self,
        query: str,
        agent_id: str,
        context: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """Consultar sabiduría acumulada (AUTÓNOMO).
        
        Args:
            query: Consulta del agente
            agent_id: ID del agente consultante
            context: Contexto adicional
        
        Returns:
            Respuesta de sabiduría
        """
        logger.info(f"🧠 Consulta de sabiduría: {query}")
        
        # Recomendar estrategia basada en la consulta
        recommendation = self.oracle.recommend_strategy(query, agent_id)
        
        return {
            "query": query,
            "agent_id": agent_id,
            "recommendation": recommendation,
            "context": context or {},
            "source": "local_wisdom_database"
        }
    
    async def reflect_on_action(
        self,
        action: str,
        result: Dict[str, Any],
        agent_id: str
    ) -> Dict[str, Any]:
        """Reflexionar sobre una acción completada (AUTÓNOMO).
        
        Args:
            action: Acción realizada
            result: Resultado de la acción
            agent_id: ID del agente
        
        Returns:
            Análisis y aprendizajes
        """
        logger.info(f"🧠 Reflexionando sobre: {action}")
        
        # Registrar la decisión en memoria local
        success = result.get("status") == "success"
        confidence = 0.9 if success else 0.5
        
        self.archive.record_decision(
            agent_id=agent_id,
            decision=action,
            reasoning=f"Acción: {action}",
            outcome=str(result),
            confidence=confidence
        )
        
        # Si fue exitoso, registrar como patrón
        if success:
            self.archive.add_pattern(
                pattern_name=f"{action}_successful",
                pattern_data=result,
                success_rate=confidence
            )
        
        return {
            "action": action,
            "result": result,
            "reflection": "Acción registrada en la memoria colectiva",
            "learning": "Patrones añadidos a la sabiduría del INFERNO",
            "confidence": confidence,
            "storage": "local_archive"
        }
    
    async def analyze_memory(self) -> Dict[str, Any]:
        """Analizar la memoria acumulada (AUTÓNOMO).
        
        Returns:
            Análisis de memoria
        """
        logger.info("🧠 Analizando memoria acumulada")
        
        return self.oracle.generate_wisdom_report()
    
    async def get_local_insights(self) -> Dict[str, Any]:
        """Obtener insights de datos locales.
        
        Returns:
            Insights del sistema
        """
        patterns = self.archive.get_patterns()
        error_summary = self.archive.get_error_summary()
        recent_logs = self.archive.get_recent_logs(limit=10)
        
        return {
            "total_patterns": len(patterns),
            "total_errors": sum(error_summary.values()),
            "error_types": error_summary,
            "recent_activity": recent_logs,
            "insights": self._generate_insights(patterns, error_summary)
        }
    
    def _generate_insights(self, patterns: Dict, errors: Dict) -> list:
        """Generar insights basados en datos locales.
        
        Args:
            patterns: Patrones encontrados
            errors: Errores registrados
        
        Returns:
            Lista de insights
        """
        insights = []
        
        # Insight sobre patrones exitosos
        if patterns:
            best_patterns = sorted(
                patterns.items(),
                key=lambda x: x[1].get('success_rate', 0),
                reverse=True
            )[:3]
            insights.append({
                "type": "success_patterns",
                "message": f"Top 3 patrones exitosos identificados",
                "patterns": [name for name, _ in best_patterns]
            })
        
        # Insight sobre errores
        if errors:
            most_common_error = max(errors, key=errors.get)
            insights.append({
                "type": "error_alert",
                "message": f"Error más frecuente: {most_common_error}",
                "frequency": errors[most_common_error]
            })
        
        return insights
