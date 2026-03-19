import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout,
    QMessageBox, QMenuBar, QAction
)


class BMICalculator(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")
        self.setGeometry(300, 300, 400, 300)

        self.create_ui()

    def create_ui(self):

        # Labels and Inputs
        self.weight_label = QLabel("Enter Weight (kg):")
        self.weight_input = QLineEdit()

        self.height_label = QLabel("Enter Height (m):")
        self.height_input = QLineEdit()

        # Button
        self.calculate_button = QPushButton("Calculate BMI")
        self.calculate_button.clicked.connect(self.calculate_bmi)

        # Result Labels
        self.result_label = QLabel("BMI Result: ")
        self.status_label = QLabel("Status: ")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight_input)
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

        self.create_menu()

    def create_menu(self):
        menu_bar = QMenuBar(self)

        file_menu = menu_bar.addMenu("File")

        clear_action = QAction("Clear", self)
        clear_action.triggered.connect(self.clear_fields)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(clear_action)
        file_menu.addAction(exit_action)

        help_menu = menu_bar.addMenu("Help")

        help_action = QAction("How to use", self)
        help_action.triggered.connect(self.show_help)

        help_menu.addAction(help_action)

        self.layout().setMenuBar(menu_bar)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text())

            # Если рост больше 3 — значит введён в сантиметрах
            if height > 3:
                height = height / 100

            bmi = weight / (height ** 2)

            self.result_label.setText(f"BMI Result: {bmi:.2f}")

            if bmi < 18.5:
                status = "Underweight"
            elif bmi < 25:
                status = "Normal"
            elif bmi < 30:
                status = "Overweight"
            else:
                status = "Obese"

            self.status_label.setText(f"Status: {status}")

        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid numbers.")

    def clear_fields(self):
        self.weight_input.clear()
        self.height_input.clear()
        self.result_label.setText("BMI Result: ")
        self.status_label.setText("Status: ")

    def show_help(self):
        QMessageBox.information(
            self,
            "How to Use",
            "Enter your weight in kilograms and height in meters.\n"
            "Click 'Calculate BMI' to see your result and status."
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMICalculator()
    window.show()
    sys.exit(app.exec_())
