from fastapi import HTTPException, status
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.serie import SerieModel
from app.schemas.serie import SerieSchema

router = APIRouter(prefix="/series", tags=["Séries"])


@router.post("/")
def criar_serie(dados: SerieSchema, db: Session = Depends(get_db)):
    nova_serie = SerieModel(**dados.model_dump())
    db.add(nova_serie)
    db.commit()
    db.refresh(nova_serie)
    return nova_serie


@router.get("/")
def listar_series(db: Session = Depends(get_db)):
    return db.query(SerieModel).all()


@router.put("/{serie_id}")
def atualizar_serie(serie_id: int, dados: SerieSchema, db: Session = Depends(get_db)):
    # 1. Busca o registro no banco
    serie = db.query(SerieModel).filter(SerieModel.id == serie_id).first()

    # 2. Verifica se a série existe
    if not serie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Série com ID {serie_id} não encontrada.",
        )

    # 3. Atualiza os campos com os novos dados
    serie.titulo = dados.titulo
    serie.descricao = dados.descricao
    serie.ano_lancamento = dados.ano_lancamento

    # 4. Salva as alterações
    db.commit()
    db.refresh(serie)

    return serie


@router.delete("/{serie_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_serie(serie_id: int, db: Session = Depends(get_db)):
    # 1. Busca o registro
    serie = db.query(SerieModel).filter(SerieModel.id == serie_id).first()

    # 2. Verifica existência
    if not serie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Série não encontrada."
        )

    # 3. Remove do banco
    db.delete(serie)
    db.commit()

    # Retornamos None (204 No Content indica sucesso sem corpo de resposta)
    return None
