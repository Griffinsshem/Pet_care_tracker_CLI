
# 🐾 Pet Care Tracker CLI

Pet Care Tracker CLI — a command-line tool to help pet owners track pets, care types (feeding, walk, vet, etc.), and care events (logs).
Why it exists: it solves the everyday problem of remembering and recording pet care actions (feeding times, vet visits, medication, grooming). The app stores structured records in a lightweight local SQLite database so you can query history, edit records, and keep reliable logs.

## Table of Contents

 - Project Overview
 - Why This Project(Problem it Solves)
 - Project Structure
 - Requirements
 - Installation & Setup
 - Initialize Database(Create Tables & Seed data)
 - Usage: CLI Commands & Examples
 - Database Schema (Tables & relationships)
 - How it Works - High Level
 - Development Notes & Tips
 - Demo Script
 - License & Credits

 ### Project Overview

 Pet Care Tracker CLI is a modular Python application that uses the SQLAlchemy ORM for persistence and Typer for building a CLI. The application stores data locally in SQLite and provides Create / Read / Update / Delete (CRUD) operations for:

- Pets (name, species, breed, age)

- Care types (feeding, walk, vet visit, etc.)

- Care events (actual logged events that connect a Pet and    CareType with a description)

It is designed for beginners learning Python, OOP, ORMs, and CLI design. The code is intentionally simple and modular so you can trace behavior easily.

### Why this Project?

- Keeps a reliable record of pet care actions so you never forget medication, feeding times, or vet visits.

- Demonstrates core software engineering concepts: database design, ORM usage (SQLAlchemy), CLI design (Typer), and modular code organization.

- Easy to extend with new features (export CSV, reminders,  multi-user support, web UI).

### Project Structure

```
pet_care_tracker/
│── README.md
└── lib/
    ├── database.py        # SQLAlchemy engine, Base, Session
    ├── debug.py           # create tables / debug helper
    ├── seed.py            # insert sample data
    ├── cli.py             # Typer CLI commands
    ├── helpers.py         # CRUD helpers (add/list/edit/delete)
    └── models/
        ├── __init__.py    # exposes Base for other models
        ├── pet.py         # Pet model
        ├── care_type.py   # CareType model
        └── care_event.py  # CareEvent model
```

### Tech Stack

- **Language**: Python 3.10+
- **Database**: SQLite (via SQLAlchemy ORM)
- **Libraries**:
  - SQLAlchemy (ORM for database interaction)
  - Tabulate (for clean CLI tables)
- **Tools**: Git & CLI (Command Line Interface)


### Requirements

- Python 3.8+

- Packages: 
   
   ```sqlalchemy```
   ```typer```

You can install them with ```pip``` or ```pipenv```

### Installation & Setup

1. (Optional but recommended) Create a virtual environment and activate it:

```
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```
pip install sqlalchemy typer
```

### Initialize Database

1. Create the tables (run once, or whenever models change):

```
python -m lib.debug
```

Output:
```
Creating tables...
Tables created successfully!
```

2. (Optional) Seed the database with sample data for demo:

```
python -m lib.seed.py
```

Output:

```
Database seeded with sample pets, care types, and events!
```

A SQLite file (e.g. pet.db) will be created in the project folder after creating tables.

### Usage - CLI Commands & Examples

Run the Typer CLI help to see commands:

```
python -m lib.cli --help
```

#### Pets

- Create:

```
python -m lib.cli create-pet NAME SPECIES [--breed BREED] [--age AGE]

```

- List:

```
python -m lib.cli show-pets
```

- Edit:

```
python -m lib.cli update-pet PET_ID [--name NAME] [--species SPECIES] [--breed BREED] [--age AGE]
```

- Delete(using pet_id):

```
python -m lib.cli remove-pet PET_ID
```

#### Care Types

- Create:

```
python -m lib.cli create-care-type "Care Type Name"
```

- List:

```
python -m lib.cli show-care-types
```

- Edit:

```
python -m lib.cli update-care-type CARE_TYPE_ID --name "New Name"
```

- Delete:

```
python -m lib.cli remove-care-type CARE_TYPE_ID
```

#### Care Events

- Create(use pet_id and care_type_id from ```show-pets```/```show-care-types```):

```
python -m lib.cli create-event PET_ID CARE_TYPE_ID "Description of the event"
```

- List:

```
python -m lib.cli show-events
```

- Edit:

```
python -m lib.cli update-event EVENT_ID [--pet-id NEW_PET_ID] [--care-type-id NEW_CARE_TYPE_ID] [--description "New description"]
```

- Delete:

```
python -m lib.cli remove-event EVENT_ID
```

- Show an individual pet history:

```
python -m lib.cli show-history PET_ID
```

### Database Schema(Tables & Relationships)

#### Tables

- ```pets``` - columns: ```id (pk)```, ```name```,    ```species```, ```breed```, ```age```
- care_types — columns: id (PK), name

- care_events — columns: ```id (PK)```, ```description```, ```pet_id (FK ->  pets.id)```, ```care_type_id (FK -> care_types.id)```

#### Relationships

 - One ```Pet``` → many ```CareEvent```s

 - One ```CareType``` → many ```CareEvent```s

 - Each ```CareEvent``` belongs to one ```Pet``` and one ```CareType```.

 ### How It Works — High Level

- ```lib/database.py``` creates an SQLAlchemy ```engine```, ```Base```, and a ```Session``` factory.

- Model classes in ```lib/models/``` inherit from ```Base```. When you run ```Base.metadata.create_all(engine)``` those model definitions become actual database tables.

- ```lib/helpers.py``` contains small functions that open a ```Session```, perform queries or modifications (add, edit, delete), and close the session.

- ```lib/cli.py``` maps Typer commands to the helper functions. CLI calls translate into DB operations behind the scenes.

- The SQLite file lives locally — no server required.

### Development Notes & Tips

- If you change models, re-run ```python lib/debug.py``` to create/alter tables (or use a migration tool like Alembic for complex migrations).

- When testing multiple seed runs, you may want to clear records or drop-and-create tables inside ```seed.py```.

- Use ```sqlite3 pet.db``` or a GUI DB viewer (like DB Browser for SQLite or a VSCode extension) to inspect tables directly.

- Keep ```helpers.py``` focused on DB logic and ```cli.py``` on user interaction — separation of concerns makes the code easier to maintain.

### License & Credits

This project is licensed under the MIT License.  
Feel free to use, modify, and distribute it under the license terms.

Credits: Built as a teaching exercise for learning Python, OOP, SQLAlchemy, and CLI design.

### 🙋‍♂️ Questions or Suggestions?

I'm always happy to hear feedback, ideas, or questions!

📧 Email: griffinsshem254@gmail.com

💻 GitHub: [griffinsshem](https://github.com/griffinsshem)
