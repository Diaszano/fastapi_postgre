#-----------------------
# BIBLIOTECAS
#-----------------------
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
#-----------------------
# CONSTANTES
#-----------------------
Base = declarative_base();
#-----------------------
# CLASSES
#-----------------------
class User(Base):
    __tablename__ = "user";
    
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    );
    name      = Column(String);
    favorites = relationship(
        "Favorite",
        backref="user"
    );

class Favorite(Base):
    __tablename__ = "favorite";
    
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    );
    symbol  = Column(String);
    user_id = Column(Integer,ForeignKey('user.id',name="fk_favorite_user"));
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------
#-----------------------