from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit
from datetime import datetime
import sys  


def on_clicked():
    data = input_field.text()
    label.setText(f"Button is clicked: text is {data}")

app = QApplication(sys.argv)

window=QWidget()
window.setWindowTitle("Example program")
window.resize(400,300)

label = QLabel("Button is not used")

input_field = QLineEdit()
button = QPushButton("Click me")

layout = QVBoxLayout()

layout.addWidget(label,alignment = Qt.AlignCenter)
layout.addWidget(button,alignment = Qt.AlignCenter)
layout.addWidget(input_field,alignment = Qt.AlignCenter)

layout.addStretch(20)

window.setLayout(layout)

button.clicked.connect(on_clicked)

window.show()

app.exec()