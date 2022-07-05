#-----------------------
# BIBLIOTECAS
#-----------------------
from src.schemas import schemas
from fastapi import APIRouter, Depends, status, HTTPException
from src.infra.sqlalchemy.repositorios.user import RepositorioUser
#-----------------------
# CONSTANTES
#-----------------------
router   = APIRouter(prefix="/user");
NOME_TAG = "Auth";
#-----------------------
# CLASSES
#-----------------------
#-----------------------
# FUNÇÕES()
#-----------------------
@router.post(   "/create",
                status_code=status.HTTP_201_CREATED,
                # response_model=schemas.User,
                tags=[NOME_TAG])
async def create_user(user:schemas.User):
    try:
        retorno = await RepositorioUser().createUserRetorno(user=user);
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