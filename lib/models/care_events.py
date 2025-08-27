from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base


class CareEvent(Base):
    
    __tablename__ = "care_events"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    pet_id = Column(Integer, ForeignKey("pets.id"))
    care_type_id = Column(Integer, ForeignKey("care_types.id"))


    pet = relationship("Pet", back_populates="care_events")
    care_type = relationship("CareType", back_populates="care_events")


    def __repr__(self):
        return f"<CareEvent(pet_id={self.pet_id}, care_type_id={self.care_type_id})>"