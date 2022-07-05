#-----------------------
# BIBLIOTECAS
#-----------------------
from asyncio import run
from src.infra.sqlalchemy.models.models import Base
from src.infra.sqlalchemy.config.connection import engine
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
#-----------------------
# FUNÇÕES()
#-----------------------
async def create_database():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all);
        await connection.run_sync(Base.metadata.create_all);

async def delete_database():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all);
if(__name__ == "__main__"):
    run(create_database())
#-----------------------
# Main()
#-----------------------
#-----------------------