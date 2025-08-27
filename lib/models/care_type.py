from sqlalchemy import Column, Integer, String
from . import Base


class CareType(Base):
    
    __tablename__ = "care_types"

    id = Column(Integer, primary_key=True)
    name = Column(String)


    def __repr__(self):
        return f"<CareType(id={self.id}, name='{self.name}')>"