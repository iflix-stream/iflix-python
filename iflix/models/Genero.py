from sqlalchemy import Column,ForeignKey
from sqlalchemy.dialects.mysql import TINYINT,VARCHAR,TEXT,INTEGER
from base import Base

class Genero(Base):

    __tablename__ = "genero"

    id = Column(INTEGER, primary_key=True)
    nome = Column(VARCHAR(255), nullable=False)
    statusGenero = Column(INTEGER(11), nullable=False,default=1)

