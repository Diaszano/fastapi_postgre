#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import List
from asyncio import gather
from src.schemas import schemas
from fastapi import APIRouter, status, HTTPException
from src.infra.sqlalchemy.repositorios.user import RepositorioUser
from src.infra.sqlalchemy.repositorios.favorite import RepositorioFavorite
#-----------------------
# CONSTANTES
#-----------------------
router   = APIRouter(prefix="/user",tags=["User"],);
#-----------------------
# CLASSES
#-----------------------
#-----------------------
# FUNÇÕES()
#-----------------------
@router.post(   "/create",
                status_code=status.HTTP_201_CREATED,
                response_model=schemas.User,
                tags=["Create"])
async def create_user(user:schemas.UserInsert):
    try:
        retorno = await RepositorioUser().createReturn(user=user);
        return retorno;
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{error}"
        );

@router.get(   "/list",
                status_code=status.HTTP_200_OK,
                response_model=List[schemas.UserComplete],
                tags=["List"])
async def list_user():
    try:
        retorno = await RepositorioUser().read();
        return retorno;
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{error}"
        );

@router.delete(   "/delete/{id}",
                status_code=status.HTTP_200_OK,
                response_model=schemas.Response,
                tags=["Delete"])
async def delete_user(id:int):
    try:
        retorno = await RepositorioUser().readId(id);
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Usuário com o id '{id}' inexistente"
        )
    
    try:
        await RepositorioUser().delete(id);
    except:
        user_favoritesId = (
            favorites.id
            for favorites in retorno.favorites
        );
        tasks = (
            RepositorioFavorite().delete(favoriteId)
            for favoriteId in user_favoritesId
        );
        await gather(*tasks);
        await RepositorioUser().delete(id);  
    return schemas.Response(message="User deletado com sucesso!");
#-----------------------
# Main()
#-----------------------
#-----------------------