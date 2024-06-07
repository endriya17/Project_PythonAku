import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Contoh PyQt5')
        self.setGeometry(100, 100, 400, 300)

        label = QLabel('Hello, PyQt5!', self)
        label.move(50, 50)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    sys.exit(app.exec_())
