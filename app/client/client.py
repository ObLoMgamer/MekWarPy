import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt6 import QtWidgets, uic
from app.client.ui.MainWindow import *

testHangar = {'Mechs':    ['Charger CGR-1A1',
                        'Cyclops CP-10-Z',
                        'Longbow LGB-0W',
                        'Victor VTR-9B',
                        'Charger CGR-1A9',
                        'Banshee BNC-3E',
                        'Goliath GOL-1H',
                        'Mauler MAL-1R',
                        'Awesome AWS-8R',
                        'Striker STC-2C',
                        'Thug THG-10E',
                        'Awesome AWS-8V',
                        'BattleMaster BLR-1G',
                        'Hatamoto-Chi HTM-26T'],
            'Vehicles':   ['Partisan Heavy Tank (Standard)',
                        'Schrek AC Carrier (Standard)',
                        'Demolisher Heavy Tank (Standard Mk. I)',
                        'Partisan Heavy Tank (LRM)'],
            'Infantry':[]}
#let's create some test data


def main():

    unit_image_map = parse_unit_image_map_to_dict(unit_image_associations_file)
    app = QtWidgets.QApplication(sys.argv)

    player = Player('testPlayer')
    player.setHangar(testHangar)
    player.generateTestPilots() #generate test pilots to match the types of whatever we've put into the test unit hangar
    window = MainWindow(player)
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
