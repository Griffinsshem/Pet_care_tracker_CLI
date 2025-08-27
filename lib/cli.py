#Typer CLI(user commands)

import typer
from lib.helpers import (
    add_pet,
    list_pets,
    edit_pet,
    delete_pet,
    add_care_type,
    list_care_types,
    edit_care_type,
    delete_care_type,
    add_care_event,
    list_care_events,
    edit_care_event,
    delete_care_event,
    list_pet_history,
)

app = typer.Typer(help="Pet Care Tracker CLI")

#Pets

@app.command()
def create_pet(name: str, species: str, breed: str="", age: int = 0):
    """Add a new pet."""
    add_pet(name, species, breed, age)

@app.command()
def show_pets():
    """List all pets."""
    list_pets()

@app.command()
def update_pet(pet_id: int, name: str = None, species: str = None, breed: str = None, age: int = None):
    """Edit an existing pet."""
    edit_pet(pet_id, name, species, breed, age)

@app.command()
def remove_pet(pet_id: int):
    """Delete a pet by id."""
    delete_pet(pet_id)


#care types
@app.command()
def create_care_type(name: str):
    """Add a new care type"""
    add_care_type(name)

@app.command()
def show_care_types():
    """List all care types."""
    list_care_types()

@app.command()
def update_care_type(care_type_id: int, name: str = None):
    """Edit an existing care type."""
    edit_care_type(care_type_id, name)

@app.command()
def remove_care_type(care_type_id: int):
    """Delete a care type by id."""
    delete_care_type(care_type_id)


#care events
@app.command()
def create_event(pet_id: int, care_type_id: int, description: str):
    """Add a care event"""
    add_care_event(pet_id, care_type_id, description)

@app.command()
def show_events():
    """List all care events."""
    list_care_events()

@app.command()
def update_event(event_id: int, pet_id: int = None, care_type_id: int = None, description: str = None):
    """Edit an existing care event."""
    edit_care_event(event_id, pet_id, care_type_id, description)

@app.command()
def remove_event(event_id: int):
    """Delete a care event by id."""
    delete_care_event(event_id)


@app.command()
def show_history(pet_id: int):
    """Show care history for a single pet by pet_id."""
    list_pet_history(pet_id)


if __name__ == "__main__":
    app()