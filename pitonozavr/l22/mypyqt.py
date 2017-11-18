import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle("Фалаут 2 топчик")
		self.setGeometry(50, 50, 640, 480)
		self.show()


if __name__ == "__main__":
	base_app = QApplication(sys.argv)
	window = MyWindow()
	sys.exit(base_app.exec_())