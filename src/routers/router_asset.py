#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import List
from src.schemas import schemas
from src.tools.tools import AssetService
from fastapi import APIRouter, status, HTTPException
from src.infra.sqlalchemy.repositorios.user import RepositorioUser
#-----------------------
# CONSTANTES
#-----------------------
router   = APIRouter(prefix="/asset",tags=["Asset"],);
#-----------------------
# CLASSES
#-----------------------
#-----------------------
# FUNÇÕES()
#-----------------------
@router.get(   "/day_summary/{id_user}",
                status_code=status.HTTP_200_OK,
                # response_model=List[schemas.AssetReturn],
                tags=["List"])
async def day_summary(id_user:int):
    try:
        user = await RepositorioUser().readId(idUser=id_user);
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User com o id '{id_user}' inexistente!"
        );
    try:
        retorno:list = [];
        
        for favorites in user.favorites:
            favorites:schemas.Favorite
            
            symbol = favorites.symbol;
            retorno.append(
                await AssetService.day_summary(symbol)
            );
        return retorno;
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{error}"
        );
#-----------------------
# Main()
#-----------------------
#-----------------------