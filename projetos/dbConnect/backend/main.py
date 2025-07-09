import uvicorn
from fastapi import FastAPI
from infra.database_connection import connect_to_db
from schema.Pessoa import PessoaCreate, PessoaResponse
from crud import criar_pessoa

app = FastAPI()

@app.get("/")
async def read_root():        
    return {"message": "Hello, World!"}

@app.post("/pessoas", response_model=PessoaResponse)
async def criar_pessoa_endpoint(pessoa: PessoaCreate):
    nova_pessoa = await criar_pessoa(pessoa)
    return nova_pessoa


if __name__ == '__main__':
      connect_to_db
      #uvicorn.run(app, host="0.0.0.0", port=8005)


