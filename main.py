from fastapi import FastAPI
import pandas as pd
import json
import numpy as np
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse
from funciones import PlayTimeGenre
from funciones import UserForGenre
from funciones import UsersRecommend
from funciones import UsersWorstDeveloper
from funciones import sentiment_analysis
from funciones import recomendacion_juego

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
def hola():
    html_content = """
        <!DOCTYPE html>
        <html lang="es">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Endpoint-APIs de Francisco Rombini</title>
                <style>
                    body {
                        font-family: 'Arial', sans-serif; /* Cambiar a la fuente deseada */
                        background-color: #ffffff; /* Fondo blanco */
                        color: #000000; /* Texto negro */
                        margin: 20px;
                    }

                    h1 {
                        font-size: 2em; /* Tamaño de la fuente para h1 */
                    }

                    h2 {
                        font-size: 1.5em; /* Tamaño de la fuente para h2 */
                    }

                    ul {
                        list-style-type: none; /* Elimina los puntos de la lista */
                        padding: 0;
                    }

                    li {
                        margin-bottom: 10px; /* Espacio entre elementos de la lista */
                    }
                </style>
            </head>
            <body>
                <h1>Bienvenidos a mi API</h1>
                <p>Mi nombre es Francisco Rombini de la academia SOYHENRY, soy de la cohorte DataFT-17</p>

                <h2>Endpoints Disponibles:</h2>
                <ul>
                    <li><strong>/PlayTimeGenre/Action:</strong> Devuelve el año con mas tiempo de juego para un género específico.</li>
                    <li><strong>/UserForGenre/Adventure:</strong> Proporciona detalles sobre el usuario que acumula más horas jugadas para el género dado.</li>
                    <li><strong>/UsersRecommend/2012:</strong> Devuelve el top 3 de juegos mas recomendados por usuarios para el año dado.</li>
                    <li><strong>/UsersWorstDeveloper/2014:</strong> Devuelve el top 3 de desarrolladoras con juegos menos recomendados por usuarios para el año dado.</li>
                    <li><strong>/sentiment_analysis/Valve:</strong> Devuelve análisis de sentimientos para un desarrollador específico.</li>
                    <li><strong>/recomendacion_juego/10:</strong> Recomienda 5 juegos similares al id de juego ingresado.</li>
                </ul>
            </body>
        </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/PlayTimeGenre/{genero}")
async def user(genero: str):
    try:
        resultado = PlayTimeGenre(genero)
        return resultado
    except Exception as e:
        return {"error": str(e)}   
    
@app.get("/UserForGenre/{genero}")
async def user(genero: str):
    try:
        resultado = UserForGenre(genero)
        return resultado
    except Exception as e:
        return {"error": str(e)}

@app.get("/UsersRecommend/{anio}")
async def user(anio:int):
    try:
        resultado = UsersRecommend(anio)
        return resultado
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/UsersWorstDeveloper/{anio}")
async def user(anio:int):
    try:
        resultado = UsersWorstDeveloper(anio)
        return resultado
    except Exception as e:
        return {"error": str(e)}  
    

@app.get("/sentiment_analysis/{desarrolladora}")
async def user(desarrolladora:str):
    try:
        resultado = sentiment_analysis(desarrolladora)
        return resultado
    except Exception as e:
        return {"error": str(e)}  
    

@app.get("/recomendacion_juego/{id_juego}")
async def user(id_juego:int):
    try:
        resultado = recomendacion_juego(id_juego)
        return resultado
    except Exception as e:
        return {"error": str(e)}     