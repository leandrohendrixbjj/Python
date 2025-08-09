from datetime import datetime
from pydantic import BaseModel, condecimal

class NotaFiscalBase(BaseModel):
    numero: str
    total: condecimal(max_digits=12, decimal_places=2)
    pessoa_id: int

class NotaFiscalCreate(NotaFiscalBase):
    pass

class NotaFiscalResponse(BaseModel):
    nota_fiscal_id: int
    numero: str
    data_emissao: datetime
    total: condecimal(max_digits=12, decimal_places=2)
    pessoa_id: int

    class Config:
        orm_mode = True
