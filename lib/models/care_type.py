from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base


class CareType(Base):
    
    __tablename__ = "care_types"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    care_event = relationship("CareEvent", back_populates="care_type")

    def __repr__(self):
        return f"<CareType(name={self.name})>"