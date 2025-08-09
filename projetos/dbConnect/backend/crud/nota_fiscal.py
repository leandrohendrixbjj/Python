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

        logging.info(f"Registrando nota fiscal: {nota.numero}, Total: {nota.total}, Data Emissão: {data_emissao}")
        print(f"Registrando nota fiscal: {nota.numero}, Total: {nota.total}, Data Emissão: {data_emissao}")

        query = """
        INSERT INTO nota_fiscal (numero, data_emissao, total)
        VALUES ($1, $2, $3)
        RETURNING nota_fiscal_id, numero, data_emissao, total
        """
        values = (nota.numero, data_emissao, nota.total)

        nova_nota = await db_connection.fetchrow(query, *values)

        return dict(nova_nota) if nova_nota else None

    except Exception as e:
        logging.error(f"Erro ao criar nota fiscal: {e}")
        raise HTTPException(status_code=500, detail="Erro interno ao criar nota fiscal.")

    finally:
        if 'db_connection' in locals() and db_connection:
            await db_connection.close()
