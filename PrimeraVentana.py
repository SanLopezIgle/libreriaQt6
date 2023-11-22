import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap

class PrimeraVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("mi primera ventana con qt")

        self.lblEtiqueta1 = QLabel("hola, que tal?")
        lblEtiqueta2 = QLabel()
        lblEtiqueta2.setPixmap(QPixmap("gato.jpg"))
        botonSaludo = QPushButton("saludo")
        botonSaludo.clicked.connect(self.on_botonSaludo_clicked)

        cajaVertical = QVBoxLayout()
        cajaVertical.addWidget(self.lblEtiqueta1)
        cajaVertical.addWidget(lblEtiqueta2)
        cajaVertical.addWidget(botonSaludo)

        container = QWidget()
        container.setLayout(cajaVertical)
        self.setCentralWidget(container)

        self.setFixedSize(400,400)
        self.show()


    def on_botonSaludo_clicked(self):
        self.lblEtiqueta1.setText("hola compañeros")


if __name__ == "__main__":
    aplication = QApplication(sys.argv)
    ventana = PrimeraVentana()
    aplication.exec()