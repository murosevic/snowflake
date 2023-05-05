import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QLabel

class MessengerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the window title and size
        self.setWindowTitle("Messenger")
        self.setFixedSize(400, 500)

        # Create the layout for the window
        mainLayout = QVBoxLayout()
        messageLayout = QVBoxLayout()
        inputLayout = QHBoxLayout()

        # Create the label for displaying messages
        messageLabel = QLabel()
        messageLabel.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        messageLabel.setWordWrap(True)

        # Create the textbox for entering messages
        inputTextBox = QTextEdit()
        inputTextBox.setFixedHeight(50)
        inputTextBox.setPlaceholderText("Say something")
        inputTextBox.setStyleSheet("QTextEdit { border: none; background-color: white; padding: 10px; border-radius: 25px; }"
                                    "QTextEdit:focus { border: none; background-color: white; }")

        # Create the button for sending messages
        sendButton = QPushButton("Send")
        sendButton.setFixedHeight(50)
        sendButton.setStyleSheet("QPushButton { border: none; border-radius: 25px; background-color: #00bfff; color: white; }"
                                  "QPushButton:hover { background-color: #00a5ff; }"
                                  "QPushButton:pressed { background-color: #008bff; }")

        # Add the message label and input textbox to the message layout
        messageLayout.addWidget(messageLabel)
        messageLayout.setContentsMargins(0, 0, 0, 0)
        inputLayout.addWidget(inputTextBox)
        inputLayout.addWidget(sendButton)
        inputLayout.setContentsMargins(0, 0, 0, 0)

        # Add the message and input layouts to the main layout
        mainLayout.addLayout(messageLayout)
        mainLayout.addLayout(inputLayout)
        mainLayout.setContentsMargins(20, 20, 20, 20)

        # Set the main layout for the window
        self.setLayout(mainLayout)

        # Connect the send button to the function for sending messages
        sendButton.clicked.connect(lambda: self.sendMessage(inputTextBox, messageLabel))

    def sendMessage(self, inputTextBox, messageLabel):
        # Get the message from the input textbox
        message = inputTextBox.toPlainText()

        # Clear the input textbox
        inputTextBox.clear()

        # Add the message to the message label
        messageLabel.setText(f"{message}\n{messageLabel.text()}")


if __name__ == '__main__':
    # Create the application
    app = QApplication(sys.argv)

    # Create and show the main window
    window = MessengerWindow()
    window.show()

    # Run the application
    sys.exit(app.exec())
