from sqlalchemy import Column, DateTime, Integer, String
from database import Base

"""Representa uma tabela no banco de dados"""

class Pessoa(Base):
    __tablename__ = "pessoas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    data_resposta = Column(DateTime)
    email = Column(String, nullable=True)
