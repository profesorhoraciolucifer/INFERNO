"""Módulo Oracle - Consultor de sabiduría basada en experiencia.

El Oráculo consulta los registros acumulados y sugiere caminos futuros.
Usa patrones de éxito, lecciones de errores y experiencias previas.
"""

import logging
from typing import Dict, List, Any, Optional
from collections import Counter
from nodriza.archive import Archive

logger = logging.getLogger(__name__)


class Oracle:
    """Oráculo de sabiduría del INFERNO."""
    
    def __init__(self, archive: Archive):
        """Inicializar el oráculo.
        
        Args:
            archive: Instancia del archivo de memoria
        """
        self.archive = archive
        logger.info("Oráculo despertado")
    
    def consult_past_decisions(
        self,
        agent_id: str,
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """Consultar decisiones pasadas de un agente.
        
        Args:
            agent_id: ID del agente
            limit: Número de decisiones a consultar
        
        Returns:
            Lista de decisiones pasadas
        """
        logger.info(f"Consultando decisiones pasadas del agente {agent_id}")
        return []
    
    def recommend_strategy(
        self,
        current_situation: str,
        agent_id: str
    ) -> Dict[str, Any]:
        """Recomendar una estrategia basada en experiencia.
        
        Args:
            current_situation: Descripción de la situación actual
            agent_id: ID del agente consultante
        
        Returns:
            Recomendación con estrategia y confianza
        """
        patterns = self.archive.get_patterns()
        error_summary = self.archive.get_error_summary()
        
        # Analizar patrones relevantes
        relevant_patterns = [
            (name, data) for name, data in patterns.items()
            if data.get('success_rate', 0) > 0.7
        ]
        
        recommendation = {
            "situation": current_situation,
            "agent_id": agent_id,
            "strategies": [],
            "warnings": [],
            "confidence": 0.0
        }
        
        # Añadir estrategias basadas en patrones exitosos
        for pattern_name, pattern_data in relevant_patterns:
            recommendation["strategies"].append({
                "pattern": pattern_name,
                "success_rate": pattern_data.get('success_rate', 0),
                "approach": pattern_data.get('data', {})
            })
        
        # Añadir advertencias basadas en errores comunes
        if error_summary:
            most_common_error = max(error_summary, key=error_summary.get)
            recommendation["warnings"].append(
                f"Error frecuente: {most_common_error} ({error_summary[most_common_error]} veces)"
            )
        
        # Calcular confianza
        recommendation["confidence"] = min(
            1.0,
            len(relevant_patterns) * 0.2 + (1 - len(error_summary) * 0.1)
        )
        
        logger.info(
            f"Estrategia recomendada para {agent_id}: "
            f"confianza {recommendation['confidence']:.2f}"
        )
        
        return recommendation
    
    def analyze_errors(
        self,
        error_type: Optional[str] = None
    ) -> Dict[str, Any]:
        """Analizar errores registrados.
        
        Args:
            error_type: Tipo específico de error a analizar
        
        Returns:
            Análisis de errores
        """
        error_summary = self.archive.get_error_summary()
        
        analysis = {
            "total_errors": sum(error_summary.values()),
            "error_distribution": error_summary,
            "most_common": max(error_summary, key=error_summary.get) if error_summary else None,
            "recommendations": []
        }
        
        # Generar recomendaciones
        if error_summary:
            for error_type, count in sorted(
                error_summary.items(),
                key=lambda x: x[1],
                reverse=True
            )[:3]:
                analysis["recommendations"].append(
                    f"Reducir {error_type}: {count} ocurrencias detectadas"
                )
        
        logger.info(f"Análisis de errores completado: {analysis['total_errors']} errores")
        
        return analysis
    
    def predict_success(
        self,
        plan: str,
        agent_id: str
    ) -> Dict[str, Any]:
        """Predecir probabilidad de éxito basada en experiencia.
        
        Args:
            plan: Plan propuesto
            agent_id: ID del agente
        
        Returns:
            Predicción de éxito
        """
        patterns = self.archive.get_patterns()
        
        # Buscar patrones similares
        similar_patterns = [
            data.get('success_rate', 0)
            for name, data in patterns.items()
        ]
        
        if similar_patterns:
            avg_success_rate = sum(similar_patterns) / len(similar_patterns)
        else:
            avg_success_rate = 0.5  # Tasa base
        
        prediction = {
            "plan": plan,
            "agent_id": agent_id,
            "predicted_success_rate": avg_success_rate,
            "based_on_patterns": len(similar_patterns),
            "recommendation": "Proceder" if avg_success_rate > 0.6 else "Precaución"
        }
        
        logger.info(
            f"Predicción para {agent_id}: "
            f"tasa de éxito {avg_success_rate:.2%}"
        )
        
        return prediction
    
    def generate_wisdom_report(self) -> Dict[str, Any]:
        """Generar reporte de sabiduría acumulada.
        
        Returns:
            Reporte completo de sabiduría
        """
        patterns = self.archive.get_patterns()
        error_analysis = self.analyze_errors()
        recent_logs = self.archive.get_recent_logs(limit=20)
        
        report = {
            "title": "Reporte de Sabiduría del INFERNO",
            "total_patterns_learned": len(patterns),
            "total_errors_analyzed": error_analysis["total_errors"],
            "patterns": patterns,
            "error_analysis": error_analysis,
            "recent_activity": recent_logs
        }
        
        logger.info("Reporte de sabiduría generado")
        
        return report
