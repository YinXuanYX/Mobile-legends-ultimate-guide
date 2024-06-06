from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(720,1280)
        self.setWindowTitle("Mobile Legends Win Rate Calculator")

        parentLayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()

        self.button1 = QPushButton("Heroes")
        self.button1.setFixedSize(400, 70)
        font = self.button1.font()
        font.setPointSize(18)
        self.button1.setFont(font)
        self.button2 = QPushButton("All Matches played")
        self.button2.setFixedSize(400, 70)
        font = self.button2.font()
        font.setPointSize(16)
        self.button2.setFont(font)
        self.button3 = QPushButton("Winning Rate")
        self.button3.setFixedSize(400, 70)
        font = self.button3.font()
        font.setPointSize(18)
        self.button3.setFont(font)

        buttonLayout.addWidget(self.button1)
        buttonLayout.addSpacing(50)
        buttonLayout.addWidget(self.button2)
        buttonLayout.addSpacing(50)
        buttonLayout.addWidget(self.button3)
        buttonLayout.addSpacing(50)

        self.label = QLabel("Here to be the next World Champion?!")
        font = self.font()
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        parentLayout.addLayout(buttonLayout)
        parentLayout.addWidget(self.label)

        centerWidget= QWidget()
        centerWidget.setLayout(parentLayout)
        self.setCentralWidget(centerWidget)

app = QApplication([])

window = Window()

window.show()
app.exec()