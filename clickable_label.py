from PyQt5 import QtCore, QtGui, QtWidgets


class QClickableLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtWidgets.QLabel.__init__(self, parent)

    def mousePressEvent(self, event):
        self.clicked.emit()
