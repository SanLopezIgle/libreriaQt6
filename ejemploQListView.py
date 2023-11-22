import sys
import typing

from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout,
                            QWidget, QListView, QHBoxLayout, QLineEdit)
from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtGui import QImage

tickImage = QImage('cheque.png')

class TareasModelo(QAbstractListModel):

   def __init__(self, tareas=None):
       super().__init__()
       self.tareas = tareas or []

   def data(self, indice, rol):

       if (rol == Qt.ItemDataRole.DisplayRole):
           _, texto = self.tareas[indice.row()]
           return texto

       if (rol ==Qt.ItemDataRole.DecorationRole):
           estado,_ = self.tareas[indice.row()]
           if estado:
               return tickImage

   def rowCount(self, indice):
       return len(self.tareas)

class VentanaPrincipal(QMainWindow):
   def __init__(self):
       super().__init__()

       self.setWindowTitle("Ejemplo QListView con Qt")

       listaTareas = [(False, 'Primera tarea'), (False, 'Segunda tarea')]

       self.modelo = TareasModelo(listaTareas)

       cajaV = QVBoxLayout()

       self.lstTareas = QListView()
       self.lstTareas.setModel(self.modelo)
       self.lstTareas.setSelectionMode(QListView.SelectionMode.MultiSelection)
       cajaV.addWidget(self.lstTareas)


       cajaH = QHBoxLayout()
       btnBorrar = QPushButton("Borrar")
       btnBorrar.pressed.connect(self.on_btnBorrar_pressed)
       btnHecho = QPushButton("Hecho")
       btnHecho.pressed.connect(self.on_btnHecho_pressed)
       cajaH.addWidget(btnBorrar)
       cajaH.addWidget(btnHecho)

       cajaV.addLayout(cajaH)

       self.txtTarea = QLineEdit()
       cajaV.addWidget(self.txtTarea)

       btnAgregarTarea = QPushButton("Añadir Tarea")
       btnAgregarTarea.pressed.connect(self.on_btnAgregarTarea_pressed)
       cajaV.addWidget(btnAgregarTarea)

       container = QWidget()
       container.setLayout(cajaV)
       self.setCentralWidget(container)

       self.setFixedSize(400, 400)
       self.show()


   def on_btnAgregarTarea_pressed(self):
       texto = self.txtTarea.text().strip()
       if texto:
           self.modelo.tareas.append((False, texto))
           self.modelo.layoutChanged.emit()
           self.txtTarea.setText("")


   def on_btnBorrar_pressed(self):
       indices = self.lstTareas.selectedIndexes()
       if indices:
           for indice in sorted(indices, reverse=True):
                del self.modelo.tareas[indice.row()]
           self.modelo.layoutChanged.emit()
           self.lstTareas.clearSelection()


   def on_btnHecho_pressed(self):
       indices = self.lstTareas.selectedIndexes()
       if indices:
           for indice in indices:
               estado,texto = self.modelo.tareas[indice.row()]
               self.modelo.tareas[indice.row()] = (True, texto)
              # self.modelo.tareas[indice.row()] = (True, self.modelo.tareas[indice.row()][1]). Otra forma de escribir las dos lineas de arriba
           self.modelo.dataChanged.emit(indice, indice)
           self.lstTareas.clearSelection()


#DIFERENCIA ENTRE PONER EL METODO () O SIN ()?
if __name__ == "__main__":
   aplicacion = QApplication(sys.argv)
   ventana = VentanaPrincipal()
   aplicacion.exec()