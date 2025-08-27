#create database tables

from lib.database import Base, engine
from lib.models import pet, care_type, care_event


print("Creating tables...")
Base.metadata.create_all(engine)
print("Tables created successfully!")