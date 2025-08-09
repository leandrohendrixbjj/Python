"""
    Representação da tabela do banco de dados
    1-) Define a estrutura da tabela
    2-) Usado pelo ORM para gerar queries SQL
"""
from sqlalchemy import Column, DateTime, Integer, String
from database import Base


class Pessoa(Base):
    __tablename__ = "pessoas"

    pessoa_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    data_resposta = Column(DateTime)
    email = Column(String, nullable=True)
