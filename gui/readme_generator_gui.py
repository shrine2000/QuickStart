import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QCheckBox, QPushButton, QTextEdit
from readme_template import ReadmeTemplate


class ReadmeGeneratorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("README Generator")
        self.layout = QVBoxLayout()
        self.init_ui()

    def init_ui(self):
        self.checkbox_dict = {
            "Badges": QCheckBox("Badges"),
            "Authors": QCheckBox("Authors"),
            "Usage/Examples": QCheckBox("Usage/Examples"),
            "Run Locally": QCheckBox("Run Locally"),
            "Running Tests": QCheckBox("Running Tests"),
            "Demo": QCheckBox("Demo"),
            "Screenshots": QCheckBox("Screenshots"),
            "Roadmap": QCheckBox("Roadmap"),
            "License": QCheckBox("License")
        }

        self.readme_text = QTextEdit()

        generate_button = QPushButton("Generate README")
        generate_button.clicked.connect(self.generate_readme)

        self.layout.addWidget(QLabel("Select sections to include in README:"))
        for checkbox in self.checkbox_dict.values():
            self.layout.addWidget(checkbox)
        self.layout.addWidget(generate_button)

        self.layout.addWidget(QLabel("Generated README:"))
        self.layout.addWidget(self.readme_text)

        self.setLayout(self.layout)

    def generate_readme(self):
        template = ReadmeTemplate()

        for section, checkbox in self.checkbox_dict.items():
            if checkbox.isChecked():
                template.add_section(section)

        readme_content = template.generate_readme()
        self.readme_text.setPlainText(readme_content)


# Create the application
app = QApplication(sys.argv)

# Create and show the main window
window = ReadmeGeneratorGUI()
window.show()

# Run the event loop
sys.exit(app.exec_())
