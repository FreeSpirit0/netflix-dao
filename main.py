from utils.db import ShowsDB
import os
from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

nf_shows = ShowsDB(DATABASE_URL)
print(nf_shows.titles().get_all())
print(nf_shows.titles().get("s1").title)

