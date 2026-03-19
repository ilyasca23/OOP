from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit
from calculator import Calculator


class CalculatorWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.calculator = Calculator()

        self.setWindowTitle("Calculator")
        self.setGeometry(200, 200, 300, 300)

        self.input = QLineEdit()
        self.input.setReadOnly(True)

        layout = QGridLayout()

        layout.addWidget(self.input, 0, 0, 1, 4)

        buttons = [
            ("7",0,0), ("8",0,1), ("9",0,2), ("/",0,3),
            ("4",1,0), ("5",1,1), ("6",1,2), ("*",1,3),
            ("1",2,0), ("2",2,1), ("3",2,2), ("-",2,3),
            ("0",3,0), ("C",3,1), ("=",3,2), ("+",3,3)
        ]

        for text,row,col in buttons:
            button = QPushButton(text)
            button.clicked.connect(self.handle_button)
            layout.addWidget(button,row+1,col)

        self.setLayout(layout)

    def handle_button(self):

        button = self.sender()
        value = button.text()

        if value == "C":
            self.calculator.clear_expression()
            self.input.setText("")

        elif value == "=":
            result = self.calculator.calculate()
            self.input.setText(str(result))

        else:
            self.calculator.add_to_expression(value)
            self.input.setText(self.calculator.get_expression())
