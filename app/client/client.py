import sys
from PyQt6 import QtWidgets, uic

#let's create some test data

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
                        'Partisan Heavy Tank (LRM)']}

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        uic.loadUi("app/client/mainwindow.ui", self)

        self.setWindowTitle("MekWarPy")

    #     button = QPushButton("Press Me!")
    #     button.setCheckable(True)
    #     button.clicked.connect(self.the_button_was_clicked)
    #     button.clicked.connect(self.the_button_was_toggled)

    #     self.setCentralWidget(button)

    # def the_button_was_clicked(self):
    #     print("Clicked!")

    # def the_button_was_toggled(self, checked):
    #     print("Checked?", checked)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
