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
# Favorite
class Favorite(BaseModel):
    symbol:str;
    
    class Config:
        orm_mode = True;

class FavoriteInsert(Favorite):
    user_id:Optional[int] = None;

class FavoriteComplete(FavoriteInsert):
    id:Optional[int] = None;

# User
class UserInsert(BaseModel):
    name:str;
    
    class Config:
        orm_mode = True;

class User(UserInsert):
    id:Optional[int] = None;    

class UserComplete(User):
    favorites:Optional[List[Favorite]] = None;

# Response
class Response(BaseModel):
    message:str
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------
#-----------------------