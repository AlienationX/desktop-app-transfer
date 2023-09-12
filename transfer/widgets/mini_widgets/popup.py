from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys

class popup(QWidget):
    def __init__(self, parent = None, widget=None):    
        QWidget.__init__(self, parent)
        layout = QGridLayout(self)
        button = QPushButton("Very Interesting Text Popup. Here's an arrow")
        layout.addWidget(button)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        self.adjustSize()  # 适应窗口大小
        # tag this widget as a popup
        self.setWindowFlags(Qt.Popup)  # Popup or ToolTip
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明

        print(widget.rect())
        point = widget.rect().bottomRight()
        print(point)
        # map that point as a global position
        global_point = widget.mapToGlobal(point)
        print(global_point)
        # by default, a widget will be placed from its top-left corner, so
        # we need to move it to the left based on the widgets width
        self.move(global_point - QPoint(self.width(), 0))
        print(global_point - QPoint(self.width(), 0))

class Window(QWidget):
        
    def __init__(self):
        QWidget.__init__(self)
        self.button = QPushButton('Hit this button to show a popup', self)
        self.button.clicked.connect(self.handleOpenDialog)
        self.button.move(250, 50)
        self.resize(600, 200)

    def handleOpenDialog(self):
        self.popup = popup(self, self.button)
        self.popup.show()

if __name__ == '__main__':
        app = QApplication([])
        win = Window()
        win.show()
        sys.exit(app.exec_())