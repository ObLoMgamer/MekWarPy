import sys
import os
import zipfile
import math

mechZip = 'data/mechfiles/mechs.zip'
vehicleZip = 'data/mechfiles/vehicles.zip'
infantryZip = 'data/mechfiles/infantry.zip'

def print_instance_attributes(instance):
    """
    This function iterates through all the attributes of a given class instance
    and prints their names and values.
    """
    for attr in dir(instance):
        # Check to ensure we're not printing built-in attributes/methods
        if not attr.startswith('__') and not callable(getattr(instance, attr)):
            print(f"{attr}: {getattr(instance, attr)}")

class Pilot:

    def __init__(self, name, pilotType):
        self.name = name
        self.type = pilotType
        self.gunnery = 4
        self.piloting = 5
        self.experience = None
        self.skills = [] #pilot skills such as Manoevering Ace, Astech, etc.
        self.matchHistory={}


    def __init__(self):
        self.name = None
        self.gunnery = None
        self.piloting = None
        self.type = None #either vehicle or mech
        self.experience = None
        self.skills = []
        self.matchHistory={}

class Unit: 

    def __init__(self):
        self.name = None
        self.unitType = None
        self.rules_level = None
        self.model=None
        self.mass=None

    def __init__(self, name, unitType):
        self.name = name
        self.unitType = unitType
        self.rules_level = None
        self.model=None
        self.mass=None

class Infantry(Unit):
    
    def __init__(self):
        self.unit_type = None
        self.name = None
        self.model = None
        self.year = None
        self.type = None
        self.motion_type = None
        self.field_guns_equipment = []
        self.source = None
        self.squad_size = None
        self.squadn = None
        self.secondn = None
        self.primary_weapon = None
        self.secondary_weapon = None
        self.antimek_skill = None
        self.armor_kit = None

    def zipload(self, blk_file_path):
        """
        Load an infantry unit from a .blk file within a zip archive.

        :param blk_file_path: Path to the .blk file within the zip archive.
        """
        print("Reading from file:", blk_file_path)

        # Open the zip file and read the .blk file
        with zipfile.ZipFile(infantryZip, 'r') as zip_ref:
            blk_content = zip_ref.read(blk_file_path).decode().split('\n')

        current_tag = None

        # Process each line in the blk file
        for line in blk_content:
            line = line.strip()

            # Skip comments and empty lines
            if line.startswith('#') or not line:
                continue

            # Handling XML-like tags and values
            if line.startswith('<') and '>' in line:  # Tag line
                tag, value = line[1:].split('>', 1)
                if tag.endswith('/'):
                    continue  # Skip self-closing tags
                current_tag = tag if '/' not in tag else None
            else:  # Value line
                # Assign values to attributes based on the current tag
                if current_tag in ['year', 'motion_type', 'squad_size', 'squadn', 'secondn', 'antimek', 'source']:
                    setattr(self, current_tag.lower(), line)
                elif current_tag == 'Name':
                    self.name = line
                elif current_tag == 'Model':
                    self.model = line
                elif current_tag == 'UnitType':
                    self.unit_type = line
                elif current_tag == 'Type':
                    self.type = line
                elif current_tag == 'Primary':
                    self.primary_weapon = line
                elif current_tag == 'Secondary':
                    self.secondary_weapon = line
                elif current_tag == 'armorKit':
                    self.armor_kit = line
                elif current_tag == 'Field Guns Equipment':
                    self.field_guns_equipment.append(line)

class Vehicle(Unit):

    def __init__(self):
        super().__init__("", "Vehicle") #set the name and the unitType
        'Name', 'Model', 'year', 'Type', 'motion_type', 'cruiseMP', 'engine_type', 'tonnage', 'UnitType', 'transporters', 'source'
         # Initialize equipment locations and armor
        self.equipment = {
            'Body Equipment': [],
            'Front Equipment': [],
            'Right Equipment': [],
            'Left Equipment': [],
            'Rear Equipment': [],
            'Turret Equipment': [],
            'Rotor Equipment': []
        }

        self.armor = {
            'Front': 0,
            'Right Side': 0,
            'Left Side': 0,
            'Rear': 0,
            'Turret': 0,
            'Rotor': 0
        }

        self.structure = {
            'Front': 0,
            'Right Side': 0,
            'Left Side': 0,
            'Rear': 0,
            'Turret': 0,
            'Rotor': 0
        }
        self.hasTurret = False
        self.vehicleType=''
        self.unitType='Vehicle'

    def calculate_internal_structure(self):
        """
        Calculate the internal structure points for a vehicle in Battletech, dynamically handling locations.

        :param tonnage: The tonnage of the vehicle.
        :param vehicle_type: The type of the vehicle (e.g., 'Tracked', 'Wheeled', 'Hover', 'VTOL', 'Naval').
        :param has_turret: Boolean indicating whether the vehicle has a turret (applicable for non-VTOL types).
        :return: A dictionary with the internal structure points for each location.
        """
        # Define a basic rule for internal structure points calculation
        print(self.mass)
        total_structure_points = self.mass // 5  # Example rule: tonnage divided by 5
        print(total_structure_points)

        # # Adjust the rule based on vehicle type
        # if self.unitType == 'VTOL':
        #     total_structure_points = self.mass // 10  # Adjusted rule for VTOL
        # elif self.unitType == 'Hover':
        #     total_structure_points = self.mass // 6  # Adjusted rule for Hover Tanks

        # Determine which locations are active based on vehicle type
        # Reset structure points for all locations
        for location in self.structure.keys():
            self.structure[location] = 0
        active_locations = ['Front', 'Right Side', 'Left Side', 'Rear', 'Turret', 'Rotor']
        if self.vehicleType == 'VTOL':
            active_locations.append('Rotor')
        elif self.hasTurret:
            active_locations.append('Turret')

        # Distribute the structure points across active locations
        points_per_location = math.ceil(self.mass // 10)
        # print(points_per_location)
        for location in self.structure.keys():
            if location == 'Turret': 
                if self.hasTurret: #only if we have a turret
                    self.structure[location] = points_per_location
            elif location == 'Rotor':
                if self.vehicleType == 'VTOL': #only if this is a VTOL
                    elf.structure[location] = points_per_location
            else: #otherwise, not a special case
                self.structure[location] = points_per_location


    def zipload(self, blk_file_path):

        print("Reading from file:", blk_file_path)

        # Open the zip file and read the .blk file
        with zipfile.ZipFile(vehicleZip, 'r') as zip_ref:
            blk_content = zip_ref.read(blk_file_path).decode().split('\n')

        current_tag = None
        armor_values=[]

        # Process each line in the blk file
        for line in blk_content:
            line = line.strip()

            # Skip comments and empty lines
            if line.startswith('#') or not line:
                continue

            # Handling XML-like tags and values
            if line.startswith('<') and '>' in line:  # Tag line
                tag, value = line[1:].split('>', 1)
                if tag.endswith('/'):
                    continue  # Skip self-closing tags
                current_tag = tag if '/' not in tag else None
            else:  # Value line
                # Assign values to attributes based on the current tag
                if current_tag in ['year', 'motion_type', 'cruiseMP', 'engine_type', 'transporters', 'source']:
                    setattr(self, current_tag.lower(), line)
                elif current_tag == 'tonnage':
                    self.mass = int(float(line))
                    print("Mass is: "+str(self.mass))
                elif current_tag == 'Name':
                    self.name = line
                elif current_tag == 'Model':
                    self.model = line
                elif current_tag == 'UnitType':
                    self.vehicleType = line
                elif current_tag == 'Type':
                    self.rules_level = line
                elif current_tag == 'armor':
                    # Split armor values and assign them to respective locations
                    armor_values.append(int(line.strip())) #int(x) for x in line.split()]
                elif current_tag in self.equipment:
                    self.equipment[current_tag].append(line)

        # print(armor_values)

        for i, location in enumerate(self.armor.keys()):
            # print(location)
            # print(i)
            if i>len(armor_values)-1:
                break
            if i == 4: #special case, we've hit a turret or rotor
                if self.unitType == 'VTOL': #if VTOL, it's the rotors
                    self.armor['Rotor'] = armor_values[i]
                else: #otherise this is a turret
                    self.armor['Turret'] = armor_values[i]
                    self.hasTurret = True
            else: #not special case, there are just 4 locations, set them in order
                self.armor[location] = armor_values[i]
        self.calculate_internal_structure()

class Mech(Unit):

    def __init__(self):
        super().__init__("", "Mech") #set the name and the unitType
        self.model = ""
        self.config = ""
        self.tech_base = ""
        self.era = ""
        self.source = ""
        self.rules_level = ""
        self.engine = ""
        self.structure = ""
        self.myomer = ""
        self.heat_sinks = ""
        self.walk_mp = 0
        self.jump_mp = 0
        self.armor = ""
        self.armor_distribution = {}
        self.weapons = []
        self.critical_slots = {}

    def __str__(self):
        return f"{self.name} {self.model}"

    def calculate_internal_structure(self):
        # Standard BattleTech rules for internal structure points
        self.internal_structure['Head'] = 3
        self.internal_structure['Center Torso'] = math.ceil(self.mass * 0.1)
        side_torso_points = math.ceil(self.mass * 0.05)
        arm_points = side_torso_points
        leg_points = math.ceil(self.mass * 0.1)
        self.internal_structure['Left Torso'] = side_torso_points
        self.internal_structure['Right Torso'] = side_torso_points
        self.internal_structure['Left Arm'] = arm_points
        self.internal_structure['Right Arm'] = arm_points
        self.internal_structure['Left Leg'] = leg_points
        self.internal_structure['Right Leg'] = leg_points


    def zipload(self, file_path):
        location = None

        print("Reading from file: "+file_path)

        #archive =  
        file = zipfile.ZipFile(mechZip, 'r').read(file_path).decode().split('\n') #we're loading mechs, so we know where this zipped data file lives, let's open it, decode and split into lines

        for line in file:

            line = line.strip()
            #print(line)
            if line.startswith('Version:'):
                continue
            elif line.startswith('Config:'):
                self.config = line.split(':')[1]
            elif line.startswith('TechBase:'):
                self.tech_base = line.split(':')[1]
            elif line.startswith('Era:'):
                self.era = line.split(':')[1]
            elif line.startswith('Source:'):
                self.source = line.split(':')[1]
            elif line.startswith('Rules Level:'):
                self.rules_level = line.split(':')[1]
            elif line.startswith('Mass:'):
                self.mass = int(line.split(':')[1])
            elif line.startswith('Engine:'):
                self.engine = line.split(':')[1]
            elif line.startswith('Structure:'):
                self.structure = line.split(':')[1]
            elif line.startswith('Myomer:'):
                self.myomer = line.split(':')[1]
            elif line.startswith('Heat Sinks:'):
                self.heat_sinks = line.split(':')[1]
            elif line.startswith('Walk MP:'):
                self.walk_mp = int(line.split(':')[1])
            elif line.startswith('Jump MP:'):
                self.jump_mp = int(line.split(':')[1])
            elif line.startswith('Armor:'):
                self.armor = line.split(':')[1]
            elif 'Armor' in line and ':' in line:
                parts = line.split(':')
                self.armor_distribution[parts[0].strip()] = int(parts[1].strip())
            elif 'Weapons:' in line:
                continue
            elif ',' in line:
                self.weapons.append(line)
            elif line.endswith(':'):
                if location:  # Save the previous location's data
                    self.critical_slots[location] = components
                location = line[:-1]  # New location
                components = []
            elif location:
                components.append(line)  # Add component to current location
            elif line:
                if not self.name:
                    self.name = line
                elif not self.model:
                    self.model = line

        if location:  # Save the last location's data
            self.critical_slots[location] = components