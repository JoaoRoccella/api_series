from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.serie import SerieModel
from app.schema.serie import SerieSchema

serie = APIRouter()


@serie.post("/")
async def criar_serie(dados: SerieSchema, db: Session = Depends(get_db)):
    nova_serie = SerieModel(**dados.model_dump())
    db.add(nova_serie)
    db.commit()
    db.refresh(nova_serie)
    return nova_serie


@serie.get("/series")
async def listar_series(db: Session = Depends(get_db)):
    return db.query(SerieModel).all()


# Tarefa 1: Resolva todos os erros da sua aplicação
# Tarefa 2: Crie as novas rotas de atualização e deleção da API
# Tarefa 3: Resolva todos os erros das novas rotas
# Versione

# Extra: resolva o erro de importação das variáveis de ambiente detectado no módulo python-dotenv e utilize corretamente a importação com a função load_dotenv() em seu database.py


@serie.put("/serie/{id}/update")
def atualizar_serie(id: int, dados: SerieSchema, db: Session = Depends(get_db)):
    
    # 1. Busca o registro no banco
    serie = db.query(SerieModel).filter(SerieModel.id == id).first()

    # 2. Verifica se a série existe
    if not serie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Série com ID {id} não encontrada.",
        )
    
    # 3. Atualiza os campos com os novos dados
    for campo, valor in dados.model_dump().items():
        setattr(serie, campo, valor)
        
    # serie.titulo = dados.titulo
    # serie.descricao = dados.descricao
    # serie.ano_lancamento = dados.ano_lancamento

    # 4. Salva as alterações
    db.commit()
    db.refresh(serie)

    return serie


@serie.delete("/serie/{id}/delete")
async def apagar_serie(id: int, db: Session = Depends(get_db)):

    serie = db.query(SerieModel).filter(SerieModel.id == id).first()

    if not serie:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"A série com ID {id} não foi encontrada."
        )
    
    db.delete(serie)

    db.commit()
    
    return {
        "mensagem": f"Serie com ID {id} apagada com sucesso",
        "series": db.query(SerieModel).all()
        }