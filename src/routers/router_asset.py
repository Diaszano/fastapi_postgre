#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import List
from asyncio import gather
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
                response_model=List[schemas.AssetReturn],
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
        favorites_symbols = (
            favorite.symbol
            for favorite in user.favorites
        );
        
        tasks = (
            AssetService.day_summary(symbol)
            for symbol in favorites_symbols
        );

        return await gather(*tasks);
    
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{error}"
        );
#-----------------------
# Main()
#-----------------------
#-----------------------