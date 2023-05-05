import sys
from PyQt6.QtWidgets import *


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        text = QTextBrowser("Enter text")

        # Set the central widget of the Window.s
        self.setCentralWidget(text)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()