#insert starter data

from lib.database import Session
from lib.models.pet import Pet
from lib.models.care_type import CareType
from lib.models.care_events import CareEvent

def run_seed():
    
    session = Session()

    bud