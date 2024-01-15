from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QLabel, QFrame
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QPixmap
from PyQt6 import uic

imgWidth=84
imgHeight=72

class UnitIcon(QtWidgets.QWidget):

    doubleClicked = QtCore.pyqtSignal() #define clicked as a signal
    clicked = QtCore.pyqtSignal() #define double-clicked as a signal

    def __init__(self): 
        super().__init__()

        self.horizontal_padding = 0
        self.vertical_padding = 0

        uic.loadUi("app/client/ui/UnitIcon.ui", self)

        # Adjust the layout properties

        frame = self.findChild(QFrame, 'frame')
        frame.layout().setContentsMargins(0, 0, 0, 0)
        frame.layout().setSpacing(0)

        self.unitIcon = frame.findChild(QLabel, 'unitIcon')
        self.unitName = frame.findChild(QLabel, 'unitName')

        # Adjust the QLabel size policy
        self.unitIcon.setSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        self.unitName.setSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)

        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self._emitClickedSignal)

        self._clickCount = 0

    def setHorizontalPadding(self, padding):
            self.horizontal_padding = padding
            self.adjustMargins()

    def setVerticalPadding(self, padding):
        self.vertical_padding = padding
        self.adjustMargins()

    def adjustMargins(self):
        # Adjust the main frame's margins to include padding
        frame = self.findChild(QFrame, 'frame')
        frame.setContentsMargins(self.horizontal_padding, self.vertical_padding,
                                 self.horizontal_padding, self.vertical_padding)

    def setCustomFixedSize(self, width, height):
        self.setFixedSize(width, height)

    def setIcon(self, imagePath):
            pixmap = QPixmap(imagePath)
            if not pixmap.isNull():
                # Scale the pixmap to fit the label's size while maintaining the aspect ratio
                scaled_pixmap = pixmap.scaled(imgWidth, imgHeight, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
                self.unitIcon.setPixmap(scaled_pixmap)
                # Set the alignment to center the pixmap if it's smaller than the label size
                self.unitIcon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                print('Loaded ' + imagePath)
            else:
                print('ERROR loading ' + imagePath)

    def setName(self, name):
        self.unitName.setText(name)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self._clickCount += 1
            if not self.timer.isActive():
                self.timer.start(250)  # 250 ms for double-click interval
            else:
                if self._clickCount == 2:
                    print('Double-click caught!')
                    #this should spawn a UnitWidget with the details of the unit in it
                    self.doubleClicked.emit()
                    self._clickCount = 0
                    self.timer.stop()
        super().mousePressEvent(event)

    def _emitClickedSignal(self):
        if self._clickCount == 1:
            self.clicked.emit()
        self._clickCount = 0
