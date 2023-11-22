import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, QWidget, QTabWidget

from CajaColor import CajaColor

class VentanaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo QTabWidget")

        tabs = QTabWidget()
            #La clase QTabWidget proporciona un contenedor de pestañas, donde cada pestaña puede
        #   #contener un conjunto diferente de widgets o información
        tabs.setTabPosition(QTabWidget.TabPosition.South)
            #Establece la posición de las pestañas en la parte inferior.
        tabs.setMovable(True)
            #Permite que las pestañas sean movibles.

        for color in ["red", "green", "blue", "yellow"]:#enumerate es como una tupla pero añade numero a cada elemento
          tabs.addTab(CajaColor(color), color)

          self.setCentralWidget(tabs)
          self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    app.exec()
