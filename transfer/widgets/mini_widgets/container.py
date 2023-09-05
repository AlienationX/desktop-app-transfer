from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt

"""TODO 间距和背景色设置无效"""

class HContainer(QWidget, QHBoxLayout):
    
    def __init__(self):
        super().__init__()
        QHBoxLayout.__init__(self, self)     # 调用QHBoxLayout的构造函数，第二个self代表绑定到自己的QWidget上
        
        self.setAttribute(Qt.WA_StyledBackground, True)  # 无法继承背景色的设置，需要手动设置，便于测试 https://www.cnpython.com/qa/1523133
        # self.setStyleSheet("background-color: green;")
        print("HContainer", self.getContentsMargins())
        # self.setContentsMargins(0, 0, 0, 0)      # 去掉默认边距 # QWidget和QHBoxLayout都有该方法，执行QHBoxLayout的才会起作用
        QHBoxLayout.setContentsMargins(self, 0, 0, 0, 0)
        print("HContainer", self.getContentsMargins())


class VContainer(QWidget, QVBoxLayout):
    
    def __init__(self):
        super().__init__()
        QVBoxLayout.__init__(self, self)
    
        self.setAttribute(Qt.WA_StyledBackground, True)  # 无法继承背景色的设置，需要手动设置，便于测试
        # self.setStyleSheet("background-color: green;")
        print("VContainer", self.getContentsMargins())
        # self.setContentsMargins(0, 0, 0, 0)
        QVBoxLayout.setContentsMargins(self, 0, 0, 0, 0)
        print("VContainer", self.getContentsMargins())


def createContainer(layout_type):
    # 工厂函数
    if layout_type == "row":
        return HContainer
    else:
        return VContainer
    