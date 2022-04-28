# netflix-dao
This program is for querying netflix shows and staff of the show.

## Setup

1. Create sqlite database from schema  
```
sqlite3 shows.db < db.sql
```
2. Import the data into database.
```
sqlite3 shows.db
.mode csv
.import data/netflix_titles.csv titles
.import data/netflix_staffs.csv staffs
```
3. Start virtual environment.
```
python3 -m venv venv
source bin/env/activate
```
4. Install requirement.
```
pip install -r requirement.txt
```
## Configuration and Run
1. Create `.env` file in the root directory with the following.
```
DATABASE_URL = "sqlite:///shows.db"
```
2. Run using
```
python3 main.py
```
  
