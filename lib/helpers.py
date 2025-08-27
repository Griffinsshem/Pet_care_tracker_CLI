# lib/helpers.py
#helper functions used in CLI

from lib.database import Session
from lib.models.pet import Pet
from lib.models.care_type import CareType
from lib.models.care_events import CareEvent

#pet helpers

def add_pet(name: str, species: str, breed: str, age: int):
    """Add a new pet to the database."""
    session = Session()
    pet = Pet(name=name, species=species, breed=breed, age=age)
    session.add(pet)
    session.commit()
    print(f"Pet '{name}' added!")
    session.close()

def list_pets():
    """List all pets in the database."""
    session = Session()
    pets = session.query(Pet).all()
    if not pets:
        print("No pets found.")
    else:
        for p in pets:
            print(f"{p.id}. {p.name} - {p.species} / {p.breed} (age {p.age})")
    session.close()


#care type helpers

def add_care_type(name: str):
    """Add a new care type."""
    session = Session()
    ct = CareType(name=name)
    session.add(ct)
    session.commit()
    print(f"Care type '{name}' added!")
    session.close()

def list_care_types():
    """Show all available care types."""
    session = Session()
    types = session.query(CareType).all()
    if not types:
        print("No care types found.")
    else:
        for t in types:
            print(f"{t.id}. {t.name}")
    session.close()


#care event helpers

def add_care_event(pet_id: int, care_type_id: int, description: str):
    """Log a new care event"""
    session = Session()
    pet = session.get(Pet, pet_id)
    if not pet:
        print(f"No pet with id={pet_id}")
        session.close()
        return
    
    ctype = session.get(CareType, care_type_id)
    if not ctype:
        print(f"No care type with id={care_type_id}")
        session.close()
        return
    

    event = CareEvent(pet_id=pet_id, care_type_id=care_type_id, description=description)
    session.add(event)
    session.commit()
    print(f"Event added for {pet.name}: {ctype.name} - {description}")


def list_care_events():
    """Show all care events with their pet and care type."""
    session = Session()
    events = session.query(CareEvent).all()
    if not events:
        print("No care events found.")
    else:
        for e in events:
            pet_name = e.pet.name if e.pet else f"pet#{e.pet_id}"
            ct_name = e.care_type.name if e.care_type else f"type#{e.care_type_id}"
            print(f"{e.id}. {pet_name} — {ct_name} — {e.description}")
    session.close()


def list_pet_history(pet_id: int):
    """List all events for a single pet"""
    session = Session()
    pet = session.get(Pet, pet_id)
    if not pet:
        print(f"No pet with id={pet_id}")
        session.close()
        return
    
    events = session.query(CareEvent).filter_by(pet_id=pet_id).all()
    print(f"Care history for {pet.name}:")
    if not events:
        print(" (no events yet)")
    else:
        for e in events:
            ct_name = e.care_type.name if e.care_type else f"type#{e.care_type_id}"
            print(f"  - {ct_name}: {e.description} (event id={e.id})")

    session.close()


