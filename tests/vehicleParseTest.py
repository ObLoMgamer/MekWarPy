import sys
import os

# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.core.Unit import *
import zipfile



archive = zipfile.ZipFile('data/mechfiles/vehicles.zip', 'r')
veefile = '3050U/Fury Command Tank.blk'


loadedVee = Vehicle()
loadedVee.zipload(veefile)

print_instance_attributes(loadedVee)
