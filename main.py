from fastapi import FastAPI
import pandas as pd
import json
import numpy as np
from fastapi.responses import JSONResponse
from funciones import PlayTimeGenre

app = FastAPI()

@app.get('/')
def hola():
    return {'Esta es mi APi, Soy Francisco Rombini'}

'''1.def PlayTimeGenre( genero : str ): Debe devolver año con mas horas jugadas para dicho género.
Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}'''

@app.get("/PlayTimeGenre/{genero}")
async def user(genero: str):
    try:
        resultado = PlayTimeGenre(genero)
        return resultado
    except Exception as e:
        return {"error": str(e)}   