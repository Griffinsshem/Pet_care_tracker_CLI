#!/usr/bin/env python3
# lib/debug.py

from models import Base
from lib.database import engine

print("Creating tables...")
Base.metadata.create_all(engine)
print("Tables created successfully!")