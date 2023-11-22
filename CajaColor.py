import sys

from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import (QWidget, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QMainWindow)
from PyQt6.QtCore import Qt

class CajaColor(QWidget):
    def __init__(self,color):
        super().__init__()
        self.setAutoFillBackground(True)
            #En el método __init__, establece el fondo del widget para que se rellene automáticamente (self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
            #Crea una paleta de colores y configura el color de fondo utilizando la clase QColor y el argumento color proporcionado al constructor
        self.setPalette(paleta)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EJemplo con Box")

        contenedorPrincipal= QHBoxLayout()
            #layout horizontal
        caja2 = QVBoxLayout()
        caja3 = QVBoxLayout()
            # 2 layouts veticales

        caja2.addWidget(CajaColor("red"))
        caja2.addWidget(CajaColor("yellow"))
        caja2.addWidget(CajaColor("blue"))
        contenedorPrincipal.addLayout(caja2)

        contenedorPrincipal.addWidget(CajaColor("green"))

        caja3.addWidget(CajaColor("blue"))
        caja3.addWidget(CajaColor("orange"))
        contenedorPrincipal.addLayout(caja3)

        widgetPrincipal = QWidget()
        widgetPrincipal.setLayout(contenedorPrincipal)
        self.setCentralWidget(widgetPrincipal)


if __name__ == "__main__":
    app =QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
