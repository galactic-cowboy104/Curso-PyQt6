import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QMessageBox,
                             QPushButton, QVBoxLayout)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializar_gui()

    def inicializar_gui(self):

        self.setMinimumHeight(200)
        self.setFixedWidth(220)
        self.setWindowTitle('Layout Vertical')
        self.generar_form()
        self.show()

    def generar_form(self):

        boton1 = QPushButton('Botón 1')
        boton2 = QPushButton('Botón 2')
        boton3 = QPushButton('Botón 3')
        boton4 = QPushButton('Botón 4')

        boton1.clicked.connect(self.imprimir_nombre)
        boton2.clicked.connect(self.imprimir_nombre)
        boton3.clicked.connect(self.imprimir_nombre)
        boton4.clicked.connect(self.imprimir_nombre)

        layout = QVBoxLayout()
        layout.addWidget(boton1)
        layout.addWidget(boton2)
        layout.addWidget(boton3)
        layout.addWidget(boton4)

        self.setLayout(layout)

    def imprimir_nombre(self):
        boton = self.sender()
        QMessageBox.information(self, 'Info', f'{boton.text()}',
                                QMessageBox.StandardButton.Ok,
                                QMessageBox.StandardButton.Ok)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
