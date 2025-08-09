import logging
from datetime import datetime
from fastapi import HTTPException
from infra.database_connection import connect_to_db
from schema.NotaFiscal import NotaFiscalCreate, NotaFiscalResponse

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

async def criar_nota_fiscal(nota: NotaFiscalCreate):
    try:
        db_connection = await connect_to_db()

        data_emissao = datetime.now()  # Data com timezone se quiser pode ajustar para utcnow()

        if not await pessoa_existe(nota.pessoa_id):
            raise HTTPException(status_code=404, detail="Pessoa não encontrada.")

        logging.info(f"Registrando nota fiscal: {nota.numero}, Total: {nota.total}, Data Emissão: {data_emissao}")
        print(f"Registrando nota fiscal: {nota.numero}, Total: {nota.total}, Data Emissão: {data_emissao}")

        query = """
        INSERT INTO nota_fiscal (numero, data_emissao, total, pessoa_id)
        VALUES ($1, $2, $3, $4)
        RETURNING nota_fiscal_id, numero, data_emissao, total, pessoa_id
        """
        values = (nota.numero, data_emissao, nota.total, nota.pessoa_id)

        nova_nota = await db_connection.fetchrow(query, *values)

        return dict(nova_nota) if nova_nota else None
    
    except HTTPException:        
        raise
    except Exception as e:
        logging.error(f"Erro ao criar nota fiscal: {e}")
        raise HTTPException(status_code=400, detail="Não foi possível criar a nota fiscal.") from e

    finally:
        if 'db_connection' in locals() and db_connection:
            await db_connection.close()

async def pessoa_existe(pessoa_id: int) -> bool:
    db_connection = await connect_to_db()
    try:
        query = "SELECT 1 FROM pessoas WHERE pessoa_id = $1"
        result = await db_connection.fetchrow(query, pessoa_id)
        return bool(result)
    finally:
        await db_connection.close()

