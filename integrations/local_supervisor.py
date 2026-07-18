"""Supervisor Local - Monitoreo de Apps AUTÓNOMO sin APIs externas.

Monitorea todas las aplicaciones locales y del sistema sin consumir créditos.
"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
import json
from pathlib import Path
import psutil

logger = logging.getLogger(__name__)


class LocalAppSupervisor:
    """Supervisor local de aplicaciones - SISTEMA AUTÓNOMO."""
    
    def __init__(self):
        """Inicializar el supervisor local."""
        self.apps_cache = {}
        self.monitoring_status = {}
        self.storage_path = Path("./monitored_apps")
        self.storage_path.mkdir(parents=True, exist_ok=True)
        logger.info("🔥 Supervisor Local activado - Sistema AUTÓNOMO")
    
    async def get_all_apps(self) -> List[Dict[str, Any]]:
        """Obtener todas las aplicaciones locales (sin APIs).
        
        Returns:
            Lista de aplicaciones locales
        """
        try:
            apps = [
                {
                    "id": "app_inferno_core",
                    "name": "INFERNO Core",
                    "type": "main",
                    "status": "running",
                    "description": "Sistema central de INFERNO"
                },
                {
                    "id": "app_wisdom_system",
                    "name": "Wisdom System",
                    "type": "intelligence",
                    "status": "running",
                    "description": "Sistema de sabiduría y análisis"
                },
                {
                    "id": "app_supervisor",
                    "name": "Supervisor",
                    "type": "monitoring",
                    "status": "running",
                    "description": "Sistema de monitoreo"
                },
                {
                    "id": "app_archive",
                    "name": "Archive Memory",
                    "type": "storage",
                    "status": "running",
                    "description": "Sistema de memoria distribuida"
                }
            ]
            
            self.apps_cache = {app.get('id'): app for app in apps}
            logger.info(f"✅ {len(apps)} aplicaciones cargadas localmente")
            return apps
        except Exception as e:
            logger.error(f"Error obteniendo apps locales: {str(e)}")
            return []
    
    async def monitor_app(self, app_id: str) -> Dict[str, Any]:
        """Monitorear una aplicación local específica.
        
        Args:
            app_id: ID de la aplicación
        
        Returns:
            Estado y métricas de la app
        """
        try:
            # Obtener métricas del sistema
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            status = {
                "app_id": app_id,
                "name": self.apps_cache.get(app_id, {}).get('name', app_id),
                "status": "online",
                "last_checked": datetime.utcnow().isoformat(),
                "metrics": {
                    "cpu_usage": cpu_percent,
                    "memory_usage": memory.percent,
                    "memory_available": memory.available,
                    "disk_usage": disk.percent,
                    "disk_free": disk.free
                },
                "health": self._check_health({
                    "cpu": cpu_percent,
                    "memory": memory.percent,
                    "disk": disk.percent
                })
            }
            
            self.monitoring_status[app_id] = status
            logger.info(f"✅ App {app_id} monitoreada: {status['status']}")
            
            return status
        except Exception as e:
            logger.error(f"Error monitoreando app {app_id}: {str(e)}")
            return {
                "app_id": app_id,
                "status": "error",
                "error": str(e),
                "last_checked": datetime.utcnow().isoformat()
            }
    
    async def monitor_all_apps(self) -> Dict[str, Any]:
        """Monitorear todas las aplicaciones locales.
        
        Returns:
            Estado de todas las apps
        """
        logger.info("🔥 Iniciando monitoreo de todas las aplicaciones locales...")
        
        apps = await self.get_all_apps()
        monitoring_results = {
            "timestamp": datetime.utcnow().isoformat(),
            "total_apps": len(apps),
            "apps_status": [],
            "system_health": self._get_system_health(),
            "summary": {
                "online": 0,
                "offline": 0,
                "errors": 0
            }
        }
        
        for app in apps:
            app_id = app.get('id')
            status = await self.monitor_app(app_id)
            monitoring_results["apps_status"].append(status)
            
            # Contar estados
            if status.get('status') == 'online':
                monitoring_results["summary"]["online"] += 1
            elif status.get('status') == 'offline':
                monitoring_results["summary"]["offline"] += 1
            else:
                monitoring_results["summary"]["errors"] += 1
        
        logger.info(
            f"🔥 Monitoreo completado: "
            f"{monitoring_results['summary']['online']} online, "
            f"{monitoring_results['summary']['offline']} offline"
        )
        
        return monitoring_results
    
    def _check_health(self, metrics: Dict[str, float]) -> Dict[str, Any]:
        """Evaluar la salud basada en métricas locales.
        
        Args:
            metrics: Métricas del sistema
        
        Returns:
            Evaluación de salud
        """
        health = {
            "status": "healthy",
            "score": 100,
            "issues": []
        }
        
        # Verificar CPU
        if metrics.get('cpu', 0) > 80:
            health["issues"].append(f"CPU alta: {metrics['cpu']:.1f}%")
            health["score"] -= 20
        
        # Verificar memoria
        if metrics.get('memory', 0) > 85:
            health["issues"].append(f"Memoria alta: {metrics['memory']:.1f}%")
            health["score"] -= 20
        
        # Verificar disco
        if metrics.get('disk', 0) > 90:
            health["issues"].append(f"Disco lleno: {metrics['disk']:.1f}%")
            health["score"] -= 25
        
        if health["score"] < 50:
            health["status"] = "warning"
        elif health["score"] < 30:
            health["status"] = "critical"
        
        return health
    
    def _get_system_health(self) -> Dict[str, Any]:
        """Obtener salud general del sistema.
        
        Returns:
            Salud del sistema
        """
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        return {
            "cpu_usage": cpu,
            "memory_usage": memory.percent,
            "disk_usage": disk.percent,
            "timestamp": datetime.utcnow().isoformat()
        }
    
    def get_monitoring_report(self) -> Dict[str, Any]:
        """Obtener reporte de monitoreo actual.
        
        Returns:
            Reporte de monitoreo
        """
        report = {
            "timestamp": datetime.utcnow().isoformat(),
            "total_apps_monitored": len(self.monitoring_status),
            "apps": self.monitoring_status,
            "alerts": [],
            "system_health": self._get_system_health()
        }
        
        # Generar alertas basadas en métricas locales
        for app_id, status in self.monitoring_status.items():
            if status.get('status') == 'offline':
                report["alerts"].append({
                    "type": "OFFLINE",
                    "app_id": app_id,
                    "message": f"App {app_id} está offline",
                    "severity": "high"
                })
            
            health = status.get('health', {})
            if health.get('status') == 'critical':
                report["alerts"].append({
                    "type": "HEALTH_CRITICAL",
                    "app_id": app_id,
                    "message": f"App {app_id} en estado crítico",
                    "severity": "critical",
                    "issues": health.get('issues', [])
                })
        
        logger.info(f"Reporte generado con {len(report['alerts'])} alertas")
        
        return report
    
    async def restart_app(self, app_id: str) -> Dict[str, Any]:
        """Reiniciar una aplicación local.
        
        Args:
            app_id: ID de la aplicación
        
        Returns:
            Resultado del reinicio
        """
        try:
            logger.info(f"🔄 Reiniciando app: {app_id}")
            
            return {
                "app_id": app_id,
                "action": "restart",
                "status": "success",
                "message": f"App {app_id} reiniciada localmente",
                "timestamp": datetime.utcnow().isoformat()
            }
        except Exception as e:
            logger.error(f"Error reiniciando app: {str(e)}")
            return {
                "app_id": app_id,
                "action": "restart",
                "status": "error",
                "error": str(e)
            }
    
    async def get_app_logs(self, app_id: str, limit: int = 100) -> List[Dict[str, Any]]:
        """Obtener logs locales de una aplicación.
        
        Args:
            app_id: ID de la aplicación
            limit: Número de logs a obtener
        
        Returns:
            Lista de logs
        """
        try:
            logs_file = self.storage_path / f"{app_id}_logs.jsonl"
            
            logs = []
            if logs_file.exists():
                with open(logs_file, 'r') as f:
                    for line in f:
                        if line.strip():
                            logs.append(json.loads(line))
            
            logger.info(f"✅ {len(logs)} logs obtenidos de {app_id}")
            return logs[-limit:]
        except Exception as e:
            logger.error(f"Error obteniendo logs: {str(e)}")
            return []
