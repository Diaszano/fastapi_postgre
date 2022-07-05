#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import List
from src.schemas import schemas
from fastapi import APIRouter, status, HTTPException
from src.infra.sqlalchemy.repositorios.favorite import RepositorioFavorite 
#-----------------------
# CONSTANTES
#-----------------------
router   = APIRouter(prefix="/favorite");
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
        retorno = await RepositorioFavorite().createReturn(favorite);
        return retorno;
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{error}"
        );

@router.get(   "/list",
                status_code=status.HTTP_200_OK,
                response_model=List[schemas.Favorite],
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
    retorno = await RepositorioFavorite().readId(id);
    if(not retorno):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Usuário com o id '{id}' inexistente"
        )
        
    await RepositorioFavorite ().delete(id);
    return schemas.Response(message="User deletado com sucesso!");
#-----------------------
# Main()
#-----------------------
#-----------------------