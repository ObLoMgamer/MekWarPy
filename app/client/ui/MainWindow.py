# This Python file uses the following encoding: utf-8
import sys,os
from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtCore import QTimer, Qt
from PyQt6 import uic
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.core.Utils import *
from app.client.ui.UnitIcon import *
from app.core.Player import *
from app.core.Unit import *
from app.client.ui.FlowContainer import *

unit_image_associations_file = 'data/images/units/mechset.txt'
units_path = 'data/mechfiles'

class MainWindow(QtWidgets.QMainWindow):

    # def __init__(self):
    #     super(MainWindow, self).__init__()

    #     uic.loadUi("app/client/ui/mainwindow.ui", self)
    #     self.setWindowTitle("MekWarPy")
    #     player = Player('testPlayer')
    #     player.setHangar(testHangar)
    #     self.player = player

    #     self.drawHangar()

    def __init__(self, player):
        super(MainWindow, self).__init__()

        uic.loadUi("app/client/ui/mainwindow.ui", self)
        self.setWindowTitle("MekWarPy")
        self.player = player

        self.drawHangar()
        self.drawRoster()

    def drawHangar(self):

        self.hangarTab = self.findChild(QtWidgets.QWidget, "hangarTab")
        print(f"HangarTab found: {self.hangarTab is not None}")  # Should print True
        self.hangarFlowContainer = FlowContainer()

        # Create a new QVBoxLayout for hangarTab and add hangarFlowContainer to it
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.hangarFlowContainer)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        # layout.addStretch() #this was causing only a part of the screen to be covered by the FlowContainer

        # Set the layout for hangarTab
        self.hangarTab.setLayout(layout)

        # Make hangarFlowContainer expand to fill available space
        self.hangarFlowContainer.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding
        )

        unitTypes = ['Mechs', 'Vehicles', 'Infantry']

        for unitType in unitTypes:

            for unit in self.player.hangar[unitType]:
                veeWidget = UnitIcon()
                veeWidget.setIcon(unit.icon)
                veeWidget.setName(unit.name)

                veeWidget.setHorizontalPadding(2)  # Set horizontal padding
                veeWidget.setVerticalPadding(5)    # Set vertical padding

                self.hangarFlowContainer.addUnitIcon(veeWidget)

    def drawRoster(self): #render the roster tab

        self.mwTab = self.findChild(QtWidgets.QWidget, "mwTab")
        self.pilotTab = self.findChild(QtWidgets.QWidget, "pilotTab")

        print(f"mwTab found: {self.mwTab is not None}")  # Should print True
        print(f"pilotTab found: {self.pilotTab is not None}")  # Should print True

        rosterTabs = {'MechWarriors': self.mwTab, 'Pilots': self.pilotTab}

        rosterTypes = ['MechWarriors','Pilots']
        #first output all mechwarriors

        for pilotType in rosterTypes:

            flowContainer = FlowContainer()

            # Create a new QVBoxLayout for hangarTab and add hangarFlowContainer to it
            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(flowContainer)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)

            rosterTabs[pilotType].setLayout(layout)

            flowContainer.setSizePolicy(
                QtWidgets.QSizePolicy.Policy.Expanding,
                QtWidgets.QSizePolicy.Policy.Expanding
            )

            for pilot in self.player.roster[pilotType]:
                pilotWidget = UnitIcon()
                pilotWidget.setIcon(pilot.icon)
                pilotWidget.setName(pilot.name)

                pilotWidget.setHorizontalPadding(2)  # Set horizontal padding
                pilotWidget.setVerticalPadding(5)    # Set vertical padding

                pilotWidget.setCustomFixedSize(100,250)

                flowContainer.addUnitIcon(pilotWidget)

        # self.mwTab = rosterTabs['MechWarriors']
        # self.pilotTab = rosterTabs['Pilots']

        #now output all pilots

