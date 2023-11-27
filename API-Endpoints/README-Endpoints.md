## Informacion


**Introducción**

Documentación de API para Análisis de Videojuegos

Estas APIs proporcionan funcionalidades clave para analizar y obtener información relevante sobre el mundo de los videojuegos. A través de varios endpoints, los usuarios pueden acceder a datos valiosos relacionados con los géneros, usuarios, recomendaciones y análisis de sentimientos de las reseñas. A continuación, se describen brevemente las funciones principales de cada endpoint:

    PlayTimeGenre(genero: str)
        Descripción: Retorna el año de lanzamiento con más horas jugadas para un género específico.
        Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X": 2013}

    UserForGenre(genero: str)
        Descripción: Retorna el usuario que acumula más horas jugadas para un género dado, junto con una lista de acumulación de horas jugadas por año.
        Ejemplo de retorno: {"Usuario con más horas jugadas para Género X": "us213ndjss09sdf", "Horas jugadas": [{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}

    UsersRecommend(año: int)
        Descripción: Retorna el top 3 de juegos MÁS recomendados por usuarios para un año dado, considerando reviews con recomendación positiva o neutral.
        Ejemplo de retorno: [{ "Puesto 1": X }, { "Puesto 2": Y }, { "Puesto 3": Z }]

    UsersWorstDeveloper(año: int)
        Descripción: Retorna el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para un año dado, considerando reviews con recomendación negativa.
        Ejemplo de retorno: [{ "Puesto 1": X }, { "Puesto 2": Y }, { "Puesto 3": Z }]

    sentiment_analysis(empresa_desarrolladora: str)
        Descripción: Retorna un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas categorizados por análisis de sentimiento.
        Ejemplo de retorno: {'Valve': [Negative = 182, Neutral = 120, Positive = 278]}

    recomendacion_usuario(id_usuario)
        Descripción: Ingresando el ID de un usuario, devuelve una lista con 5 juegos recomendados para dicho usuario.

**Endpoints:**

Url Principial: [Proyecto-ML-Steam](https://proyecto-ml-steam.onrender.com/) - proyecto-ml-steam.onrender.com

              Una introduccion con ejemplos para probar los endpoints  

1- [PlayTimeGenre](https://proyecto-ml-steam.onrender.com/PlayTimeGenre/Action) - proyecto-ml-steam.onrender.com/PlayTimeGenre/{genero}

Estos son los generos disponibles:
Action, Adventure, Animation & Modeling, Audio Production, Casual, Design & Illustration, Early Access, Education, Free to Play, Indie, Massively Multiplayer, Photo Editing, RPG, Racing, Simulation, Software Training, Sports, Strategy, Utilities, Video Production, Web Publishing 

2-[UserForGenre](https://proyecto-ml-steam.onrender.com/UserForGenre/Adventure) - proyecto-ml-steam.onrender.com/UserForGenre/{genero}

Estos son los generos disponibles:
Action, Adventure, Animation & Modeling, Audio Production, Casual, Design & Illustration, Early Access, Education, Free to Play, Indie, Massively Multiplayer, Photo Editing, RPG, Racing, Simulation, Software Training, Sports, Strategy, Utilities, Video Production, Web Publishing 

3-[UsersRecommend](https://proyecto-ml-steam.onrender.com/UsersRecommend/2012) - proyecto-ml-steam.onrender.com/UsersRecommend/{año}

Estos son los años disponibles:
2015, 2014, 2016, 2013, 2011, 2012, 2010

4-[UsersWorstDeveloper](https://proyecto-ml-steam.onrender.com/UsersWorstDeveloper/2014) - proyecto-ml-steam.onrender.com/UsersWorstDeveloper/{año}

Estos son los años disponibles:
2015, 2014, 2016, 2013, 2011, 2012

5-[sentiment_analysis](https://proyecto-ml-steam.onrender.com/sentiment_analysis/Valve) - proyecto-ml-steam.onrender.com/sentiment_analysis/{desarrollador}

Estos son algunos desarrolladores que se pueden buscar:
'Valve', 'Desconocido', 'Facepunch Studios', 'Bohemia Interactive', 'Smartly Dressed Games', 'Re-Logic', 'Digital Extremes', 'Tripwire Interactive', 'Gearbox Software,Aspyr (Mac & Linux)', 'Telltale Games', 'Daybreak Game Company', 'Bethesda Game Studios', 'Firaxis Games,Aspyr (Mac, Linux)', 'Edge of Reality', 'Treyarch', 'Avalanche Studios', 'Chucklefish', 'Freejam', 'Coffee Stain Studios', 'The Behemoth', 'Rockstar North'

6-[recomendacion_juego](https://proyecto-ml-steam.onrender.com/recomendacion_juego/10) - proyecto-ml-steam.onrender.com/recomendacion_juego/{id_juego}

Estos son algunos ids de juegos disponibles para probar:

10 320 340 360 380 400 420 440 500 550 570 620 630 730 1002 1200 1230 1250 1256 1257 1280 1300 1500 1510 1520 1530 1600 1610 1620 1630 1640 1670 1690 1700 1840 1900 1930 2100 2200 2210 2270 2280 2290 2300 2310 2320 2330 2340 2350 2360 2370 2390 2400 2420 2450 3400 3410 3420 3430 3440 3450 3460 3480 3483 3490 3500 3510 3520 3530 3540 3560 3570 3580 3590 3600 3610 3620 3700 3710 3720 3730 3800 3810 3820 3830 3838 3839 3900 3910 3920 3960 3980 3990 4000 4100 4230 4290 4300 4420 4460 4470 4500 4520 4530 4560 4570 4580 4700 4720 4760 4770 11390 11450 11480 11560 11590 11610 11900 11920 12100 12110 0

