#-----------------------
# BIBLIOTECAS
#-----------------------
from src.schemas import schemas
from src.infra.sqlalchemy.models.models import User
from sqlalchemy import select, update, delete, insert
from src.infra.sqlalchemy.config.connection import async_session
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class RepositorioUser():
    
    async def createUserRetorno(self,user:schemas.User) -> User:
        session_user = User(
            name=user.name
        );
        async with async_session() as session:
            session.add(session_user);
            await session.commit();
            await session.refresh(session_user);
        return session_user;
    
    async def createUser(self,user:schemas.User) -> User:
        async with async_session() as session:
            stmt = insert(User).values(
                name = user.name
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