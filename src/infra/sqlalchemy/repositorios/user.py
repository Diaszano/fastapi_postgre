#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import List
from src.schemas import schemas
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy import update, delete, insert
from src.infra.sqlalchemy.models.models import User
from src.infra.sqlalchemy.config.connection import async_session
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class RepositorioUser():
    
    # CRUD
    # Create
    async def createReturn(self,user:schemas.User) -> User:
        session_user = User(
            name=user.name
        );
        async with async_session() as session:
            session:Session
            
            session.add(session_user);
            await session.commit();
            await session.refresh(session_user);
        return session_user;
    # Create
    async def create(self,user:schemas.User) -> None:
        async with async_session() as session:
            session:Session
            
            stmt = insert(User).values(
                name = user.name
            );
            
            await session.execute(stmt);
            await session.commit();
    # Read
    async def read(self) -> List[User]:
        retorno = None;
        async with async_session() as session:
            session:Session
            
            stmt = select(User);
            
            retorno = await session.execute(stmt);
            retorno = retorno.scalars().fetchall();
        return retorno;
    # Read
    async def readId(self,idUser:int) -> User:
        retorno = None;
        async with async_session() as session:
            session:Session
            
            stmt = select(User).where(
                User.id==idUser    
            );
            
            retorno = await session.execute(stmt);
            retorno = retorno.scalars().one();
        return retorno;
    # Read
    async def readName(self,name:str) -> List[User]:
        retorno = None;
        async with async_session() as session:
            session:Session
            
            stmt = select(User).where(
                User.name==name  
            );
            
            retorno = await session.execute(stmt);
            retorno = retorno.scalars().one();
        return retorno;
    # Update
    async def update(self,idUser:int,user:schemas.User) -> None:
        async with async_session() as session:
            session:Session
            
            stmt = update(User).where(
                User.id==idUser
            ).values(
                name=user.name
            );
            
            await session.execute(stmt);
            await session.commit();
    
    # Delete
    async def delete(self,idUser:int) -> None:
        async with async_session() as session:
            session:Session
            
            stmt = delete(User).where(
                User.id==idUser
            );
            
            await session.execute(stmt);
            await session.commit();
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------
#-----------------------