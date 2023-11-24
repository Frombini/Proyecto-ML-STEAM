from fastapi import FastAPI
import pandas as pd
import json
import numpy as np
from fastapi.responses import JSONResponse
from funciones import PlayTimeGenre
from funciones import UserForGenre
from funciones import UsersRecommend
from funciones import UsersWorstDeveloper
from funciones import sentiment_analysis
from funciones import recomendacion_juego

app = FastAPI()

@app.get('/')
def hola():
    return {
            
        'mensaje': 'Bienvinidos a mi API, mi nombre es Francisco Rombini de la academia SOYHENY, de la cohorte DataFT-17',
        'API1': 'https://proyecto-ml-steam.onrender.com/PlayTimeGenre/genero',
        'EJ1': 'https://proyecto-ml-steam.onrender.com/PlayTimeGenre/Action',
        'API2': 'https://proyecto-ml-steam.onrender.com/UserForGenre/genero',
        'EJ2': 'https://proyecto-ml-steam.onrender.com/UserForGenre/Adventure',
        'API3': 'https://proyecto-ml-steam.onrender.com/UsersRecommend/anio',
        'EJ3': 'https://proyecto-ml-steam.onrender.com/UsersRecommend/2012',
        'API4': 'https://proyecto-ml-steam.onrender.com/UsersWorstDeveloper/anio',
        'EJ4': 'https://proyecto-ml-steam.onrender.com/UsersWorstDeveloper/anio',
        'API5': 'https://proyecto-ml-steam.onrender.com/sentiment_analysis/desarrolladora',
        'EJ5': 'https://proyecto-ml-steam.onrender.com/sentiment_analysis/Valve ',
        'API6': 'https://proyecto-ml-steam.onrender.com/recomendacion_juego/id_juego',
        'EJ6': 'https://proyecto-ml-steam.onrender.com/recomendacion_juego/10'

            }

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