from fastapi import FastAPI, HTTPException, Request
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
                        background-color: #f0f0f0; /* Cambiar a tu color de fondo deseado */
                        color: #333333; /* Texto negro */
                        margin: 20px;
                        font-family: 'Arial', sans-serif; /* Puedes cambiar la fuente si lo deseas */
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

                    a {
                        color: #0000FF; /* Color del enlace (azul en este caso) */
                        text-decoration: none; /* Elimina el subrayado de los enlaces */
                    }

                    a:hover {
                        text-decoration: underline; /* Subrayado al pasar el mouse sobre el enlace */
                    }
                </style>
            </head>
            <body>
                <h1>Bienvenidos a mi API</h1>
                <p>Mi nombre es Francisco Rombini de la academia SOYHENRY, soy de la cohorte DataFT-17</p>

                <h2>Endpoints Disponibles:</h2>
                <ul>
                    <li><a href="https://proyecto-ml-steam.onrender.com/PlayTimeGenre/Action">/PlayTimeGenre/Action</a></li>
                    <li><a href="https://proyecto-ml-steam.onrender.com/UserForGenre/Adventure">/UserForGenre/Adventure</a></li>
                    <li><a href="https://proyecto-ml-steam.onrender.com/UsersRecommend/2012">/UsersRecommend/2012</a></li>
                    <li><a href="https://proyecto-ml-steam.onrender.com/UsersWorstDeveloper/2014">/UsersWorstDeveloper/2014</a></li>
                    <li><a href="https://proyecto-ml-steam.onrender.com/sentiment_analysis/Valve">/sentiment_analysis/Valve</a></li>
                    <li><a href="https://proyecto-ml-steam.onrender.com/recomendacion_juego/10">/recomendacion_juego/10</a></li>
                </ul>
            </body>
        </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/PlayTimeGenre/{genero}")
async def play_time_genre(genero:str):
    try:
        resultado = PlayTimeGenre(genero)
        return resultado
    except Exception as e:
        return {"error": str(e)}   
    
@app.get("/UserForGenre/{genero}")
async def user_for_genre(genero:str):
    try:
        resultado = UserForGenre(genero)
        return resultado
    except Exception as e:
        return {"error": str(e)}

@app.get("/UsersRecommend/{anio}")
async def users_recommend(anio:int):
    try:
        anio_int = int(anio)
    except ValueError:
        return {"detail": [{"type": "invalid_input", "msg": "El año debe ser un número entero"}]}

    result = UsersRecommend(anio_int)
    return result
    
@app.get("/UsersWorstDeveloper/{anio}")
async def users_worst_developer(anio:int):
    try:
        anio_int = int(anio)
    except ValueError:
        return {"detail": [{"type": "invalid_input", "msg": "El año debe ser un número entero"}]}

    result = UsersWorstDeveloper(anio_int)
    return result
    

@app.get("/sentiment_analysis/{desarrolladora}")
async def sentiment_analysis_route(desarrolladora:str):
    try:
        resultado = sentiment_analysis(desarrolladora)
        return resultado
    except Exception as e:
        return {"error": str(e)}  
    

@app.get("/recomendacion_juego/{id_juego}")
async def recomendacion_juego_route(id_juego:int):
    try:
        id_juego = int(id_juego)
    except ValueError:
        return {"detail": [{"type": "invalid_input", "msg": "El año debe ser un número entero"}]}

    result = recomendacion_juego(id_juego)
    return result     