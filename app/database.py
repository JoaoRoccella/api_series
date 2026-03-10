import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# 1. Garantir que o Banco de Dados (Schema) exista antes de conectar com SQLAlchemy
def __criar_banco_se_nao_existir():
    connection = pymysql.connect(
        host=getenv('DB_HOST'),
        user=getenv('DB_USER'),
        password=getenv('DB_PSWD')
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {getenv('DB_NAME')}")
        connection.commit()
    finally:
        connection.close()

# Executa a criação do banco (Schema)
__criar_banco_se_nao_existir()

# 2. Configuração do SQLAlchemy
DATABASE_URL = f"mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PSWD')}@{getenv('DB_HOST')}/{getenv('DB_NAME')}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 3. Dependência para injetar a sessão do banco nas rotas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()