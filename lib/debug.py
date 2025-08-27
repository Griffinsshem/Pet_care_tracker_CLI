#!/usr/bin/env python3
# lib/debug.py

#create tables

from lib.database import Base, engine
from lib.models import pet, care_type, care_event

if __name__ == "__main__":
    print("Creating tables...")
    Base.metadata.create_all(engine)
    print("Tables created successfully!")