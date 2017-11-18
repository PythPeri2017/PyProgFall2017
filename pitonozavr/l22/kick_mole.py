# Запуск приложения, запуск окна.
# Создаем 9 нор, 3х3, из которых высовывается крот.
# Эти норы должны хранить изображение норы и быть кликабельными.
# Крот должен высовываться.
# Игрок может колотить крота.
# Счетчик попаданий по голове крота



import sys
import random

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class MyWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle("Бей крота")
		self.setGeometry(50, 50, 640, 480)
		self.show()


if __name__ == "__main__":
	base_app = QApplication(sys.argv)
	window = MyWindow()
	sys.exit(base_app.exec_())