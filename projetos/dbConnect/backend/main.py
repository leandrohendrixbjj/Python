import uvicorn
from fastapi import FastAPI
from infra.database_connection import connect_to_db

from schema.Pessoa import PessoaCreate, PessoaResponse
from schema.NotaFiscal import NotaFiscalCreate, NotaFiscalResponse

from crud.pessoa import criar_pessoa
from crud.nota_fiscal import criar_nota_fiscal

app = FastAPI()

@app.get("/")
async def read_root():        
    return {"message": "Hello, World!"}

@app.post("/pessoas", response_model=PessoaResponse)
async def criar_pessoa_endpoint(pessoa: PessoaCreate):
    nova_pessoa = await criar_pessoa(pessoa)
    return nova_pessoa

@app.post("/notafiscal", response_model=NotaFiscalResponse)
async def criar_notafiscal_endpoint(nota_fiscal: NotaFiscalCreate):
    nova_fiscal = await criar_nota_fiscal(nota_fiscal)
    return nova_fiscal

if __name__ == '__main__':
      connect_to_db
      #uvicorn.run(app, host="0.0.0.0", port=8005)


