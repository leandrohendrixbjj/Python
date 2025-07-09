from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional

"""
   É um modelo de dados usado para validar, converter e documentar os dados que entram 
   (request) e saem (response) da sua API.

   Ele faz essa validação antes de entrar na lógica do seu endpoint, e também filtra/valida 
   a resposta antes de enviar para o cliente.
"""

class PessoaCreate(BaseModel):
    nome: str
    data_resposta: Optional[datetime] = None
    email: Optional[str] = None

    @validator('nome')
    def nome_deve_ter_tamanho_minimo(cls, nome):
        if len(nome) < 2:
            raise ValueError('O nome deve ter pelo menos 2 caracteres.')
        return nome

class PessoaResponse(BaseModel):
    """
        Para que os campos sejam retornados na resposta, é necessário que eles estejam 
        definidos em RETURNING no crud,  e o parametro da função seja do tipo PessoaResponse: 
        @app.post("/pessoas", response_model=PessoaResponse)
    """
    id: int
    nome: str    
    email: Optional[str] = None

    class Config:
        orm_mode = True