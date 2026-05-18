from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World"}


@app.get("/about")
def hello():
    return {"message":"Welcome to About Section !!"}

#LEARN: To run this file use command  : uvicorn main:app --reload 



