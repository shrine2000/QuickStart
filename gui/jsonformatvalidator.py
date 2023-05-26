from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import json


class JSONFormatValidator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # JSON Input
        self.json_input_label = QLabel("JSON Input:")
        self.json_input_text = QTextEdit()
        self.json_input_text.setFont(QFont("Courier"))
        self.json_input_text.setTabChangesFocus(True)

        # Validation Result
        self.validation_result_label = QLabel("Validation Result:")
        self.validation_result_text = QTextEdit()
        self.validation_result_text.setReadOnly(True)

        # Validate Button
        self.validate_button = QPushButton("Validate")
        self.validate_button.clicked.connect(self.validateJSON)

        # Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.json_input_label)
        main_layout.addWidget(self.json_input_text)
        main_layout.addWidget(self.validation_result_label)
        main_layout.addWidget(self.validation_result_text)
        main_layout.addWidget(self.validate_button)

        self.setLayout(main_layout)

    def validateJSON(self):
        json_text = self.json_input_text.toPlainText()
        try:
            json_object = json.loads(json_text)
            self.validation_result_text.setText("Valid JSON")
        except ValueError as e:
            self.validation_result_text.setText("Invalid JSON: " + str(e))


# Example usage:
if __name__ == '__main__':
    app = QApplication([])
    validator = JSONFormatValidator()
    validator.show()
    app.exec_()
