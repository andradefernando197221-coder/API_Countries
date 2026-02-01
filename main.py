"""
=============================================================================
PUNTO DE ENTRADA DE LA APLICACIÓN FASTAPI
=============================================================================

Este es el archivo principal de la aplicación. Aquí se configura e inicializa
la instancia de FastAPI y se registran todos los routers (controladores).

FastAPI es un framework moderno y de alto rendimiento para construir APIs
con Python 3.7+ basado en estándares como OpenAPI y JSON Schema.

Características principales de FastAPI:
- Rápido
- Fácil
- Robusto
- Documentado (Swagger UI y ReDoc)

Para ejecutar la aplicación:
    uvicorn main:app --reload

Documentación automática disponible en:
    - Swagger UI: http://localhost:8000/docs
    - ReDoc: http://localhost:8000/redoc

Autor: Fernando Andrade
Fecha: Enero 2026
=============================================================================
"""

# =============================================================================
# IMPORTS
# =============================================================================
from fastapi import FastAPI

# Routers (controladores)
from controllers.weathercontroller import router as weather_router
from controllers.countries_controller import router as countries_router


# =============================================================================
# CONFIGURACIÓN DE LA APLICACIÓN
# =============================================================================
app = FastAPI(
    title="API de Consumo de Servicios Externos",
    description="""
    ## API de Consumo de APIs Externas 🌍🌤️
    
    Esta API demuestra el consumo de servicios externos utilizando
    una arquitectura modular basada en controladores y servicios.
    
    ### Servicios disponibles:
    * Clima (OpenWeatherMap)
    * Países (REST Countries)
    
    ### Tecnologías utilizadas:
    * FastAPI
    * Requests
    * Pydantic
    * APIs públicas externas
    """,
    version="1.1.0",
    contact={
        "name": "Fernando Andrade",
        "email": "tu@email.com"
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    }
)


# =============================================================================
# ENDPOINT RAÍZ (HOME)
# =============================================================================
@app.get(
    "/",
    summary="Página de inicio",
    description="Endpoint de bienvenida que confirma que la API está funcionando",
    tags=["General"]
)
def home():
    return {
        "message": "Welcome to the External APIs Consumer",
        "docs": "Visita /docs para ver la documentación interactiva",
        "version": "1.1.0"
    }


# =============================================================================
# REGISTRO DE ROUTERS
# =============================================================================
# Weather API
app.include_router(weather_router)

# Countries API
app.include_router(countries_router)


# =============================================================================
# EJECUCIÓN LOCAL
# =============================================================================
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
