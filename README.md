<h1 align="center"> Proyecto-ML-STEAM </h1>

![steam_1](https://github.com/Frombini/Proyecto-ML-STEAM/assets/137807368/5bc892bc-8922-4490-ae9d-619258565383)

## Index

## Introduccion

Bienvenidos al proyecto de Machine learning de Steam. nuestro desafio planteado para este proyecto consiste en desarrollar un proceso de MLOs que incluya etapas de Ingeniería de Datos con Extraction, Transform and Load (ETL), pasando al Machine Learning, con Exploratory Data Analysis (EDA), junto con la exploración y entrenamiento de modelos, finalizando con el deployment tanto del modelo como endpoints.

## Rol a Desarrollar

Empezaste a trabajar como Data Scientist en Steam, una plataforma multinacional de videojuegos. Vas a crear tu primer modelo de ML que soluciona un problema de negocio: Steam pide que te encargues de crear un sistema de recomendación de videojuegos para usuarios.

Vas a sus datos y te das cuenta que la madurez de los mismos es poca (ok, es nula): Datos anidados, de tipo raw, no hay procesos automatizados para la actualización de nuevos productos, entre otras cosas… haciendo tu trabajo imposible .
Debes empezar desde 0, haciendo un trabajo rápido de Data Engineer y tener un MVP (Minimum Viable Product) para el cierre del proyecto!

## Propuesta del Tabajo

Propuesta de trabajo (requerimientos de aprobación)

Transformaciones: Para este MVP no se te pide transformaciones de datos(aunque encuentres una motivo para hacerlo) pero trabajaremos en leer el dataset con el formato correcto. Puedes eliminar las columnas que no necesitan para responder las consultas o preparar los modelos de aprendizaje automático, y de esa manera optimizar el rendimiento de la API y el entrenamiento del modelo.

Feature Engineering: En el dataset user_reviews se incluyen reseñas de juegos hechos por distintos usuarios. Debes crear la columna 'sentiment_analysis' aplicando análisis de sentimiento con NLP con la siguiente escala: debe tomar el valor '0' si es malo, '1' si es neutral y '2' si es positivo. Esta nueva columna debe reemplazar la de user_reviews.review para facilitar el trabajo de los modelos de machine learning y el análisis de datos. De no ser posible este análisis por estar ausente la reseña escrita, debe tomar el valor de 1.

Desarrollo API: Propones disponibilizar los datos de la empresa usando el framework FastAPI. Las consultas que propones son las siguientes:

Debes crear las siguientes funciones para los endpoints que se consumirán en la API. 

    def PlayTimeGenre( genero : str ): Debe devolver año con mas horas jugadas para dicho género.
Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}

    def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}

    def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

    def UsersWorstDeveloper( año : int ): Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

    def sentiment_analysis( empresa desarrolladora : str ): Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.
Ejemplo de retorno: {'Valve' : [Negative = 182, Neutral = 120, Positive = 278]}

Sistema de recomendación item-item:
    def recomendacion_juego( id de producto ): Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.

Importante:El MVP tiene que ser una API que pueda ser consumida segun los criterios de API REST o RESTful desde cualquier dispositivo conectado a internet. Algunas herramientas como por ejemplo, Streamlit, si bien pueden brindar una interfaz de consulta, no cumplen con las condiciones para ser consideradas una API, sin workarounds.
Deployment: Conoces sobre Render y tienes un tutorial de Render que te hace la vida mas fácil. También podrías usar Railway, o cualquier otro servicio que permita que la API pueda ser consumida desde la web.

## Obejtivos

Queremos desarrollar y desplegar un sistema de recomendacion de juegos, teniendo endopints que se consumen online y pueden responder las funciones que nos pidieron para desarrollar
Esto lo vamos a hacer aprovechando los conjuntos de datos y nos enfocaremos en lograr los siguientes hitos específicos:

Transformación y Limpieza de Datos

Aplicaremos técnicas de Extracción, Transformación y Carga (ETL) y análisis Exploratorio de Datos (EDA)

Diseñaremos e implementaremos una API que será consumida online para responder las necesidades antes mencionadas.

Modelo de Aprendizaje Automático

Desarrollaremos un modelo de aprendizaje automático que va a predecir con precisión una recomendacion para juegos, donde agregando el id del item del tipo que queremos que nos recomiende, nos devolvera una lista con los 5 juegos recomendados por el genero del juego agregado.

Despliegue de la API

Implementaremos la API en un entorno de producción. Queremos que sea accesible para todos, aplicando buenas prácticas para garantizar un rendimiento óptimo.

MLOps: Gestión Eficiente

Estableceremos una infraestructura de MLOps para navegar sin problemas por todas las etapas de este emocionante proyecto. Desde la transformación de datos hasta el despliegue, estamos comprometidos con una operación eficiente y sin contratiempos.

## Ámbito de Proyecto

Enlace para descarga de los archivos JSON
https://drive.google.com/drive/folders/1VUSnjqYKaTzJ24kreKPwDhcEiu-_6IPG?usp=drive_link


## Pila de Tecnologías

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)


## Pasos realizados para el proyecto

ETL(extract, transform, load)
EDA
modelado de los datos
consumir datos limpios
Machine learning
montar api (local api, deploy-Render)
entrenamiento de los datos

## Colaboradores

-colaboradores : Gabriel Veron, , Juan Ochoa, Lucas Koch

Quiero agradecer a mis compañeros de Cohorte que me ayudaron en este proceso:

| Johanna Rangel | Uriel Cercero | Gretel Sanchez |
| --- | --- | --- |
| [<img src="https://avatars.githubusercontent.com/JohannaRangel" width=75><br><sub>Johanna Rangel</sub>](https://github.com/JohannaRangel) | [<img src="https://avatars.githubusercontent.com/u/121000341?v=4" width=75><br><sub>Uriel Cercero</sub>](https://github.com/JUrielCerecero) | [<img src="https://avatars.githubusercontent.com/u/120042696?v=4" width=75><br><sub>Gretel Sanchez</sub>](https://github.com/KGSanchezM)



