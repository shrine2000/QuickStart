from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox, QPushButton, QTextEdit, QHBoxLayout, QFormLayout
from gui.readme_template import ReadmeTemplate

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
            "Project Structure": QCheckBox("Project Structure"),
            "Screenshots": QCheckBox("Screenshots"),
            "Roadmap": QCheckBox("Roadmap"),
            "License": QCheckBox("License")
        }

        self.project_structure_form = QFormLayout()
        self.project_structure_checkbox = self.checkbox_dict["Project Structure"]
        self.project_structure_checkbox.stateChanged.connect(self.toggle_project_structure)

        self.readme_text = QTextEdit()

        generate_button = QPushButton("Generate README")
        generate_button.clicked.connect(self.generate_readme)

        self.layout.addWidget(QLabel("Select sections to include in README:"))
        for checkbox in self.checkbox_dict.values():
            self.layout.addWidget(checkbox)

        self.layout.addWidget(QLabel("Project Structure:"))
        self.layout.addLayout(self.project_structure_form)

        self.layout.addWidget(generate_button)

        self.layout.addWidget(QLabel("Generated README:"))
        self.layout.addWidget(self.readme_text)

        self.setLayout(self.layout)

    def toggle_project_structure(self, state):
        if state == 2:  # Checked state
            self.project_structure_form.addRow(QLabel("Specify the project structure here:"))
            self.project_structure_textedit = QTextEdit()
            self.project_structure_form.addRow(self.project_structure_textedit)
        else:
            self.project_structure_form.removeRow(1)
            self.project_structure_form.removeRow(0)

    def generate_readme(self):
        template = ReadmeTemplate(self.project_structure_textedit.toPlainText())

        for section, checkbox in self.checkbox_dict.items():
            if checkbox.isChecked():
                template.add_section(section)

        readme_content = template.generate_readme()
        self.readme_text.setPlainText(readme_content)
