from fastapi import FastAPI
from app.database import engine, Base
from app.routes import serie

# Cria as tabelas no banco de dados se elas não existirem
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Séries")

# "Plugando" as rotas de séries no controlador principal
app.include_router(serie.router)

@app.get("/")
def health_check():
    return {"status": "API Online"}