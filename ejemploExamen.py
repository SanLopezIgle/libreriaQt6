import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QMainWindow, QWidget, QTabWidget, QCheckBox, QListView, QPushButton, QComboBox, QFrame, QSlider, QGroupBox
from PyQt6.QtGui import QPixmap

class EjercicioFormulario(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Examen 15-12-2018")
        self.setFixedSize(800, 400)

        cajaV = QVBoxLayout()

        cajaH1 = QHBoxLayout()
        cajaV.addLayout(cajaH1)

        cajaH2 = QHBoxLayout()
        cajaV.addLayout(cajaH2)

        cajaH1V1 = QVBoxLayout()
        cajaH1V1.setAlignment(Qt.AlignmentFlag.AlignTop)
        cajaH1.addLayout(cajaH1V1)
        lblImagenDisco = QLabel()
        lblImagenDisco.setPixmap(QPixmap("disco.png"))
        cajaH1V1.addWidget(lblImagenDisco)
        botonAnimado = QCheckBox("Animado")
        cajaH1V1.addWidget(botonAnimado)
        lswLista = QListView()
        cajaH1.addWidget(lswLista)

        cajaH1V2 = QVBoxLayout()
        cajaH1.addLayout(cajaH1V2)
        botonEngadir = QPushButton("Engadir a pista a reproducir")
        cajaH1V2.addWidget(botonEngadir)
        botonSubir = QPushButton("Subir na lista")
        cajaH1V2.addWidget(botonSubir)
        botonBaixar = QPushButton("Baixar na lista")
        cajaH1V2.addWidget(botonBaixar)

        grid = QGridLayout()
        botonSaltar = QPushButton("Saltar")
        grid.addWidget(botonSaltar)
        comboSaltar = QComboBox()
        comboSaltar.addItems([str(i) for i in range(9)])
        grid.addWidget(comboSaltar, 0, 1, 1, 2)
        cajaH1V2.addLayout(grid)

        botonAbrir = QPushButton("Abrir ficheiro...")
        cajaH1V2.addWidget(botonAbrir)
        botonReproducir = QPushButton("Reproducir ficheiro...")
        cajaH1V2.addWidget(botonReproducir)
        botonGardar = QPushButton("Gardar como...")
        cajaH1V2.addWidget(botonGardar)
        botonEliminar = QPushButton("Eliminar pista")
        cajaH1V2.addWidget(botonEliminar)

        cajaH2 = QHBoxLayout()
        cajaV.addLayout(cajaH2)

        grid2 = QGridLayout()
        cajaH2.addLayout(grid2)

        etiquetaSon = QLabel("Son:")
        etiquetaRitmo = QLabel("Ritmo:")
        etiquetaVolume = QLabel("Volume:")
        etiquetaFormato = QLabel("Formato:")
        etiquetaSalidaAudio = QLabel("Saida de audio:")
        grid2.addWidget(etiquetaSon, 0, 0, 1, 1)
        grid2.addWidget(etiquetaRitmo, 1, 0, 1, 1)
        grid2.addWidget(etiquetaVolume, 2, 0, 1, 1)
        grid2.addWidget(etiquetaFormato, 3, 0, 1, 1)
        grid2.addWidget(etiquetaSalidaAudio, 4, 0, 1, 1)

        comboSon = QComboBox()
        grid2.addWidget(comboSon, 0, 1, 1, 2)
        comboSon.addItems(["Maracas", "Marimba", "Triángulo", "Timbales"])
        sliderRitmo = QSlider(Qt.Orientation.Horizontal)
        grid2.addWidget(sliderRitmo, 1, 1, 1, 2)
        sliderVolume = QSlider(Qt.Orientation.Horizontal)
        grid2.addWidget(sliderVolume, 2, 1, 1, 2)
        comboFormato = QComboBox()
        grid2.addWidget(comboFormato, 3, 1, 1, 2)
        comboFormato.addItems(["mp3", "wav", "wma", "ogg"])
        comboSaida = QComboBox()
        grid2.addWidget(comboSaida, 4, 1, 1, 2)

        cajaH2V2 = QHBoxLayout()
        marco = QGroupBox("Opcións de reproducción")
        marco.setLayout(cajaH2V2)
        cajaH2.addWidget(marco)

        #marco = QFrame()
        #marco.setFrameStyle(QFrame.Shape.Box)
        #marco.setLayout(cajaH2V2)
        #marco.setWindowTitle("Opcións de reproducción")

        cajaOpciones1 = QVBoxLayout()
        cajaH2V2.addLayout(cajaOpciones1)
        cajaOpciones2 = QVBoxLayout()
        cajaH2V2.addLayout(cajaOpciones2)

        botonAsincrono = QCheckBox("Asincrono")
        cajaOpciones1.addWidget(botonAsincrono)
        botonEnome = QCheckBox("E nome de ficheiro")
        cajaOpciones1.addWidget(botonEnome)
        botonXML = QCheckBox("XML persistente")
        cajaOpciones1.addWidget(botonXML)

        botonFiltrar = QCheckBox("Filtrar antes de reproducir")
        cajaOpciones2.addWidget(botonFiltrar)
        botonEXML = QCheckBox("E XML")
        cajaOpciones2.addWidget(botonEXML)
        botonReproduccion = QCheckBox("Reproduccion NPL")
        cajaOpciones2.addWidget(botonReproduccion)

        container = QWidget()
        container.setLayout(cajaV)
        self.setCentralWidget(container)


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = EjercicioFormulario()  # creamos instancia de nuestra primera ventana. Como en JAVA, llamamos a la clase.
    ventana.show()
    aplicacion.exec()