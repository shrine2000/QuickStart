from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QWidget, QVBoxLayout, QStackedWidget, QHBoxLayout
import sys
from gui.new_project_window import NewProjectWindow
from gui.readme_generator_gui import ReadmeGeneratorGUI
from gui.about_widget import AboutWidget
from gui.jsonformatvalidator import JSONFormatValidator



class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Quick Start')

        self.Width = 800
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)

        self.sidebar = QListWidget()

        self.sidebar.addItem('New Project')
        self.sidebar.addItem('JSON Format/Validate')
        self.sidebar.addItem('Readme')
        self.sidebar.addItem('About Us')

        self.tab1 = self.ui1()
        self.tab2 = self.ui2()
        self.tab3 = self.ui3()
        self.tab4 = self.ui4()

        self.initUI()

    def initUI(self):
        sidebar_widget = QWidget()
        sidebar_layout = QVBoxLayout()
        sidebar_layout.addWidget(self.sidebar)
        sidebar_widget.setLayout(sidebar_layout)

        # Increase the width of the sidebar
        sidebar_widget.setFixedWidth(200)

        stacked_widget = QStackedWidget()
        stacked_widget.addWidget(self.tab1)
        stacked_widget.addWidget(self.tab2)
        stacked_widget.addWidget(self.tab3)
        stacked_widget.addWidget(self.tab4)

        main_layout = QHBoxLayout()
        main_layout.addWidget(sidebar_widget)
        main_layout.addWidget(stacked_widget)
        main_layout.setStretch(0, 0)  # Disable stretching for the sidebar

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.sidebar.currentRowChanged.connect(stacked_widget.setCurrentIndex)

    def ui1(self):
        main_layout = QVBoxLayout()
        new_project_window = NewProjectWindow()
        main_layout.addWidget(new_project_window)
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui2(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(ReadmeGeneratorGUI())
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui3(self):
        main_layout = QVBoxLayout()
        about_widget = AboutWidget()
        main_layout.addWidget(about_widget)
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui4(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(JSONFormatValidator())
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('macintosh')

    ex = Window()
    ex.show()
    sys.exit(app.exec_())
