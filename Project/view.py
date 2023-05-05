import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPalette, QColor


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(900, 500)

        layout = QVBoxLayout()

        line = QLineEdit()
        line.resize(1, 1)

        layout.addWidget(line)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()