import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit
from PyQt6.QtGui import QPixmap

class SegundaVentana(QMainWindow): #QMainWindow proporciona una ventana ppal. a la aplicacion
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi segunda ventana con Qt")

        self.txtSaludo = QLineEdit()
            #QLineEdit widget de PyQt que proporciona un campo de entrada de una sola línea
        self.txtSaludo.returnPressed.connect(self.on_botonSaludo_clicked)
            #returnPressed se emite cuando el usuario presiona la tecla "Enter"
            #connect establece que, cuando se emite la señal returnPressed, se debe llamar a la función self.on_botonSaludo_clicked
        self.lblEtiqueta1 = QLabel("Hola, qué tal?")
            #QLabel widget de PyQt utilizado para mostrar texto o imágenes
        fuente = self.lblEtiqueta1.font()
        fuente.setPointSize(30)
            #cambia tamaño de la fuente actual
        self.lblEtiqueta1.setFont(fuente)
            #le aplica el cambio a lblEtiqueta1
        self.lblEtiqueta1.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
            #setAlignment se utiliza para configurar la alineación
            #self.lblEtiqueta1 estará centrado tanto horizontal como verticalmente en el área disponible del QLabel
        botonSaludo = QPushButton("Saludo")
            #QPushButton es un widget que representa un botón que el usuario puede presionar
        botonSaludo.clicked.connect(self.on_botonSaludo_clicked)
            #Establece una conexión entre la señal clicked del objeto QPushButton llamado botonSaludo y el método self.on_botonSaludo_clicked
            #los botones emiten la señal clicked cuando son presionados

        cajaVertical = QVBoxLayout()
            #QVBoxLayout es un diseño que organiza los widgets de manera vertical en un contenedor
        cajaVertical.addWidget(self.lblEtiqueta1)
        cajaVertical.addWidget(self.txtSaludo)
        cajaVertical.addWidget(botonSaludo)

        container = QWidget()
            #QWidget es un widget básico en PyQt que puede contener otros widgets
        container.setLayout(cajaVertical)
            #Estás diciendo que los widgets que has agregado a cajaVertical deberían organizarse en este contenedor verticalmente
        self.setCentralWidget(container)
            #Establece container como el widget central de tu ventana principal

        self.setFixedSize(400, 400)
            #el tamaño fijo de la ventana principal en 400 píxeles de ancho y 400 píxeles de alto
        self.show()
            #Muestra la ventana principal

    def on_botonSaludo_clicked(self):
        saludo = self.txtSaludo.text()
            #Obtiene el texto ingresado en el campo de texto self.txtSaludo
        self.lblEtiqueta1.setText(saludo)
            #Establece el texto de self.lblEtiqueta1 con el valor de la variable saludo
if __name__ =="__main__":
    aplicacion = QApplication(sys.argv)
    ventana = SegundaVentana()
    aplicacion.exec()