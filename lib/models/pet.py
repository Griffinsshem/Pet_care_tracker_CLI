from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base


class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    species = Column(String)
    breed = Column(String)
    age = Column(Integer)


    #relationship: a pet can have many events
    care_events =relationship("CareEvent", back_populates="pet")

    def __repr__(self):
        return f"<Pet(name={self.name}, species={self.species})>"