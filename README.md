Countries API - Documentación del Contrato de API

## Descripción General

### ¿Qué hace la API?
La Countries API es un servicio REST que permite consultar información básica de países del mundo a través de su nombre.

### ¿Qué información devuelve?
Dependiendo del endpoint, la API puede devolver:

Nombre del país
Capital
Región
Población
Bandera (URL)
Idiomas
Moneda(s)

### ¿Para qué sirve?
Esta API sirve para:
Aplicaciones educativas
Proyectos académicos
Prácticas de consumo de APIs REST
Mostrar información de países en aplicaciones web o móviles



### Endpoints utilizados

URL del endpoint
/countries/{name}

Método HTTP
GET

## Parámetros requeridos

Parámetro	Tipo	Descripción
name	string	Nombre del país a consultar (ej: colombia, peru, mexico)
📤 Ejemplo de petición
GET http://127.0.0.1:8000/countries/colombia


O usando curl:

curl -X GET "http://127.0.0.1:8000/countries/colombia" -H "accept: application/json"

##  Respuesta exitosa (200 OK)
Ejemplo de respuesta (JSON)
{
  "name": "Colombia",
  "capital": "Bogotá",
  "region": "Americas",
  "population": 50882884,
  "flag": "https://flagcdn.com/co.svg",
  "languages": ["Spanish"],
  "currencies": ["COP"]
}

## Descripción de los campos más importantes

## Campo                       Descripción
name	                    Nombre oficial del país
capital                  	Capital del país
region	                  Región geográfica
population	              Número aproximado de habitantes
flag	                    URL de la imagen de la bandera
languages	                Idiomas principales
currencies                Monedas oficiales


## Manejo de errores

404 Not Found

##  Ejemplo de respuesta de error

{
  "detail": "Country not found"
}


## Error interno del servidor

500 Internal Server Error

## Ejemplo de respuesta
Internal Server Error


### Conclucion 

La API responde en formato JSON, El nombre del país no es sensible a mayúsculas
Está diseñada para fines académicos y de aprendizaje
Se recomienda validar el nombre del país antes de hacer la petición
