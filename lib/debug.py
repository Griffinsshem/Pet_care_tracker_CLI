#create database tables

from lib.database import Base, engine
from lib.models.pet import Pet
from lib.models.care_type import CareType
from lib.models.care_events import CareEvent


if __name__ == "__main__":
    print("Creating tables...")
    Base.metadata.create_all(engine)
    print("Tables created successfully!")