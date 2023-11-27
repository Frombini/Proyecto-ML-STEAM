import pandas as pd
import numpy as np

'''1.def PlayTimeGenre( genero : str ): Debe devolver año con mas horas jugadas para dicho género.
    Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}'''

def PlayTimeGenre(genero:str):
    # Leemos el archivo consulta1.csv para utilizar la funcion
    consulta1 = pd.read_csv('consulta1.csv')
        # Función para juntar palabras en la columna 'Genres'
    def juntar_palabras(genres):
        palabras = genres.split(', ')
        palabras_juntas = ''.join(palabra.replace(' ', '') for palabra in palabras)
        return palabras_juntas.capitalize()
    # Aplicamos la función a la columna 'Genres'
    consulta1['Genres_juntos'] = consulta1['Genres'].apply(juntar_palabras)
    consulta1['Genres_juntos'] = consulta1['Genres_juntos']
    # Dropear la columna 'Genres'
    consulta1 = consulta1.drop('Genres', axis=1)
    # Renombrar la columna 'Genres_juntos' a 'Genres'
    consulta1 = consulta1.rename(columns={'Genres_juntos': 'Genres'})
    genero = genero.capitalize()
    # Filtrar el DataFrame para el género específico
    filtered_df = consulta1[consulta1['Genres'] == genero]

    if filtered_df.empty:
        return {"Género no encontrado en el conjunto de datos"}

    # Agrupar por año de lanzamiento y sumar las horas jugadas
    grouped_df = filtered_df.groupby('ReleaseDate')['PlaytimeForever'].sum()

    # Encontrar el año con más horas jugadas
    max_year = grouped_df.idxmax()

    # Convertir max_year a un tipo de datos nativo de Python
    max_year = int(max_year)

    # Devolver el resultado como un diccionario
    result = {"Año de lanzamiento con más horas jugadas para {}:".format(genero): max_year}

    return result

'''2. def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
    Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}'''

def UserForGenre(genero:str):
    #Carga de archivo
    consulta2 = pd.read_csv('consulta2.csv')
    #Funcion para juntar palabras en este caso generos de dos o mas nombres
    def juntar_palabras(genres):
        palabras = genres.split(', ')
        palabras_juntas = ''.join(palabra.replace(' ', '') for palabra in palabras)
        return palabras_juntas.capitalize()
    # Aplicamos la función a la columna 'Genres'
    consulta2['Genres_juntos'] = consulta2['Genres'].apply(juntar_palabras)
    consulta2['Genres_juntos'] = consulta2['Genres_juntos']
    # Dropear la columna 'Genres'
    consulta2 = consulta2.drop('Genres', axis=1)
    # Renombrar la columna 'Genres_juntos' a 'Genres'
    consulta2 = consulta2.rename(columns={'Genres_juntos': 'Genres'})
    genero = genero.capitalize()
    # Filtrar el DataFrame por el género dado
    genre_data = consulta2[consulta2['Genres'] == genero]

    # Encontrar al usuario con más horas jugadas para ese género
    top_user = genre_data.loc[genre_data['PlaytimeForever'].idxmax()]['UserId']

    # Crear una lista de acumulación de horas jugadas por año
    hours_by_year = genre_data.groupby('ReleaseDate')['PlaytimeForever'].sum().reset_index()
    hours_by_year = hours_by_year.rename(columns={'ReleaseDate': 'Año', 'PlaytimeForever': 'Horas'})
    # Convertir las horas a enteros (int) dividiendo por 60
    hours_by_year['Horas'] = (hours_by_year['Horas'] / 60).astype(int)
    hours_list = hours_by_year.to_dict(orient='records')

    # Crear el diccionario de retorno
    result = {
        "Usuario con más horas jugadas para Género {}".format(genero): top_user,
        "Horas jugadas": hours_list
    }

    return result

'''3. def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
    Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]'''

def UsersRecommend(anio:int):
    # Leemos el archivo consulta3.csv para utilizar la funcion
    consulta3 = pd.read_csv('consulta3.csv')
    if type(anio) != int:
        return {"Debes colocar el año en entero, EJ:2015"}
    if anio < consulta3['YearPosted'].min() or anio > consulta3['YearPosted'].max():
        return {"Año no encontrado en el conjunto de datos"}
    
    # Filtrar por el año especificado y reseñas recomendadas y positivas/neutrales
    filtered_reviews = consulta3[(consulta3['YearPosted'] == anio)]
    
    # Obtener el top 3 de juegos más recomendados
    top3_games = filtered_reviews.nlargest(3, 'total_sentiment_analysis')[['ItemName', 'total_sentiment_analysis']]
    
    # Crear el formato de retorno
    retorno = [{f"Puesto {i+1}": juego} for i, juego in enumerate(top3_games['ItemName'])]

    return retorno

'''4. def UsersWorstDeveloper( año : int ): Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
    Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]'''


def UsersWorstDeveloper(anio:int):
    consulta4 = pd.read_csv('consulta4.csv')
    if type(anio) != int:
        return {"Debes colocar el año en entero, EJ:2015"}
    if anio < consulta4['YearPosted'].min() or anio > consulta4['YearPosted'].max():
        return {"Año no encontrado en el conjunto de datos"}
    # Filtrar el DataFrame para el año dado y donde las recomendaciones son False y comentarios negativos
    filtered_df = consulta4[consulta4['YearPosted'] == anio]

    # Seleccionar las 3 desarrolladoras con más revisiones negativas
    top_worst = filtered_df.groupby('Developer')['CountSentiment'].sum().nlargest(3).reset_index()

    # Crear la lista de resultados en el formato deseado
    result = [{"Puesto {}: {}".format(i + 1, row['Developer'])} for i, row in top_worst.iterrows()]

    return result

'''5. def sentiment_analysis( empresa desarrolladora : str ): Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.
    Ejemplo de retorno: {'Valve' : [Negative = 182, Neutral = 120, Positive = 278]}'''
 
def sentiment_analysis(desarrolladora:str):
    consulta5 = pd.read_csv('consulta5.csv')
    # Función para juntar palabras en la columna 'Genres'
    def juntar_palabras(genres):
        palabras = genres.split(', ')
        palabras_juntas = ''.join(palabra.replace(' ', '') for palabra in palabras)
        return palabras_juntas.capitalize()

    # Aplicar la función a la columna 'Developer'
    consulta5['Developer'] = consulta5['Developer'].apply(juntar_palabras)

    desarrolladora = desarrolladora.capitalize()
    if type(desarrolladora) != str:
        return "Debes colocar un desarrollador de tipo str, EJ:'Valve'"
    if len(desarrolladora) == 0:
        return "Debes poner un desarrolador en tipo String"
    # Filtramos el DataFrame para la empresa desarrolladora especificada
    filtered_df = consulta5[consulta5['Developer'] == desarrolladora]

    # Contamos la cantidad de registros para cada categoría de sentimiento
    sentiment_counts = filtered_df['sentiment_analysis'].value_counts()

    # Creamos el diccionario de retorno
    result = {desarrolladora: f"[Negative = {sentiment_counts.get(0, 0)}, Neutral = {sentiment_counts.get(1, 0)}, Positive = {sentiment_counts.get(2, 0)}]"}
    return result

'''Sistema de recomendación item-item:
    6. def recomendacion_juego( id de producto ): Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.'''

def recomendacion_juego(id_juego:int):
    # Cargamos el csv de consulta6 para alimentar la funcion
    modelo_df = pd.read_csv('consulta6.csv')
    # Verificar si la ID del juego está en la columna "ItemId"
    if id_juego not in modelo_df["ItemId"].values:
        return "El id ingresado no existe en el dataset"
    # Buscar el índice del juego con la ID dada
    indice_juego = modelo_df[modelo_df["ItemId"] == id_juego].index[0]

    # Obtener las recomendaciones para ese juego
    recomendaciones = modelo_df.iloc[indice_juego]["RecomendacionesTop5"]

    return recomendaciones