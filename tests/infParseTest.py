import sys
import os

# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.core.Unit import *
import zipfile

infile = "TW/IS Platoons/Jump Platoon (LRM).blk"

loadedInf = Infantry()
loadedInf.zipload(infile)

print_instance_attributes(loadedInf)