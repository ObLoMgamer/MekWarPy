import sqlite4
# This Python file uses the following encoding: utf-8

# the dbInit script creates and/or updates the database which holds basic unit data (unit name, image path, and data path)
# more unit data is not stored in the database in order to retain compatibility with MegaMek via .mtf and .blk files


file_path = 'data/images/units/mechset.txt'
db_path = 'data/data.db'
units_path = 'data/mechfiles'

def setWeaponsTables():
    weaponsTable = {}



def store_unit_paths(unit_image_map):
    """
    Store the parsed data in an SQLite database.

    Parameters:
    db_path (str): The path to the SQLite database file.
    unit_image_map (dict): The dictionary containing unit names and their image paths.
    """

    # Connect to the SQLite database
    conn = sqlite4.connect(db_path)
    cursor = conn.cursor()

    # Create table for unit paths
    cursor.execute('''CREATE TABLE IF NOT EXISTS battletech_unit_paths
                      (unit_name TEXT PRIMARY KEY, image_path TEXT, data_path TEXT)''')

    # Insert data into the unit paths table
    for unit_name, image_path in unit_image_map.items():
        cursor.execute('''INSERT OR REPLACE INTO battletech_unit_paths (unit_name, image_path)
                          VALUES (?, ?)''', (unit_name, image_path))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Example usage:
# db_path = 'path_to_your_database.db'  # Replace with your actual database file path
# data = comprehensive_parsed_data  # This is the dictionary obtained from parsing the file
# store_in_sqlite(db_path, data)


def parse_battletech_file(file_path):
    """
    Parse the entire file comprehensively, ensuring that all relevant lines are processed.
    """
    unit_image_map = {}

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            line = line.strip()
            if line.startswith('chasis') or line.startswith('exact'):
                # Splitting the line into components and stripping potential extra spaces
                parts = [part.strip() for part in line.split('"') if part.strip()]
                if len(parts) == 3:
                    # Extract unit name and image path
                    unit_name, image_path = parts[1], parts[2].strip()
                    unit_image_map[unit_name] = image_path

    return unit_image_map

# Testing the function with the provided file
unit_image_map = parse_battletech_file(file_path)
# print(unit_image_map)


#parse zip files and list all relevant unit files (mechs, vehicles, infantry)
#parse image associations for these files
#create a dictionary that holds all three pieces of information
#store associations in database table
