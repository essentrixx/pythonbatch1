# PyQt5 introduction
import sys
from time import sleep

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QCheckBox, QRadioButton, QButtonGroup
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

# class MainWindow(QMainWindow):
    # def __init__(self):
        # super().__init__()
        # self.setWindowTitle("My cool first GUI")
        # self.setGeometry(x, y, width, height)
        # self.setGeometry(700, 300, 500, 500)
        # self.setWindowIcon(QIcon("vite.svg"))
        #
        # label = QLabel("Hello", self)   # self refers to window obj, window = parent widget, label = child widget
        # label.setFont(QFont("Arial", 16))
        # label.setGeometry(0, 0, 500, 100)
        # label.setStyleSheet("color: #fff;"
        #                     "background-color: #6fdcf7")

        # label.setAlignment(Qt.AlignTop) # vertically top
        # label.setAlignment(Qt.AlignBottom) # vertically bot
        # label.setAlignment(Qt.AlignVCenter) # vertically center

        # label.setAlignment(Qt.AlignRight)  # hoz right
        # label.setAlignment(Qt.AlignLeft)  # hoz left
        # label.setAlignment(Qt.AlignHCenter) # hoz center

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)   # both h v
        # label.setAlignment(Qt.AlignCenter)  # both h v with shortcut


# PyQt5 Images
        # label = QLabel(self)
        # label.setGeometry(0, 0, 250, 250)
        #
        # pixmap = QPixmap("chef-claude-icon.png")
        # label.setPixmap(pixmap)
        #
        # label.setScaledContents(True) # fix image according to w and h
        #
        # label.setGeometry(      # both center
        #                     (self.width() - label.width()) // 2,
        #                     (self.height() - label.height()) // 2,
        #                     label.width(),
        #                     label.height()
        #                 )


# PyQt5 Layouts
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700, 300, 500, 500)
#         self.initUI()

    # def initUI(self):
    #     central_widget = QWidget()
    #     self.setCentralWidget(central_widget)
    #
    #     label1 = QLabel("#1", self)
    #     label2 = QLabel("#2", self)
    #     label3 = QLabel("#3", self)
    #     label4 = QLabel("#4", self)
    #     label5 = QLabel("#5", self)
    #
    #     label1.setStyleSheet("background-color: red;")
    #     label2.setStyleSheet("background-color: blue;")
    #     label3.setStyleSheet("background-color: green;")
    #     label4.setStyleSheet("background-color: yellow;")
    #     label5.setStyleSheet("background-color: purple;")

        # vbox = QVBoxLayout()
        #
        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)
        #
        # central_widget.setLayout(vbox)

        # hbox = QHBoxLayout()
        #
        # hbox.addWidget(label1)
        # hbox.addWidget(label2)
        # hbox.addWidget(label3)
        # hbox.addWidget(label4)
        # hbox.addWidget(label5)
        #
        # central_widget.setLayout(hbox)

        # grid = QGridLayout()
        #
        # grid.addWidget(label1, 0, 0)    # row 0 column 0
        # grid.addWidget(label2, 0, 1)
        # grid.addWidget(label3)
        # grid.addWidget(label4)
        # grid.addWidget(label5)
        #
        # central_widget.setLayout(grid)

# Push Button
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700, 300, 500, 500)
#         self.button = QPushButton("Click me!", self)
#         self.label = QLabel("Hello python", self)
#         self.initUI()
#
#     def initUI(self):
#         self.button.setGeometry(150, 200, 200, 100)
#         self.button.setStyleSheet("font-size: 30px;")
#         self.button.clicked.connect(self.on_click)
#
#         self.label.setGeometry(150, 300, 200, 100)
#         self.label.setStyleSheet("font-size: 50px")
#
#     def on_click(self):
#         # print("Clicked")
#         # self.button.setText("hello")    # click me! to hello
#         # self.button.setDisabled(True)
#
#         self.label.setText("Goodbye")


# checkbox
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700, 300, 500, 500)
#         self.checkbox = QCheckBox("like food?", self)
#         self.initUI()
#
#
#     def initUI(self):
#         self.checkbox.setGeometry(10, 0, 500, 100)
#         self.checkbox.setStyleSheet("font-size: 30px")
#         self.checkbox.setChecked(False)
#         self.checkbox.stateChanged.connect(self.checkbox_changed)
#
#
#     def checkbox_changed(self, state):
#         # if state == Qt.Checked:
#         #     print("you like food")
#         # else:
#         #     print("You do not like food")
#
#         print("you like food" if state == Qt.Checked else "You do not like food")


# radio buttons
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Mastercard", self)
        self.radio3 = QRadioButton("Gift card", self)
        self.radio4 = QRadioButton("Store", self)
        self.radio5 = QRadioButton("Online", self)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        self.initUI()


    def initUI(self):
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)

        self.setStyleSheet("QRadioButton { font-size: 40px; }")

        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)


    def radio_button_changed(self):
        radio_button = self.sender()  # sender return widget and sent to signal(toggle)
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()