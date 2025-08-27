
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
python -m lib.cli create-pet "name" "species" --breed "bree" --age <num>
```

- List:

```
python -m lib.cli show-pets
```

- Edit:

```
python -m lib.cli update-pet <id> --name "name" --breed "breed" --age <num>
```

- Delete(using pet_id):

```
python -m lib.cli remove-pet <num>
```

#### Care Types

- Create:
