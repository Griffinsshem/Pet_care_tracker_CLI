#insert starter data

from lib.database import Session
from lib.models.pet import Pet
from lib.models.care_type import CareType
from lib.models.care_events import CareEvent

def run_seed():
    
    session = Session()

    # sample pets
    buddy = Pet(name="Buddy", species="Dog", breed="Beagle", age=3)
    whiskers = Pet(name="Whiskers", species="Cat", breed="Siamese", age=2)

    # sample care types
    feeding = CareType(name="Feeding")
    walk = CareType(name="Walk")
    vet = CareType(name="Vet Visit")

    session.add_all([buddy, whiskers, feeding, walk, vet])
    session.commit()

    e1 = CareEvent(pet_id=buddy.id, care_type_id=feeding.id, description="Breakfast kibble at 8:00")
    e2 = CareEvent(pet_id=buddy.id, care_type_id=walk.id, description="Evening walk 20 mins")
    e3 = CareEvent(pet_id=whiskers.id, care_type_id=vet.id, description="Annual check-up")

    session.add_all([e1, e2, e3])
    session.commit()
    session.close()

    print("Database seeded with sample pets, care types, and events!")


if __name__ == "__main__":
    run_seed()

