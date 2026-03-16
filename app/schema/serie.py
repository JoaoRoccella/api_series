from pydantic import BaseModel
from typing import Optional

class SerieSchema(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    ano_lancamento: int

    class Config:
        from_attributes = True

class SerieUpdateSchema(BaseModel):
    titulo: Optional[str]
    descricao: Optional[str]
    ano_lancamento: Optional[int]

    class Config:
        from_attributes = True