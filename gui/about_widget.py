from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget


class AboutWidget(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        title_label = QLabel("About")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; text-align: center;")
        main_layout.addWidget(title_label)

        description_label = QLabel("The QuickStart is a PyQt5-based application that enables users to \neffortlessly create new projects with customizable features and settings. \nWith this application, users can specify the project name, \nselect a license, choose the project directory, \nand even provide a GitHub repository URL.")
        description_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(description_label)

        twitter_handle_label = QLabel()
        twitter_handle_label.setOpenExternalLinks(True)
        twitter_handle_label.setText('<a href="https://twitter.com/shrine_sabu">Author</a>')
        twitter_handle_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        twitter_handle_label.setCursor(QCursor(Qt.PointingHandCursor))
        main_layout.addWidget(twitter_handle_label)

        main_layout.addStretch()

        self.setLayout(main_layout)
