from PyQt5.QtWidgets import *
import sys
from gui.new_project_window import NewProjectWindow
from gui.readme_generator_gui import ReadmeGeneratorGUI
from gui.about_widget import AboutWidget

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

         
        self.setWindowTitle('Quick Start')

        self.Width = 800
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)

         
        self.btn_1 = QPushButton('New Project', self)
        self.btn_2 = QPushButton('Readme', self)
        self.btn_3 = QPushButton('About Us', self)
 
        self.btn_1.clicked.connect(self.button1)
        self.btn_2.clicked.connect(self.button2)
        self.btn_3.clicked.connect(self.button3)
 
        self.tab1 = self.ui1()
        self.tab2 = self.ui2()
        self.tab3 = self.ui3()
 
        self.initUI()

    def initUI(self):
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.btn_1)
        left_layout.addWidget(self.btn_2)
        left_layout.addWidget(self.btn_3)
        left_layout.addStretch(5)
        left_layout.setSpacing(20)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)

        self.right_widget = QTabWidget()
        self.right_widget.tabBar().setObjectName("mainTab")

        self.right_widget.addTab(self.tab1, '')
        self.right_widget.addTab(self.tab2, '')
        self.right_widget.addTab(self.tab3, '')
 
        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet('''QTabBar::tab{width: 0; \
            height: 0; margin: 0; padding: 0; border: none;}''')

        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.right_widget)
        main_layout.setStretch(0, 40)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
 
    def button1(self):
        self.right_widget.setCurrentIndex(0)

    def button2(self):
        self.right_widget.setCurrentIndex(1)

    def button3(self):
        self.right_widget.setCurrentIndex(2)
 
    def ui1(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(NewProjectWindow())
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


 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())