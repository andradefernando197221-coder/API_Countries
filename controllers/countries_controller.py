from fastapi import APIRouter, HTTPException
from services.paises_service import (
    obtener_paises,
    obtener_pais_por_nombre
)

router = APIRouter(
    prefix="/countries",
    tags=["Countries"]
)


@router.get("/")
def get_countries():
    resultado = obtener_paises()

    if isinstance(resultado, dict) and "error" in resultado:
        raise HTTPException(status_code=500, detail=resultado)

    return {
        "status": "success",
        "total": len(resultado),
        "data": resultado
    }


@router.get("/{nombre}")
def get_country_by_name(nombre: str):
    resultado = obtener_pais_por_nombre(nombre)

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail="País no encontrado"
        )

    if isinstance(resultado, dict) and "error" in resultado:
        raise HTTPException(status_code=500, detail=resultado)

    return {
        "status": "success",
        "data": resultado
    }
