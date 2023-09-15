from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import sys

class WidgetA(QWidget):
    signal = Signal(dict)
    
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.btn = QPushButton("click", self)
        self.btn.clicked.connect(self.done_and_emit)
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.btn)
        self.setLayout(self.layout)
        
    def done_and_emit(self):
        print(self.__class__, "done")
        self.signal.emit({
            "code": 0,
            "msg": "ok",
            "data": {
                "message": "i am w1 done."
            }
        })
        

class WidgetB(QWidget):
    signal = Signal(dict)
    
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.btn = QPushButton("click", self)
        self.btn.clicked.connect(self.done_and_emit)
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.btn)
        self.setLayout(self.layout)

    def done_and_emit(self):
        print(self.__class__, "done")
        self.signal.emit({
            "code": 0,
            "msg": "ok",
            "data": {
                "message": "i am w2 done."
            }
        })
    
    def done(self, data):
        print("i am dooooone too.")
        print(data["data"]["message"])
        
class TestWidget(QWidget):
    
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.w1 = WidgetA()
        self.w2 = WidgetB()

        # 给信号绑定回调函数
        self.w1.signal.connect(lambda x: self.w2.done(x))  # w1发送信号过来后，再执行w2的方法

        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.w1)
        self.layout.addWidget(self.w2)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TestWidget()
    w.show()
    app.exec()