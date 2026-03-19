import sys
from PyQt5.QtWidgets import QApplication
from calculator_window import CalculatorWindow

app = QApplication(sys.argv)

window = CalculatorWindow()
window.show()

sys.exit(app.exec_())
