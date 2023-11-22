import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, QWidget

from CajaColor import CajaColor #cajaColor es la clase y CajaColor es el metodo

class VentanaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo Grid Layout con Qt")

        red = QGridLayout()
            #Crea un objeto QGridLayout llamado red. Este layout se utilizará para organizar los widgets en una cuadrícula.

        red.addWidget(CajaColor("red"))
        red.addWidget(CajaColor("blue"),0,1,1,2)
        red.addWidget(CajaColor("green"),1,0,2,1)
        red.addWidget(CajaColor("pink"),1,1,1,2)
        red.addWidget(CajaColor("orange"),2,1,1,1)
        red.addWidget(CajaColor("yellow"),2,2,1,1)
            #Los argumentos adicionales en algunos casos (como 0, 1, 1, 2) especifican la posición y el tamaño del widget en la cuadrícula.

        control = QWidget()
        control.setLayout(red)
        self.setCentralWidget(control)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    app.exec()
