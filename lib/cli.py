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
    welcome_message,
    exit_message,
)

app = typer.Typer(help="🐾 Pet Care Tracker CLI")


@app.command()
def welcome():
    """Show welcome message."""
    welcome_message()

# Pets
@app.command()
def create_pet(name: str, species: str, breed: str = "", age: int = 0):
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

# Care Types
@app.command()
def create_care_type(name: str):
    """Add a new care type."""
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

# Care Events
@app.command()
def create_event(pet_id: int, care_type_id: int, description: str):
    """Add a care event."""
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

# Pet History
@app.command()
def show_history(pet_id: int):
    """Show care history for a single pet by pet_id."""
    list_pet_history(pet_id)

# Exit
@app.command()
def exit():
    """Exit the application."""
    exit_message()


def menu():
    print("\n=== Pet Care Tracker Menu ===")
    print("1. Add Pet")
    print("2. List Pets")
    print("3. Update Pet")
    print("4. Delete Pet")
    print("5. Add Care Type")
    print("6. List Care Types")
    print("7. Update Care Type")
    print("8. Delete Care Type")
    print("9. Add Care Event")
    print("10. List Care Events")
    print("11. Update Care Event")
    print("12. Delete Care Event")
    print("13. Show Pet History")
    print("0. Exit")
    return input("Enter choice: ")

@app.command()
def run():
    """Run interactive menu with numbers instead of typing commands."""
    welcome_message()
    while True:
        choice = menu()
        if choice == "1":
            name = input("Name: ")
            species = input("Species: ")
            breed = input("Breed (optional): ")
            age = int(input("Age: "))
            add_pet(name, species, breed, age)
        elif choice == "2":
            list_pets()
        elif choice == "3":
            pet_id = int(input("Pet ID: "))
            name = input("New name (or leave blank): ") or None
            species = input("New species (or leave blank): ") or None
            breed = input("New breed (or leave blank): ") or None
            age_input = input("New age (or leave blank): ")
            age = int(age_input) if age_input else None
            edit_pet(pet_id, name, species, breed, age)
        elif choice == "4":
            pet_id = int(input("Pet ID to delete: "))
            delete_pet(pet_id)
        elif choice == "5":
            name = input("Care type name: ")
            add_care_type(name)
        elif choice == "6":
            list_care_types()
        elif choice == "7":
            ct_id = int(input("Care Type ID: "))
            name = input("New name: ")
            edit_care_type(ct_id, name)
        elif choice == "8":
            ct_id = int(input("Care Type ID to delete: "))
            delete_care_type(ct_id)
        elif choice == "9":
            pet_id = int(input("Pet ID: "))
            ct_id = int(input("Care Type ID: "))
            desc = input("Description: ")
            add_care_event(pet_id, ct_id, desc)
        elif choice == "10":
            list_care_events()
        elif choice == "11":
            event_id = int(input("Event ID: "))
            pet_input = input("New Pet ID (or leave blank): ")
            pet_id = int(pet_input) if pet_input else None
            ct_input = input("New Care Type ID (or leave blank): ")
            ct_id = int(ct_input) if ct_input else None
            desc = input("New description (or leave blank): ") or None
            edit_care_event(event_id, pet_id, ct_id, desc)
        elif choice == "12":
            event_id = int(input("Event ID to delete: "))
            delete_care_event(event_id)
        elif choice == "13":
            pet_id = int(input("Pet ID: "))
            list_pet_history(pet_id)
        elif choice == "0":
            exit_message()
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    app()
