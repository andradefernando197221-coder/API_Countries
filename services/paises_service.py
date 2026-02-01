import requests

BASE_URL = "https://restcountries.com/v3.1"


def obtener_paises():
    url = f"{BASE_URL}/all"
    params = {
        "fields": "name,capital,region,population,flags"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            return {
                "error": "No se pudo obtener información de países",
                "status_code": response.status_code
            }

        data = response.json()
        paises = []

        for pais in data:
            paises.append({
                "nombre": pais.get("name", {}).get("common", "No disponible"),
                "capital": pais.get("capital")[0] if pais.get("capital") else "No disponible",
                "region": pais.get("region", "No disponible"),
                "poblacion": pais.get("population", 0),
                "bandera": pais.get("flags", {}).get("png", "")
            })

        return paises

    except requests.exceptions.RequestException as e:
        return {
            "error": "Error al conectar con la API REST Countries",
            "detalle": str(e)
        }


def obtener_pais_por_nombre(nombre: str):
    url = f"{BASE_URL}/name/{nombre}"
    params = {
        "fields": "name,capital,region,population,flags"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 404:
            return None

        if response.status_code != 200:
            return {
                "error": "Error al consultar el país",
                "status_code": response.status_code
            }

        data = response.json()
        pais = data[0]

        return {
            "nombre": pais.get("name", {}).get("common", "No disponible"),
            "capital": pais.get("capital")[0] if pais.get("capital") else "No disponible",
            "region": pais.get("region", "No disponible"),
            "poblacion": pais.get("population", 0),
            "bandera": pais.get("flags", {}).get("png", "")
        }

    except requests.exceptions.RequestException as e:
        return {
            "error": "Error al conectar con la API REST Countries",
            "detalle": str(e)
        }
