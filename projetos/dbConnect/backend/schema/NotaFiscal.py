from datetime import datetime
from pydantic import BaseModel, condecimal

class NotaFiscalCreate(BaseModel):
    numero: str
    total: condecimal(max_digits=12, decimal_places=2)

class NotaFiscalCreate(NotaFiscalCreate):
    pass

class NotaFiscalResponse(BaseModel):
    nota_fiscal_id: int
    numero: str
    data_emissao: datetime
    total: condecimal(max_digits=12, decimal_places=2)

    class Config:
        orm_mode = True
