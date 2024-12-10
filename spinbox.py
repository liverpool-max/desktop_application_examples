import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel,QMainWindow, QVBoxLayout, QSpinBox, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt

class  MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SpinBox example")
        self.resize(600,400)

        cenrtal_widget = QWidget()

        layout = QVBoxLayout()

        self.spinbox = QSpinBox(self)
        self.spinbox.setRange(1,12)
        self.spinbox.setValue(1)
        self.spinbox.setSuffix(" mounth")

        self.welcome_label = QLabel("Please select mounth",self)

        self.button = QPushButton("Click",self)
        self.button.clicked.connect(self.on_clicked)

        self.result_label = QLabel(self)

        layout.addWidget(self.welcome_label, alignment = Qt.AlignCenter )
        layout.addWidget(self.spinbox, alignment = Qt.AlignCenter )
        layout.addWidget(self.button, alignment = Qt.AlignCenter )
        layout.addWidget(self.result_label, alignment = Qt.AlignCenter )

        cenrtal_widget.setLayout(layout)
        self.setCentralWidget(cenrtal_widget)

    def on_clicked(self):
        value = self.spinbox.value()
        current_mounth = 11
        if current_mounth > value:
            self.result_label.setText(f"Your selection : {value} You selected a past mounth")
        elif current_mounth == value:
            self.result_label.setText(f"Your selected : {value} You selected current mounth")
        else:
            self.result_label.setText(f"Your selected : {value} You selected future mounth")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

