#-----------------------
# BIBLIOTECAS
#-----------------------
from pydantic import BaseModel
from typing import Optional, List
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class FavoriteSimples(BaseModel):
    symbol:str;

class User(BaseModel):
    id       : Optional[int] = None;
    name     : str;
    favorites: Optional[List[FavoriteSimples]] = None;

class Favorite(BaseModel):
    id     : Optional[int] = None;
    symbol : str;
    user_id: Optional[int] = None;
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------
#-----------------------