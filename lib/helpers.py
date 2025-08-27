# lib/helpers.py
#helper functions used in CLI

from models import session
from models.pet import Pet
from models.care_type import CareType
from models.care_events import CareEvent

#pet helpers

def add_pet(name, species, breed, age):
    """Create a new pet and save it to the database"""

    new_pet = Pet(name=name, species=species, breed=breed, age=age)
    session.add(new_pet)
    session.commit()
    print(f"Pet '{name}' added!")

def list_pets():
    """Show all pets currently in the database"""

    pets = session.query(Pet).all()
    if pets:
        for pet in pets:
            print(f"{pet.id}. {pet.name} ({pet.species}, {pet.breed}, age {pet.age})")
    else:
        print("No pets found.ADD some first!")


#care type helpers

def add_care_type(name):
    """Create a new care type."""

    new_type = CareType(name=name)
    session.add(new_type)
    session.commit()
    print(f"Care type '{name}' added!")

def list_care_type():
    """Show all available care types."""
    types = session.query(CareType).all()
    if types:
        for t in types:
            print(f"{t.id}. {t.name}")
    else:
        print("No care types found. ADD some first!")


#care event helpers

def add_care_event(pet_id, care_type_id, description):
    """Log a new care event"""
    new_event = CareEvent(pet_id=pet_id, care_type_id=care_type_id, description=description)
    session.add(new_event)
    session.commit()
    print(f"Care event logged for pet #{pet_id}!")


def list_care_events():
    """Show all care events with their pet and care type."""
    events = session.query(CareEvent).all()
    if events:
        for e in events:
            pet_name = e.pet.name if e.pet else "Unknown Pet"
            care_type_name = e.care_type.name if e.care_type else "Unknown CareType"
            print(f"{e.id}. {pet_name} - {care_type_name} - {e.description}")

    else:
        print("No care events logged yet.")


