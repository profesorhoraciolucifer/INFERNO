# INFERNO 🔥

**Sistema de Programación de Alto Nivel para Descargar y Usar Unido a la Red**

INFERNO es una plataforma distribuida de alto nivel construida con **Python, FastAPI y LangChain**, diseñada para integración seamless con Replit, Base44 y agentes de IA.

## Características

- 🚀 **API REST moderna** con FastAPI
- 🤖 **Integración LangChain** para agentes de IA
- 📦 **Descarga y gestión de recursos** desde la red
- 🔗 **Conexión fácil con Base44**
- ☁️ **Deployable en Replit**
- 🔐 **Configuración segura** con variables de entorno

## Quick Start

### Requisitos
- Python 3.9+
- pip

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/profesorhoraciolucifer/INFERNO.git
cd INFERNO

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales

# Ejecutar la aplicación
python main.py
```

La aplicación estará disponible en `http://localhost:8000`

## Estructura del Proyecto

```
inferno/
├── main.py                 # Punto de entrada principal
├── requirements.txt        # Dependencias del proyecto
├── .env.example           # Template de configuración
├── .gitignore             # Archivos a ignorar en git
├── config/
│   └── settings.py        # Configuración centralizada
├── agents/
│   ├── __init__.py
│   └── llm_agent.py       # Agentes LangChain
├── api/
│   ├── __init__.py
│   ├── routes.py          # Endpoints FastAPI
│   └── models.py          # Modelos de datos Pydantic
├── integrations/
│   ├── __init__.py
│   ├── base44.py          # Integración con Base44
│   └── replit.py          # Utilidades para Replit
├── services/
│   ├── __init__.py
│   ├── download.py        # Servicio de descargas
│   └── network.py         # Servicios de red
└── tests/
    └── test_api.py        # Tests unitarios
```

## API Endpoints

### Health Check
```bash
GET /health
```

### Agents
```bash
POST /api/agents/chat
GET /api/agents/list
```

### Downloads
```bash
POST /api/download
GET /api/download/{id}/status
```

## Documentación Interactiva

Una vez ejecutando, accede a la documentación interactiva:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Integración con Base44

Configura tu API key de Base44 en `.env`:

```env
BASE44_API_KEY=tu_api_key_aqui
BASE44_API_URL=https://api.base44.com
```

## Integración con LangChain

Configura tu API key de LangChain:

```env
LANGCHAIN_API_KEY=tu_api_key_aqui
LANGCHAIN_ENVIRONMENT=production
```

## Deployment en Replit

1. Importa este repositorio en Replit
2. Configura las variables de entorno en Replit Secrets
3. Ejecuta `python main.py`
4. Tu aplicación será accesible vía URL de Replit

## Desarrollo

### Ejecutar tests
```bash
pytest tests/ -v
```

### Formato de código
```bash
black .
pylint **/*.py
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo licencia MIT. Ver `LICENSE` para más detalles.

## Contacto

**Profesor Horacio Lucifer**
- GitHub: [@profesorhoraciolucifer](https://github.com/profesorhoraciolucifer)
- Email: profesorhoraciolucifer@example.com

---

**INFERNO** - Programación de Alto Nivel Distribuida 🔥
