"""Registry Central - Registro de todas las aplicaciones del ecosistema."""

import json
from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum


class AppStatus(Enum):
    """Estados posibles de una aplicación."""
    ONLINE = "online"
    OFFLINE = "offline"
    ERROR = "error"
    DEPLOYING = "deploying"
    BUILDING = "building"
    IDLE = "idle"


class AppType(Enum):
    """Tipos de aplicaciones del ecosistema."""
    API = "api"
    BOT = "bot"
    WEB = "web"
    MOBILE = "mobile"
    SERVICE = "service"
    INTEGRATION = "integration"
    EDITOR = "editor"


class AppRegistry:
    """Registry centralizado de todas las apps."""
    
    def __init__(self, registry_file: str = "./supervisor/registry.json"):
        self.registry_file = registry_file
        self.apps = self._load_registry()
    
    def _load_registry(self) -> Dict:
        """Cargar registry desde archivo."""
        try:
            with open(self.registry_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return self._init_registry()
    
    def _init_registry(self) -> Dict:
        """Inicializar registry con todas las apps conocidas."""
        return {
            "timestamp": datetime.now().isoformat(),
            "apps": {
                # 🔥 NÚCLEO
                "inferno_core": {
                    "name": "INFERNO Core",
                    "type": "api",
                    "status": "online",
                    "url": "http://localhost:8000",
                    "repository": "https://github.com/profesorhoraciolucifer/INFERNO",
                    "platform": "github",
                    "last_check": None,
                    "health_endpoint": "/status",
                    "restart_command": "python main.py"
                },
                
                # 🧠 MEMORIA Y SABIDURÍA
                "nodriza": {
                    "name": "Nodriza (Cebador)",
                    "type": "service",
                    "status": "online",
                    "url": "https://replit.com/@profesorhoraciolucifer/Nodriza",
                    "platform": "replit",
                    "last_check": None,
                    "health_endpoint": "/api/health",
                    "description": "Sistema de cebadores y memoria"
                },
                
                # 🤖 AGENTES
                "fleet_langchain": {
                    "name": "Fleet (LangChain)",
                    "type": "bot",
                    "status": "idle",
                    "url": "https://replit.com/@profesorhoraciolucifer/Fleet",
                    "platform": "replit",
                    "last_check": None,
                    "description": "Agente de conversación"
                },
                
                # 🌐 INTEGRACIONES
                "base44_superagent": {
                    "name": "Base44 SuperAgent",
                    "type": "integration",
                    "status": "online",
                    "url": "https://app.base44.com/superagent/69d28c760c0fc513098b94ea",
                    "platform": "base44",
                    "last_check": None,
                    "description": "Motor de integración y orquestación"
                },
                
                # 📱 CANALES DE COMUNICACIÓN
                "whatsapp_business": {
                    "name": "WhatsApp Business",
                    "type": "integration",
                    "status": "online",
                    "platform": "external",
                    "api_endpoint": "https://api.whatsapp.com",
                    "last_check": None,
                    "description": "Canal directo con clientes"
                },
                
                "facebook_ads": {
                    "name": "Facebook Ads",
                    "type": "integration",
                    "status": "online",
                    "platform": "external",
                    "api_endpoint": "https://graph.facebook.com",
                    "last_check": None,
                    "description": "Vitrina pública y campañas"
                },
                
                "outlook": {
                    "name": "Outlook",
                    "type": "integration",
                    "status": "online",
                    "platform": "external",
                    "api_endpoint": "https://graph.microsoft.com",
                    "last_check": None,
                    "description": "Correo maestro"
                },
                
                # 🛠️ DESARROLLO
                "android_studio": {
                    "name": "Android Studio",
                    "type": "editor",
                    "status": "idle",
                    "platform": "local",
                    "last_check": None,
                    "description": "Compilador de aplicaciones móviles",
                    "build_command": "gradlew build",
                    "health_check": "grep -c 'success' build_log.txt"
                },
                
                # 🔧 GITHUB Y CI/CD
                "github_repository": {
                    "name": "GitHub Repository",
                    "type": "service",
                    "status": "online",
                    "url": "https://github.com/profesorhoraciolucifer/INFERNO",
                    "platform": "github",
                    "last_check": None,
                    "description": "Repositorio maestro con CI/CD"
                }
            }
        }
    
    def save_registry(self):
        """Guardar registry en archivo."""
        self.apps["timestamp"] = datetime.now().isoformat()
        with open(self.registry_file, 'w') as f:
            json.dump(self.apps, f, indent=2)
    
    def get_app(self, app_id: str) -> Optional[Dict]:
        """Obtener información de una app."""
        return self.apps.get("apps", {}).get(app_id)
    
    def get_all_apps(self) -> List[Dict]:
        """Obtener todas las apps."""
        return list(self.apps.get("apps", {}).values())
    
    def update_app_status(self, app_id: str, status: AppStatus, last_check: str = None):
        """Actualizar estado de una app."""
        if app_id in self.apps.get("apps", {}):
            self.apps["apps"][app_id]["status"] = status.value
            self.apps["apps"][app_id]["last_check"] = last_check or datetime.now().isoformat()
            self.save_registry()
    
    def get_by_platform(self, platform: str) -> List[Dict]:
        """Obtener apps por plataforma."""
        return [
            app for app in self.get_all_apps()
            if app.get("platform") == platform
        ]
    
    def get_by_type(self, app_type: str) -> List[Dict]:
        """Obtener apps por tipo."""
        return [
            app for app in self.get_all_apps()
            if app.get("type") == app_type
        ]
    
    def get_status_summary(self) -> Dict:
        """Obtener resumen de estados."""
        apps = self.get_all_apps()
        return {
            "total": len(apps),
            "online": len([a for a in apps if a.get("status") == "online"]),
            "offline": len([a for a in apps if a.get("status") == "offline"]),
            "error": len([a for a in apps if a.get("status") == "error"]),
            "idle": len([a for a in apps if a.get("status") == "idle"]),
            "deploying": len([a for a in apps if a.get("status") == "deploying"]),
            "building": len([a for a in apps if a.get("status") == "building"])
        }


if __name__ == "__main__":
    registry = AppRegistry()
    print(json.dumps(registry.apps, indent=2))
