"""
   Schema: estrutura de dados para entrada e saída da API
     1-) Define como os dados vão chegar (input) e como vão sair (output)
     2-) Podemos incluir regras de validações
     3-) Podemos ter campos que estão na tabela mas não queremos que sejam retornados         
"""

from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional

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
    pessoa_id: int
    nome: str    
    email: Optional[str] = None

    class Config:
        orm_mode = True