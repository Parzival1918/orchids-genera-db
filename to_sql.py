#Save the data to a SQLite database

#Import libraries
import json
import os
import sqlite3

#Import helpers
from helpers import utils

#Create folder to store the sqlite db
path = utils.SAVE_LOC + "/sqlite"
if not os.path.exists(path):
    os.makedirs(path)

#Function to read the json files
def load_json(name: str) -> dict:
    with open(utils.SAVE_LOC + "/json/" + name, "r") as file:
        return json.load(file)
    
#Function to save the data to a SQLite database
def save_sqlite(data: list[dict], name: str):
    #Create connection to database
    conn = sqlite3.connect(path + "/" + name + ".db")
    cursor = conn.cursor()

    #Create table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS orchids (
            name TEXT PRIMARY KEY,
            discovery TEXT,
            description TEXT,
            species TEXT,
            distribution TEXT
        )
        """
    )

    #Insert data
    for row in data:
        cursor.execute(
            """
            INSERT INTO orchids VALUES (
                :name, :discovery, :description, :species, :distribution
            )
            """,
            row
        )

    #Commit changes
    conn.commit()

    #Close connection
    conn.close()

#Read files in json folder
files = os.listdir(utils.SAVE_LOC + "/json")

db_name = "orchids"

for file in files:
    print(f"Loading data from {file}... ", end="")
    data = load_json(file)
    print("Done")

    print(f"Saving data to {db_name}... ", end="")
    save_sqlite(data, db_name)
    print("Done", end="\n\n")