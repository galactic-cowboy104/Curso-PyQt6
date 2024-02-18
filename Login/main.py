from PyQt6.QtWidgets import QWidget, QLabel, QMessageBox
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializar_gui()

    def inicializar_gui(self):
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('Ventana Principal')
        self.generar_contenido()

    def generar_contenido(self):

        image_path = 'background.jpg'

        try:
            with open(image_path):
                image_label = QLabel(self)
                image_label.setPixmap(QPixmap(image_path))

        except FileNotFoundError as e:
            QMessageBox.warning(self, 'Error', f'Imagen no encontrada: {e}.',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
