from fastapi import FastAPI
import cognitive as c
import psychometric as p
import technical as t

app = FastAPI()

@app.get("/")
async def text():
    return ("Woking ")

@app.get("/cognitive")
async def cogni(comp:str):
    return (c.entry(comp))

