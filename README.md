# Library (SUBD Project)

Basic front-end and back-end that showcase the useage of SQL queries.

## Requiremenets

- MySQL or MariaDB server
- `pip` to install the dependencies
- `python 3` to run the application

### Installation

- `pip -r requirements.txt` to install any dependencies
- change `connect_db.py.TEMPLATE` to `connect_db.py` and fill your database information (host, user, password)
- `cd App && python main.py` to start a live reload session

## File Structure

```bash
└─ App
   ├── database
   │   └── *.py
   │
   ├── models
   │   └── *.py
   │
   ├── static
   │   ├── css
   │   │
   │   └── js
   │
   ├── templates
   │   │
   │   └── *.html
   │
   └── main.py

```