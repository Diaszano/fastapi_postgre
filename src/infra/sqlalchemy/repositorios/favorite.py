#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import List
from src.schemas import schemas
from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete, insert
from src.infra.sqlalchemy.models.models import Favorite
from src.infra.sqlalchemy.config.connection import async_session
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class RepositorioFavorite():
    
    # CRUD
    # Create
    async def createReturn(self,favorite:schemas.FavoriteInsert) -> Favorite:
        session_user = Favorite(
            symbol=favorite.symbol,
            user_id=favorite.user_id
        );
        async with async_session() as session:
            session:Session
            
            session.add(session_user);
            await session.commit();
            await session.refresh(session_user);
        return session_user;
    # Create
    async def create(self,favorite:schemas.FavoriteInsert) -> None:
        async with async_session() as session:
            session:Session
            
            stmt = insert(Favorite).values(
                symbol=favorite.symbol,
                user_id=favorite.user_id
            );
            
            await session.execute(stmt);
            await session.commit();
    # Read
    async def read(self) -> List[Favorite]:
        retorno = None;
        async with async_session() as session:
            session:Session
            
            stmt = select(Favorite);
            
            retorno = await session.execute(stmt);
            retorno = retorno.scalars().fetchall();
        return retorno;
    # Read
    async def readId(self,idFavorite:int) -> Favorite:
        retorno = None;
        async with async_session() as session:
            session:Session
            
            stmt = select(Favorite).where(
                Favorite.id==idFavorite   
            );
            
            retorno = await session.execute(stmt);
            retorno = retorno.scalars().fetchall();
        return retorno;
    # Update
    async def update(self,idFavorite:int,favorite:schemas.Favorite) -> None:
        async with async_session() as session:
            session:Session
            
            stmt = update(Favorite).where(
                Favorite.id==idFavorite
            ).values(
                symbol=favorite.symbol,
            );
            
            await session.execute(stmt);
            await session.commit();
    
    # Delete
    async def delete(self,idFavorite:int) -> None:
        async with async_session() as session:
            session:Session
            
            stmt = delete(Favorite).where(
                Favorite.id==idFavorite
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