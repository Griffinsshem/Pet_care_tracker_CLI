#pets Table

from sqlalchemy import Column, Integer, String
from . import Base


class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    species = Column(String)
    breed = Column(String)
    age = Column(Integer)



    def __repr__(self):
        return f"<Pet(id={self.id}, name={self.name}, species={self.species})>"