#Typer CLI(user commands)

import typer
from lib.helpers import (
    add_pet,
    list_pets,
    add_care_type,
    list_care_types,
    add_care_event,
    list_care_events,
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


#care types
@app.command()
def create_care_type(name: str):
    """Add a new care type"""
    add_care_type(name)

@app.command()
def show_care_types():
    """List all care types."""
    list_care_types()

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
def show_history(pet_id: int):
    """Show care history for a single pet by pet_id."""
    list_pet_history(pet_id)


if __name__ == "__main__":
    app()