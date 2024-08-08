from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    nome: str
    descricao: str 
    preco: float
    em_estoque: bool

@app.get("/")
def read_root():
    return {"Projeto Desafio TESTE"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item criado com sucesso!", "item": item}
