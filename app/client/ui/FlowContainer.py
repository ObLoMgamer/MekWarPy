# This Python file uses the following encoding: utf-8
from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QLabel
from PyQt6.QtGui import QPixmap, QPalette
from PyQt6.QtWidgets import QGridLayout, QListWidget, QListView, QListWidgetItem, QSizePolicy
from PyQt6.QtCore import QTimer, Qt

from app.client.ui.UnitIcon import *

class FlowContainer(QListWidget):
    def __init__(self):
        super().__init__()
        # make it look like a normal scroll area
        self.viewport().setBackgroundRole(QPalette.ColorRole.Window)
        # display items from left to right, instead of top to bottom
        self.setFlow(QtWidgets.QListView.Flow.LeftToRight)
        # wrap items that don't fit the width of the viewport
        # similar to self.setViewMode(self.IconMode)
        self.setWrapping(True)
        # prevent user repositioning
        self.setMovement(self.Movement.Static)
        # always re-layout items when the view is resized
        self.setResizeMode(self.ResizeMode.Adjust)

        self.setHorizontalScrollMode(self.ScrollMode.ScrollPerPixel)
        self.setVerticalScrollMode(self.ScrollMode.ScrollPerPixel)
        self.setSpacing(45)

    def addUnitIcon(self, uniticon): #we expect a uniticon to be passed as parameter
        item = QListWidgetItem('')
        item.setFlags(item.flags() & ~(Qt.ItemFlag.ItemIsSelectable|Qt.ItemFlag.ItemIsEnabled))
        self.addItem(item)
        #item.setSizeHint(uniticon.sizeHint())
        self.setItemWidget(item, uniticon)
