from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import sys

class WidgetA(QWidget):
    signal = Signal(dict)
    
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.btn = QPushButton("click", self)
        self.btn.clicked.connect(self.done)
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.btn)
        self.setLayout(self.layout)
        
    def done(self):
        print(self.__class__, "done")
        self.signal.emit({
            "code": 0,
            "msg": "ok",
            "data": {
                "message": "i an done."
            }
        })
        

class WidgetB(QWidget):
    signal = Signal(dict)
    
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.btn = QPushButton("click", self)
        self.btn.clicked.connect(self.done)
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.btn)
        self.setLayout(self.layout)

    def done(self):
        print(self.__class__, "done")
        self.signal.emit({
            "code": 0,
            "msg": "ok",
            "data": {
                "message": "i an done."
            }
        })
        
class TestWidget(QWidget):
    
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.w1 = WidgetA()
        self.w2 = WidgetB()
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.w1)
        self.layout.addWidget(self.w2)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TestWidget()
    w.show()
    app.exec()