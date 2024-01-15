# This Python file uses the following encoding: utf-8
import json
import random

# # Re-load the JSON file as the code execution state was reset
# with open('data/weapons.json', 'r') as file:
#     weapons_data = json.load(file)

# Function to parse the JSON data into a dictionary
def parse_weapons_json_to_dict(inFile):
    with open(inFile, 'r') as file:
        data = json.load(file)
    # Dictionary to store the parsed data
    weapons_dict = {}

    # Parse and store the data in the dictionary
    for weapon_name, weapon_props in data.items():
        weapons_dict[weapon_name] = {
            'type': weapon_props.get('type', ''),
            'weight': weapon_props.get('Tonnage', 0),
            'criticals': weapon_props.get('NumCrits', 0),
            'min_range': weapon_props.get('RngMin', 0),
            'short_range': weapon_props.get('RngSht', 0),
            'med_range': weapon_props.get('RngMed', 0),
            'long_range': weapon_props.get('RngLng', 0),
            'bv': weapon_props.get('OffBV', 0),
            'cost': weapon_props.get('Cost', 0)
        }

    return weapons_dict

# # Parse the JSON data into a dictionary
# weapons_dict = parse_weapons_json_to_dict(weapons_data)

# # Display a small part of the dictionary to verify
# list(weapons_dict.items())[:3]  # Display first 3 items

def parse_unit_image_map_to_dict(file_path):
    """
    Parse the entire file comprehensively, ensuring that all relevant lines are processed.
    """
    unit_image_map = {}

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            line = line.strip()
            if line.startswith('chassis') or line.startswith('exact'):
                # Splitting the line into components and stripping potential extra spaces
                parts = [part.strip() for part in line.split('"') if part.strip()]
                if len(parts) == 3:
                    # Extract unit name and image path
                    unit_name, image_path = parts[1], parts[2].strip()
                    unit_image_map[unit_name] = image_path

    return unit_image_map

def get_random_name_from_large_file(file_path):
    selected_name = None
    line_number = 0
    with open(file_path, 'r') as file:
        for line in file:
            line_number += 1
            # Randomly replace the selected line
            if random.randint(1, line_number) == line_number:
                selected_name = line.strip().split(',')[0]
    return selected_name.strip()
