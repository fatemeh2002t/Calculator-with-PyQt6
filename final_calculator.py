from PyQt6.QtWidgets import (
    QWidget, QPushButton, QApplication, QLineEdit, QGridLayout,
    QVBoxLayout, QHBoxLayout
)
from PyQt6.QtCore import Qt
import sys

class CalculatorButton(QPushButton):
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)
        self.setFixedSize(80, 60)
        self.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                background-color: #2e7d32;
                color: white;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #cddc39;
                color: black;
            }
            QPushButton:pressed {
                background-color: #dce775;
                color: black;
            }
        """)

class Calculator(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Calculator")
        self.resize(450, 400)
        self.__buttons_text = [
            "7", "8", "9", "/",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "0", ".", "=", "+"
        ]

        self.setStyleSheet("""
            QWidget {
                background-color: #263238;
                color: white;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            QLineEdit {
                background-color: #37474f;
                border: none;
                padding: 15px;
                font-size: 28px;
                border-radius: 10px;
                color: white;
            }
        """)

        self.__creating_widgets()

    def __creating_widgets(self):
        self.__input = QLineEdit()
        self.__input.setReadOnly(False)
        self.__grid_layout = QGridLayout()
        self.__grid_layout.setSpacing(12)
        self.__grid_layout.setContentsMargins(15, 15, 15, 15)

        col = 0
        row = 0
        for button_text in self.__buttons_text:
            button = CalculatorButton(button_text)
            button.clicked.connect(self.button_clicked)
            self.__grid_layout.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.__clearall = CalculatorButton("C")
        self.__clearall.clicked.connect(self.clear_all)

        self.__back = CalculatorButton("<")
        self.__back.clicked.connect(self.backspace)

        self.__horiz = QHBoxLayout()
        self.__horiz.setSpacing(10)
        self.__horiz.addWidget(self.__clearall)
        self.__horiz.addWidget(self.__back)

        self.__main_layout = QVBoxLayout()
        self.__main_layout.setContentsMargins(20, 20, 20, 20)
        self.__main_layout.setSpacing(15)
        self.__main_layout.addWidget(self.__input)
        self.__main_layout.addLayout(self.__grid_layout)
        self.__main_layout.addLayout(self.__horiz)

        self.setLayout(self.__main_layout)

    def button_clicked(self):
        button = self.sender()
        button_text = button.text()
        if button_text == "=":
            try:
                result = str(eval(self.__input.text()))
                self.__input.setText(result)
            except Exception:
                self.__input.setText("Error")
        else:
            self.__input.setText(self.__input.text() + button_text)

    def clear_all(self):
        self.__input.clear()

    def backspace(self):
        self.__input.setText(self.__input.text()[:-1])

    def keyPressEvent(self, event):
        key = event.key()
        text = self.__input.text()
        if key in (Qt.Key.Key_0, Qt.Key.Key_1, Qt.Key.Key_2, Qt.Key.Key_3, Qt.Key.Key_4,
                   Qt.Key.Key_5, Qt.Key.Key_6, Qt.Key.Key_7, Qt.Key.Key_8, Qt.Key.Key_9, Qt.Key.Key_Period):
            self.__input.setText(text + event.text())
        elif key in (Qt.Key.Key_Plus, Qt.Key.Key_Minus, Qt.Key.Key_Slash, Qt.Key.Key_Asterisk):
            self.__input.setText(text + event.text())
        elif key in (Qt.Key.Key_Enter, Qt.Key.Key_Return, Qt.Key.Key_Equal):
            try:
                result = str(eval(text))
                self.__input.setText(result)
            except Exception:
                self.__input.setText("Error")
        elif key == Qt.Key.Key_Backspace:
            self.__input.setText(text[:-1])
        elif key == Qt.Key.Key_Delete:
            self.__input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
