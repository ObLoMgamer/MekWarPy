import sys
from PyQt6 import QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("app/client/mainwindow.ui")
window.show()
app.exec()
