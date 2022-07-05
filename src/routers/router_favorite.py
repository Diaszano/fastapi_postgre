#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import List
from src.schemas import schemas
from fastapi import APIRouter, status, HTTPException
from src.infra.sqlalchemy.repositorios.user import RepositorioUser
from src.infra.sqlalchemy.repositorios.favorite import RepositorioFavorite 
#-----------------------
# CONSTANTES
#-----------------------
router   = APIRouter(prefix="/favorite",tags=["Favorite"]);
#-----------------------
# CLASSES
#-----------------------
#-----------------------
# FUNÇÕES()
#-----------------------
@router.post(   "/create",
                status_code=status.HTTP_201_CREATED,
                response_model=schemas.Favorite,
                tags=["Create"])
async def create_user(favorite:schemas.FavoriteInsert):
    try:
        await RepositorioUser().readId(favorite.user_id);
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Usuário com o id '{favorite.user_id}' inexistente"
        )
    try:
        retorno = await RepositorioFavorite().createReturn(favorite);
        return retorno;
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{error}"
        );

@router.get(   "/list",
                status_code=status.HTTP_200_OK,
                response_model=List[schemas.FavoriteComplete],
                tags=["List"])
async def list_user():
    try:
        retorno = await RepositorioFavorite().read();
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
        await RepositorioFavorite().readId(id);
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Usuário com o id '{id}' inexistente"
        )
    try:
        await RepositorioFavorite ().delete(id);
        return schemas.Response(message="User deletado com sucesso!");
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{error}"
        );
#-----------------------
# Main()
#-----------------------
#-----------------------