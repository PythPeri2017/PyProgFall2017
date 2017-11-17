# Создается приложение
# Создается окно. Создать 6 блоков (нор), вмещающих и картинки, и кнопки.
# Наш бобер должен выскакивать из норы. 
# У нас должна быть возможность колотить бобра.
# Должен быть счет подбитых бобров.

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
		self.setWindowTitle("Лукамана первое приложение")
		self.setGeometry(50, 50, 800, 600)
		self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MyWindow()
	sys.exit(app.exec_())