import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel,QMainWindow, QVBoxLayout, QTableWidgetItem, \
    QTableWidget, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt

class  MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SpinBox example")
        self.resize(600,400)

        central_widget = QWidget()

        layout = QVBoxLayout()

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(2)
        self.table_widget.setHorizontalHeaderLabels(["Name", "Surname"])
        self.table_widget.setVerticalHeaderLabels(["1", "2"])
        self.table_widget.setEditTriggers(QTableWidget.AllEditTriggers)
        
        self.button = QPushButton("submit")
        self.button.clicked.connect(self.show_submitted_data)

        self.label = QLabel()

        layout.addWidget(self.table_widget, alignment=Qt.AlignCenter)
        layout.addWidget(self.button, alignment=Qt.AlignCenter)
        layout.addWidget(self.label, alignment=Qt.AlignCenter)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_submitted_data(self):
        values = []
        number_of_rows = self.table_widget.rowCount()
        number_of_columns = self.table_widget.columnCount()
        for row in range(number_of_rows):
            full_row_of_text = []
            for column in range(number_of_columns):
                item = self.table_widget.item(row,column)
                if item:
                    item_text = item.text()
                    full_row_of_text.append(item_text.capitalize())
            values.append(" ".join(full_row_of_text))
        self.label.setText("\n".join(values))




def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()





