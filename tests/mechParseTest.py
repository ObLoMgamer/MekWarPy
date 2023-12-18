import sys
import os

# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.core.Unit import *
import zipfile

mechfile = '3039u/Highlander HGN-733.mtf'

loadedMech = Mech()
loadedMech.zipload(mechfile)

print_instance_attributes(loadedMech)
