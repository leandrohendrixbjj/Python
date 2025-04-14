from fastapi import FastAPI, HTTPException
from app.infra.lifespan import lifespan 
from app.models.students_data import students  
from app.routes.index import router as index_router
from app.routes.students import router as students_router
from app.helper.clear import limpar_tela

limpar_tela()

app = FastAPI()
app = FastAPI(lifespan=lifespan)

# Incluindo a rota Welcome
app.include_router(index_router)

# Incluindo as rotas de estudantes
app.include_router(students_router)

