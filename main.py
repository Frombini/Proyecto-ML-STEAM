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