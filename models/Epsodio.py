from sqlalchemy import Column,ForeignKey
from sqlalchemy.dialects.mysql import TINYINT,VARCHAR,TEXT,INTEGER
from sqlalchemy.orm import relationship

from base import Base
from Temporada import Temporada
from Serie import Serie
class Epsodio(Base):

    __tablename__ = "epsodio"

    id = Column(INTEGER, primary_key=True)
    nome = Column(VARCHAR(255), nullable=False)
    sinopse = Column(TEXT, nullable=False)
    temporada_id = Column(INTEGER,ForeignKey('temporada.id'),nullable=False)
    duracao = Column(VARCHAR(45), nullable=False)
    caminho = Column(VARCHAR(100), nullable=False)
    serie_id = Column(INTEGER, ForeignKey('serie.id'), nullable=False)
    numero = Column(TINYINT(4), nullable=False,default='1')
    temporada = relationship(Temporada,backref='epsodio_temporada')
    serie = relationship(Serie,backref='epsodio_serie')



