import sys
from PyQt6.QtWidgets import QApplication, QWidget


class VentanaVacia(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializar_gui()

    def inicializar_gui(self):
        self.setGeometry(100, 100, 250, 250)
        self.setWindowTitle('Mi Primera Ventana')
        self.show()


def main():
    app = QApplication(sys.argv)
    ventana = VentanaVacia()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
