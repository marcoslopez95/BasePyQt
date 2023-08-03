import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication,QGroupBox, QHBoxLayout, QVBoxLayout, QWidget, QComboBox, QLineEdit, QPushButton, QSlider, QLabel
from PySide6.QtCore import Qt

class MyWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Aplicación")
        self.setGeometry(100, 100, 400, 200)

        # Crear los elementos de la interfaz
        self.gender_select = QComboBox()
        self.gender_select.addItem("Hombre")
        self.gender_select.addItem("Mujer")
        self.gender_select.setFixedWidth(100)  # Cambiar el ancho del QComboBox
        self.gender_select.currentIndexChanged.connect(self.on_gender_select_changed)

        self.text_input = QtWidgets.QTextEdit()
        self.text_input.setFixedWidth(200)  # Cambiar el ancho del QLineEdit
        self.text_input.setFixedHeight(150)

        self.play_button = QPushButton("Play")
        self.play_button.setFixedWidth(60)  # Cambiar el ancho del QPushButton
        self.play_button.clicked.connect(self.on_play_button_click)

        self.volume_slider1 = QSlider(Qt.Horizontal)
        self.volume_slider1.setFixedWidth(150)  # Cambiar el ancho del QSlider
        self.volume_slider1.valueChanged.connect(self.on_slider2_value_changed)

        self.volume_slider2 = QSlider(Qt.Horizontal)
        self.volume_slider2.setFixedWidth(150)  # Cambiar el ancho del QSlider
        self.volume_slider2.valueChanged.connect(self.on_slider2_value_changed)
        # Crear las etiquetas para las barras de volumen
        self.label1 = QLabel("Volumen 1")
        self.label2 = QLabel("Volumen 2")

        # Configurar el layout horizontal para el primer conjunto de elementos
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.gender_select)

        layoutLabel1 = QVBoxLayout()
        layoutLabel1.addWidget(self.label1)  # Añadir QLabel
        layoutLabel1.addWidget(self.volume_slider1)
        groupBox = QGroupBox()  # Usar QGroupBox para ajustar el tamaño del QVBoxLayout
        groupBox.setLayout(layoutLabel1)
        groupBox.setFixedHeight(70)  # Establecer tamaño fijo para groupBox
        groupBox.setFixedWidth(170)  # Establecer tamaño fijo para groupBox

        layoutLabel2 = QVBoxLayout()
        layoutLabel2.addWidget(self.label2)  # Añadir QLabel
        layoutLabel2.addWidget(self.volume_slider2)
        groupBox2 = QGroupBox()  # Usar QGroupBox para ajustar el tamaño del QVBoxLayout
        groupBox2.setLayout(layoutLabel2)
        groupBox2.setFixedHeight(70)  # Establecer tamaño fijo para groupBox
        groupBox2.setFixedWidth(170)  # Establecer tamaño fijo para groupBox
        top_layout.addWidget(groupBox) 
        top_layout.addWidget(groupBox2) 

        # Configurar el layout horizontal para el segundo conjunto de elementos
        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.text_input)
        bottom_layout.addWidget(self.play_button)
        # Configurar el layout vertical para combinar los dos layouts horizontales
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def on_gender_select_changed(self, index):
        gender = self.gender_select.currentText()
        print("Selected gender:", gender)

    def on_play_button_click(self):
        text_input_value = self.text_input.text()
        print("Text input value:", text_input_value)

    def on_slider1_value_changed(self, value):
        print("Volume 1:", value)

    def on_slider2_value_changed(self, value):
        print("Volume 2:", value)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())