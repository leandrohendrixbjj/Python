from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship 

Base = declarative_base()

class NotaFiscal(Base):
    __tablename__ = "nota_fiscal"

    nota_fiscal_id = Column(Integer, primary_key=True, index=True)
    numero = Column(String(50), nullable=False)
    data_emissao = Column(TIMESTAMP(timezone=True), server_default=func.now())
    total = Column(Numeric(12, 2), nullable=False)
    pessoa = relationship("Pessoa", back_populates="notas")
