import pandas as pd
import numpy as np

def PlayTimeGenre(genero):
    # Leemos el archivo consulta1.csv para utilizar la funcion
    consulta1 = pd.read_csv('consulta1.csv')
    # Filtrar el DataFrame para el género específico
    filtered_df = consulta1[consulta1['Genres'] == genero]

    if filtered_df.empty:
        return {"Género no encontrado en el conjunto de datos"}

    # Agrupar por año de lanzamiento y sumar las horas jugadas
    grouped_df = filtered_df.groupby('ReleaseDate')['PlaytimeForever'].sum()

    # Encontrar el año con más horas jugadas
    max_year = grouped_df.idxmax()

    # Devolver el resultado como un diccionario
    result = {"Año de lanzamiento con más horas jugadas para {}:".format(genero): max_year}

    return result