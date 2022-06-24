#https://stackoverflow.com/questions/56194201/insert-image-into-qgridlayout-and-draw-on-top-of-image-in-pyqt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Label(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Label, self).__init__(parent)
        self.image = QtGui.QPixmap("D:/MatLab/ImagesSport/Kohei_Uchimura.jpg")
        self.drawing = False
        self.lastPoint = QtCore.QPoint()
        self.setCursor(Qt.CrossCursor)
        self.setMouseTracking(True)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(QtCore.QPoint(), self.image)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drawing = True
            painter = QtGui.QPainter(self.image)
            painter.setPen(QtGui.QPen(QtCore.Qt.red, 2, QtCore.Qt.SolidLine))
            painter.drawEllipse(event.pos(), 5, 5)
            if self.lastPoint:
                painter.setPen(QtGui.QPen(QtCore.Qt.blue, 2, QtCore.Qt.SolidLine))
                painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def sizeHint(self):
        return self.image.size()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Python Center of Mass Program")

        self.label = Label()
        self.textedit = QtWidgets.QTextEdit()

        widget = QtWidgets.QWidget()
        self.setCentralWidget(widget)
        lay = QtWidgets.QHBoxLayout(widget)
        lay.addWidget(self.label, alignment=QtCore.Qt.AlignCenter)
        lay.addWidget(self.textedit)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())