import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from subprocess import Popen

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Создаем кнопку "Начать"
        start_button = QPushButton('Начать', self)
        start_button.clicked.connect(self.start_another_file)

        # Создаем вертикальный layout
        layout = QVBoxLayout()
        layout.addWidget(start_button)

        # Устанавливаем layout для основного окна
        self.setLayout(layout)

        # Устанавливаем параметры основного окна
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Пример окна с кнопкой')
        self.show()

    def start_another_file(self):
        # Запускаем другой файл (another_file.py)
        Popen(['python', 'Prodjeckt.py'])
        self.show.MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
