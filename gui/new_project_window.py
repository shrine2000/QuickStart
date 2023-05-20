from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QComboBox, QTextEdit, QVBoxLayout, QWidget


class NewProjectWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window properties
        self.setWindowTitle("New Project")

        # Create the label and text box for the project name
        self.project_name_label = QLabel("Project Name:", self)
        self.project_name_textbox = QLineEdit(self)

        # Create the license label and drop-down box
        self.license_label = QLabel("License:", self)
        self.license_dropdown = QComboBox(self)
        self.license_dropdown.addItem("Apache License 2.0")
        self.license_dropdown.addItem("BSD 3-Clause License")
        self.license_dropdown.addItem("MIT License")

        # Create the label and text box for the project directory
        self.project_directory_label = QLabel("Project Directory:", self)
        self.project_directory_textbox = QLineEdit(self)
        self.browse_button = QPushButton("Browse", self)
        self.browse_button.clicked.connect(self.browse_directory)

        # Create the label and text box for the GitHub repo URL
        self.github_url_label = QLabel("GitHub Repo URL:", self)
        self.github_url_textbox = QLineEdit(self)

        # Create the create button
        self.create_button = QPushButton("Create", self)
        self.create_button.clicked.connect(self.create_project)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.project_name_label)
        layout.addWidget(self.project_name_textbox)
        layout.addWidget(self.license_label)
        layout.addWidget(self.license_dropdown)
        layout.addWidget(self.project_directory_label)
        layout.addWidget(self.project_directory_textbox)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.github_url_label)
        layout.addWidget(self.github_url_textbox)
        layout.addWidget(self.create_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


    def create_project(self):
        # Get the project name, license, and project directory from the text boxes
        project_name = self.project_name_textbox.text()
        license_option = self.license_dropdown.currentText()
        github_url = self.github_url_textbox.text()
        project_directory = self.project_directory_textbox.text()

        # Create the project folder in the selected directory
        os.makedirs(os.path.join(project_directory, project_name), exist_ok=True)

        # Change into the new folder
        os.chdir(os.path.join(project_directory, project_name))

        # Initialize a Git repository
        subprocess.run(["git", "init"], check=True)

        # Create a README.md file
        with open("README.md", "w") as readme_file:
            readme_file.write("# " + project_name + "\n\nThis is my project.")

        # Create a .gitignore file
        with open(".gitignore", "w") as gitignore_file:
            gitignore_file.write("/.history \n/.idea \n/.vscode")

        # Create the appropriate license file based on the selected license option
        if license_option == "Apache License 2.0":
            with open("LICENSE", "w") as license_file:
                license_file.write(APACHE_LICENSE_TEXT)
        elif license_option == "BSD 3-Clause License":
            with open("LICENSE", "w") as license_file:
                license_file.write(BSD_LICENSE_TEXT)
        elif license_option == "MIT License":
            with open("LICENSE", "w") as license_file:
                license_file.write(MIT_LICENSE_TEXT)

        # Add the files to Git
        subprocess.run(["git", "add", "README.md", "LICENSE", ".gitignore"], check=True)

        # Commit the files
        subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)

        if github_url:
            # Push the changes to GitHub
            subprocess.run(["git", "remote", "add", "origin", github_url], check=True)
            subprocess.run(["git", "push", "-u", "origin", "master"], check=True)

        # Show a message box to confirm that the project was created
        confirmation_message = f"Project {project_name} created with {license_option} license."
        self.show_message_box("Success", confirmation_message)

    def show_message_box(self, title, message):
        message_box = QMessageBox(self)
        message_box.setWindowTitle(title)
        message_box.setText(message)
        message_box.addButton(QMessageBox.Ok)
        message_box.exec_()

    def browse_directory(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        directory = QFileDialog.getExistingDirectory(self, "Select Directory", "", options=options)

        # Set the selected directory in the text box
        if directory:
            self.project_directory_textbox.setText(directory)


# License texts
APACHE_LICENSE_TEXT = """\
Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/
"""

BSD_LICENSE_TEXT = """\
BSD 3-Clause License
For the full license text, please see the LICENSE file in
"""

MIT_LICENSE_TEXT = """\
MIT License
For the full license text, please see the LICENSE file in
"""
