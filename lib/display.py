# lib/display.py - Pretty print tables using Tabulate

from tabulate import tabulate
from lib.database import Session
from lib.models.pet import Pet
from lib.models.care_type import CareType
from lib.models.care_events import CareEvent


def show_pets():
    session = Session()
    pets = session.query(Pet).all()
    table = [[p.id, p.name, p.species, p.breed, p.age] for p in pets]
    print(tabulate(table, headers=["ID", "Name", "Species", "Breed", "Age"], tablefmt="fancy_grid"))
    session.close()


def show_care_types():
    session = Session()
    care_types = session.query(CareType).all()
    table = [[ct.id, ct.name] for ct in care_types]
    print(tabulate(table, headers=["ID", "Care Type"], tablefmt="fancy_grid"))
    session.close()


def show_care_events():
    session = Session()
    events = session.query(CareEvent).all()
    table = [[e.id, e.pet.name, e.care_type.name, e.description] for e in events]
    print(tabulate(table, headers=["ID", "Pet", "Care Type", "Description"], tablefmt="fancy_grid"))
    session.close()


if __name__ == "__main__":
    print("\n Pets Table:")
    show_pets()

    print("\n Care Types Table:")
    show_care_types()

    print("\n Care Events Table:")
    show_care_events()
