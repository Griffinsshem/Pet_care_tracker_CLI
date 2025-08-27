import typer
from helpers import add_pet, list_pets, add_care_type, list_care_type, add_care_event, list_care_events

app = typer.Typer()

@app.command()
def create_pet(name: str, species: str, breed: str, age: int):
    """Add a new pet."""
    add_pet(name, species, breed, age)

@app.command()
def show_pets():
    """List all pets."""
    list_pets()

@app.command()
def create_care_type(name: str):
    """Add a new care type."""
    add_care_type(name)

@app.command()
def show_care_types():
    """List all care types."""
    list_care_type()

@app.command()
def create_event(pet_id: int, care_type_id: int, description: str):
    """Add a care event for a pet."""
    add_care_event(pet_id, care_type_id, description)

@app.command()
def show_events():
    """List all care events."""
    list_care_events()

if __name__ == "__main__":
    app()
