import sys
from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QLineEdit,
                             QPushButton, QMessageBox, QCheckBox)
from PyQt6.QtGui import QFont
from registro import RegistrarUsuarioView
from main import MainWindow


class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializar_gui()

    def inicializar_gui(self):
        self.setGeometry(100, 100, 350, 250)
        self.setWindowTitle("Log In")
        self.generar_form()
        self.show()

    def generar_form(self):

        self.is_logged = False

        user_label = QLabel(self)
        user_label.setText("Usuario:")
        user_label.setFont(QFont('Arial', 10))
        user_label.move(20, 54)

        self.user_input = QLineEdit(self)
        self.user_input.resize(245, 24)
        self.user_input.move(95, 50)

        password_label = QLabel(self)
        password_label.setText("Contraseña:")
        password_label.setFont(QFont('Arial', 10))
        password_label.move(20, 86)

        self.password_input = QLineEdit(self)
        self.password_input.resize(245, 24)
        self.password_input.move(95, 82)
        self.password_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        self.check_view_password = QCheckBox(self)
        self.check_view_password.setText("Ver contraseña")
        self.check_view_password.move(90, 110)
        self.check_view_password.toggled.connect(self.mostrar_contrasena)

        login_button = QPushButton(self)
        login_button.setText('Acceder')
        login_button.resize(320, 34)
        login_button.move(20, 140)
        login_button.clicked.connect(self.iniciar_mainview)

        register_button = QPushButton(self)
        register_button.setText('Registrar')
        register_button.resize(320, 34)
        register_button.move(20, 180)
        register_button.clicked.connect(self.registrar_usuario)

    def mostrar_contrasena(self, clicked):
        if clicked:
            self.password_input.setEchoMode(
                QLineEdit.EchoMode.Normal
            )
        else:
            self.password_input.setEchoMode(
                QLineEdit.EchoMode.Password
            )

    def iniciar_mainview(self):

        users = []
        user_path = 'usuarios.txt'

        try:

            with open(user_path, 'r') as f:
                for linea in f:
                    users.append(linea.strip('\n'))

            login_info = f'{self.user_input.text()},{self.password_input.text()}'

            if login_info in users:

                QMessageBox.information(self, 'Info', 'Inicio de sesión exitoso',
                                        QMessageBox.StandardButton.Ok,
                                        QMessageBox.StandardButton.Ok)

                self.is_logged = True
                self.close()
                self.abrir_mainview()

            else:
                QMessageBox.warning(self, 'Error', 'Credenciales incorrectas.',
                                    QMessageBox.StandardButton.Close,
                                    QMessageBox.StandardButton.Close)

        except FileNotFoundError as e:
            QMessageBox.warning(self, 'Error', f'La base de datos no existe: {e}.',
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)

    def registrar_usuario(self):
        self.new_user_form = RegistrarUsuarioView()
        self.new_user_form.show()

    def abrir_mainview(self):
        self.mainwindow = MainWindow()
        self.mainwindow.show()


def main():
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
