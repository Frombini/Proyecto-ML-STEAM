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
            
        'mensaje': 'Bienvinidos a mi API, mi nombre es Francisco Rombini de la academia SOYHENRY, de la cohorte DataFT-17',
        
        'EJ1': 'https://proyecto-ml-steam.onrender.com/PlayTimeGenre/Action',
        
        'EJ2': 'https://proyecto-ml-steam.onrender.com/UserForGenre/Adventure',
        
        'EJ3': 'https://proyecto-ml-steam.onrender.com/UsersRecommend/2012',
        
        'EJ4': 'https://proyecto-ml-steam.onrender.com/UsersWorstDeveloper/2014',
        
        'EJ5': 'https://proyecto-ml-steam.onrender.com/sentiment_analysis/Valve ',

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