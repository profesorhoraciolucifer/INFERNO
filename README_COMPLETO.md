# 🔥 INFERNO - Sistema de Programación de Alto Nivel Distribuido

**INFERNO** es un sistema ceremonial de programación distribuida que combina:
- 🔥 **Acciones en Tiempo Real** (VIVA)
- 🧠 **Sabiduría y Aprendizaje** (SABIA)
- 📊 **Supervisión Autónoma** de todas las aplicaciones
- 🔮 **Oráculo Inteligente** basado en experiencia acumulada
- 💾 **Memoria Colectiva** que nunca olvida

---

## 🚀 CARACTERÍSTICAS PRINCIPALES

### ✨ Sistema Ceremonial Autónomo (SIN APIs Externas)

#### 🔥 **VIVA** - Flujo de Acciones Vivas
```
POST /viva/{agent_id}?action=download_file&parameters={}
POST /viva/{agent_id}?action=process_data&parameters={}
POST /viva/{agent_id}?action=store_data&parameters={}
POST /viva/{agent_id}?action=monitor_system&parameters={}
```

**Características:**
- ✅ Ejecución local 100% autónoma
- ✅ Almacenamiento local de acciones
- ✅ Sin dependencia de servicios externos
- ✅ Respuesta en milisegundos

#### 🧠 **SABIA** - Flujo de Sabiduría y Reflexión
```
GET /sabia/{agent_id}?query=como_optimizar_rendimiento
GET /memory/status
```

**Características:**
- ✅ Análisis de memoria acumulada
- ✅ Recomendaciones basadas en patrones
- ✅ Aprendizaje de errores pasados
- ✅ Generación de insights locales

#### 🔮 **ORÁCULO** - Consultor de Sabiduría
```
GET /oracle/{agent_id}?query=estrategia_para_problema_x
```

**Características:**
- ✅ Predicción de éxito
- ✅ Análisis de errores históricos
- ✅ Recomendaciones estratégicas
- ✅ Confianza basada en datos

#### 💫 **CEREMONIA COMPLETA** - Flujo Orquestado
```
POST /ceremony/{agent_id}?action=download_file&parameters={}
```

**Fases:**
1. **GUARDIANÍA** - Validación de seguridad
2. **VIVA** - Ejecución de acción
3. **SABIA** - Reflexión y aprendizaje

---

## 📊 SUPERVISIÓN DE APLICACIONES

### Puente Base44 Creado ✅
**URL:** https://app.base44.com/superagent/69d28c760c0fc513098b94ea

Este puente conecta INFERNO con TODAS tus aplicaciones en Base44 (@horacio-luciani).

### Endpoints de Supervisión

#### 🔥 Obtener Todas las Apps
```bash
GET /supervisor/apps

Response:
{
  "total": 4,
  "apps": [
    {"id": "app_001", "name": "INFERNO Core", "status": "running"},
    {"id": "app_002", "name": "Wisdom System", "status": "running"},
    {"id": "app_003", "name": "Supervisor", "status": "monitoring"},
    {"id": "app_004", "name": "Archive Memory", "status": "running"}
  ]
}
```

#### 🔥 Monitoreo en Tiempo Real
```bash
GET /supervisor/monitor/all

Response:
{
  "timestamp": "2026-07-18T05:57:48Z",
  "total_apps": 4,
  "summary": {
    "online": 4,
    "offline": 0,
    "errors": 0
  },
  "apps_status": [...]
}
```

#### 📊 Reporte de Monitoreo
```bash
GET /supervisor/report

Response:
{
  "timestamp": "2026-07-18T05:57:48Z",
  "total_apps_monitored": 4,
  "alerts": [],
  "apps": {...}
}
```

#### 🔄 Reiniciar Aplicación
```bash
POST /supervisor/restart/{app_id}

Response:
{
  "app_id": "app_001",
  "action": "restart",
  "status": "success"
}
```

#### 📝 Ver Logs
```bash
GET /supervisor/logs/{app_id}?limit=100

Response:
{
  "app_id": "app_001",
  "logs_count": 100,
  "logs": [...]
}
```

---

## 🏗️ ARQUITECTURA DEL SISTEMA

```
┌─────────────────────────────────────────────────────────────────┐
│                        INFERNO 🔥                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌────────────────┐      ┌────────────────┐                      │
│  │   VIVA FLOW    │      │   SABIA FLOW   │                      │
│  │ (Acciones)     │◄────►│ (Sabiduría)    │                      │
│  └────────────────┘      └────────────────┘                      │
│         ▲                        ▲                                │
│         │                        │                                │
│         └────────────────┬───────┘                                │
│                          │                                        │
│                    ┌─────▼──────┐                                 │
│                    │  CEREMONY  │                                 │
│                    │ (Orquesta)  │                                 │
│                    └─────┬──────┘                                 │
│                          │                                        │
│          ┌───────────────┼───────────────┐                        │
│          │               │               │                        │
│    ┌─────▼────┐   ┌─────▼─────┐  ┌─────▼─────┐                   │
│    │ GUARDIAN  │   │  ARCHIVE  │  │  ORACLE   │                  │
│    │(Seguridad)│   │(Memoria)  │  │(Sabiduría)│                  │
│    └───────────┘   └───────────┘  └───────────┘                  │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │         SUPERVISOR LOCAL (Autónomo, Sin APIs)              │ │
│  │                                                             │ │
│  │  • Monitoreo de CPU, Memoria, Disco                        │ │
│  │  • Alertas automáticas                                     │ │
│  │  • Reinicio local de apps                                  │ │
│  │  • Histórico de logs                                       │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                          │                                        │
│                    ┌─────▼──────────────┐                         │
│                    │  Base44 Bridge     │                         │
│                    │ (Puente a tus Apps)│                         │
│                    │ @horacio-luciani   │                         │
│                    └────────────────────┘                         │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💾 SISTEMA DE MEMORIA (NODRIZA)

### Archive (Archivo de Memoria)
```
./memoria/
├── logs.jsonl           # Eventos registrados
├── decisions.jsonl      # Decisiones tomadas
├── errors.jsonl         # Errores y soluciones
├── patterns.json        # Patrones de éxito
└── index.json          # Índice de memoria
```

**Almacena:**
- 📝 Todos los eventos del sistema
- 🎯 Decisiones tomadas por agentes
- ❌ Errores con contexto y soluciones
- ✅ Patrones de éxito identificados
- 📊 Métricas de desempeño

### Oracle (Consultor de Sabiduría)
- 🔮 Predice probabilidad de éxito
- 📚 Recomienda estrategias basadas en patrones
- ⚠️ Advierte sobre errores comunes
- 📈 Analiza evolución del sistema

### Guardian (Guardián de Seguridad)
- 🔐 Valida acciones antes de ejecutarlas
- 🚫 Bloquea agentes con múltiples fallos
- ✅ Verifica integridad de datos
- 📊 Reporta estado de seguridad

---

## 🚀 INSTALACIÓN Y USO

### Requisitos
```bash
Python 3.9+
pip install -r requirements.txt
```

### Instalación
```bash
# Clonar repositorio
git clone https://github.com/profesorhoraciolucifer/INFERNO.git
cd INFERNO

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales (opcional para sistema autónomo)

# Ejecutar
python main.py
```

### Acceder a la API
- **API REST:** http://localhost:8000
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

---

## 📡 FLUJO DE EJEMPLO

### 1. Ejecutar Acción (VIVA)
```bash
curl -X POST "http://localhost:8000/api/viva/agent_001?action=download_file&parameters={\"source\":\"local\",\"destination\":\"./downloads\"}"
```

### 2. Consultar Sabiduría (SABIA)
```bash
curl -X GET "http://localhost:8000/api/sabia/agent_001?query=como_optimizar_descargas"
```

### 3. Ceremonia Completa
```bash
curl -X POST "http://localhost:8000/api/ceremony/agent_001?action=process_data&parameters={\"data\":[]}"
```

### 4. Consultar Oráculo
```bash
curl -X GET "http://localhost:8000/api/oracle/agent_001?query=probabilidad_exito_proxima_accion"
```

### 5. Monitorear Todo
```bash
curl -X GET "http://localhost:8000/api/supervisor/monitor/all"
```

---

## 🔗 INTEGRACIÓN CON BASE44

### Bridge Creado
**URL:** https://app.base44.com/superagent/69d28c760c0fc513098b94ea

Este SuperAgent actúa como puente entre INFERNO y todas tus aplicaciones.

### Características del Bridge
- ✅ Conexión automática con @horacio-luciani
- ✅ Sincronización de estado de apps
- ✅ Alertas bidireccionales
- ✅ Acceso a memoria compartida
- ✅ Orquestación centralizada

### Cómo Usarlo
```bash
# Obtener estado de todas las apps (via Base44)
GET https://app.base44.com/superagent/69d28c760c0fc513098b94ea/status

# Las apps se comunican con INFERNO automáticamente
# INFERNO mantiene la memoria y coordina todas las acciones
```

---

## 🌟 VENTAJAS DEL SISTEMA

### 🔥 TOTALMENTE AUTÓNOMO
- ✅ No consume créditos de APIs externas
- ✅ Funciona sin conexión a internet
- ✅ Almacenamiento 100% local
- ✅ Rápido como el rayo

### 🧠 INTELIGENTE
- ✅ Aprende de cada acción
- ✅ Recuerda errores pasados
- ✅ Predice futuros problemas
- ✅ Sugiere estrategias óptimas

### 📊 SUPERVISIÓN TOTAL
- ✅ Monitorea CPU, memoria, disco
- ✅ Alertas automáticas en tiempo real
- ✅ Logs centralizados
- ✅ Reinicio remoto de apps

### 🔐 SEGURO
- ✅ Valida todas las acciones
- ✅ Bloquea intentos maliciosos
- ✅ Verifica integridad de datos
- ✅ Reporta amenazas

---

## 📚 ESTRUCTURA DE ARCHIVOS

```
INFERNO/
├── main.py                          # Punto de entrada
├── requirements.txt                 # Dependencias
├── .env.example                     # Configuración
├── .github/
│   └── workflows/
│       └── ci-cd.yml               # Pipeline CI/CD
├── config/
│   └── settings.py                 # Configuración centralizada
├── agents/
│   └── llm_agent.py                # Agentes LangChain
├── api/
│   ├── routes.py                   # Endpoints REST
│   ├── models.py                   # Modelos Pydantic
│   └── __init__.py
├── nodriza/                        # Sistema de Memoria
│   ├── archive.py                  # Archivo de memoria
│   ├── oracle.py                   # Oráculo inteligente
│   ├── guardian.py                 # Guardián de seguridad
│   └── __init__.py
├── wisdom/                         # Flujos Ceremoniales
│   ├── viva.py                     # Flujo de acciones
│   ├── sabia.py                    # Flujo de sabiduría
│   ├── ceremony.py                 # Orquestador
│   └── __init__.py
├── integrations/
│   ├── supervisor.py               # Supervisor Base44
│   ├── local_supervisor.py         # Supervisor local
│   ├── base44.py                   # Cliente Base44
│   ├── replit.py                   # Soporte Replit
│   └── __init__.py
├── services/
│   ├── download.py                 # Descargas async
│   └── network.py                  # Operaciones de red
├── memoria/                        # Almacenamiento de memoria
│   ├── logs.jsonl
│   ├── decisions.jsonl
│   ├── errors.jsonl
│   ├── patterns.json
│   └── index.json
└── tests/
    └── test_api.py                 # Tests unitarios
```

---

## 🔄 CI/CD Pipeline

### Activado en:
- ✅ Push a `main` y `develop`
- ✅ Pull Requests a `main`

### Ejecuta:
- ✅ Instalación de dependencias
- ✅ Ejecución de tests
- ✅ Lint con pylint
- ✅ Formato con black

---

## 🎯 PRÓXIMOS PASOS

1. **Desplegar en Replit**
   ```bash
   git push
   ```

2. **Conectar con Base44**
   - Usar el SuperAgent creado: https://app.base44.com/superagent/69d28c760c0fc513098b94ea
   - Configurar variables de entorno

3. **Configurar LangChain** (opcional)
   - Agregar API keys en `.env`
   - Habilitar agentes IA avanzados

4. **Monitorear en Tiempo Real**
   ```bash
   GET /supervisor/monitor/all
   ```

---

## 🤝 CONTRIBUIR

```bash
# Crear rama de feature
git checkout -b feature/tu-feature

# Hacer cambios y commit
git commit -m "feat: descripción del cambio"

# Push y crear Pull Request
git push origin feature/tu-feature
```

---

## 📞 SOPORTE

### Documentación Interactiva
- Swagger: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Memoria del Sistema
```bash
GET /memory/status
```

### Estado General
```bash
GET /status
```

---

## 📄 LICENCIA

MIT License - Ver `LICENSE` para detalles

---

## 🔥 CREADOR

**Profesor Horacio Lucifer**
- GitHub: [@profesorhoraciolucifer](https://github.com/profesorhoraciolucifer)
- Base44: [@horacio-luciani](https://app.base44.com/@horacio-luciani)

---

**INFERNO - Programación de Alto Nivel Distribuida** 🔥

*El sistema que nunca olvida, siempre aprende, y se cuida a sí mismo.*
