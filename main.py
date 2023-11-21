from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hola():
    return {'Bienvenidos a mi api'}