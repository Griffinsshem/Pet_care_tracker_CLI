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

def edit_pet(pet_id: int, name: str = None, species: str = None, breed: str = None, age: int = None):
    """Edit an existing pet's details."""
    session = Session()
    pet = session.get(Pet, pet_id)
    if not pet:
        print(f"No pet with id={pet_id}")
        session.close()
        return

    if name: pet.name = name
    if species: pet.species = species
    if breed: pet.breed = breed
    if age is not None: pet.age = age

    session.commit()
    print(f"Pet {pet_id} updated successfully!")
    session.close()

def delete_pet(pet_id: int):
    """Delete a pet from the database"""
    session = Session()
    pet = session.get(Pet, pet_id)
    if not pet:
        print(f"No pet with id={pet_id}")
    else:
        session.delete(pet)
        session.commit()
        print(f"Pet {pet_id} deleted")
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

def edit_care_type(care_type_id: int, name: str):
    """Edit an existing care type."""
    session = Session()
    ct = session.get(CareType, care_type_id)
    if not ct:
        print(f"No care type with id={care_type_id}")
    else:
        ct.name = name
        session.commit()
        print(f"Care type {care_type_id} updated to '{name}'!")
    session.close()

def delete_care_type(care_type_id: int):
    """Delete a care type."""
    session = Session()
    ct = session.get(CareType, care_type_id)
    if not ct:
        print(f"No care type with id={care_type_id}")
    else:
        session.delete(ct)
        session.commit()
        print(f"Care type {care_type_id} deleted.")
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

def edit_care_event(event_id: int, description: str = None, care_type_id: int = None):
    """Edit an existing care event."""
    session = Session()
    event = session.get(CareEvent, event_id)
    if not event:
        print(f"No event with id={event_id}")
        session.close()
        return
    
    if description: event.description = description
    if care_type_id: event.care_type_id = care_type_id

    session.commit()
    print(f"Care event {event_id} updated.")
    session.close()

def delete_care_event(event_id: int):
    """Delete a care event."""
    session = Session()
    event = session.get(CareEvent, event_id)
    if not event:
        print(f"No event with id={event_id}")
    else:
        session.delete(event)
        session.commit()
        print(f"Care event {event_id} deleted.")
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


def welcome_message():
    """Display a welcome message for the CLI app."""
    print("🐾 Welcome to the Pet Care Tracker CLI! 🐾")

def exit_message():
    """Display a goodbye message when exiting the CLI app."""
    print("Goodbye! 👋Thanks for using the Pet Care Tracker.")
