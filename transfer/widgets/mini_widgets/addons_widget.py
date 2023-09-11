
from typing import Optional
from PySide6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QWidget
from PySide6.QtCore import Qt


class HContainer(QFrame, QHBoxLayout):
    
    def __init__(self):
        super().__init__()
        QHBoxLayout.__init__(self, self)     # 调用QHBoxLayout的构造函数，第二个self代表绑定到自己的QFrame上
        
        # self.setAttribute(Qt.WA_StyledBackground, True)  # 无法继承背景色的设置，需要手动设置，便于测试 https://www.cnpython.com/qa/1523133
        # self.setContentsMargins(0, 0, 0, 0)      # 去掉默认边距 # QFrame和QHBoxLayout都有该方法，执行QHBoxLayout的才会起作用
        QHBoxLayout.setContentsMargins(self, 0, 0, 0, 0)


class VContainer(QFrame, QVBoxLayout):
    
    def __init__(self):
        super().__init__()
        QVBoxLayout.__init__(self, self)
    
        # self.setAttribute(Qt.WA_StyledBackground, True)  # 无法继承背景色的设置，需要手动设置，便于测试
        # self.setContentsMargins(0, 0, 0, 0)
        QVBoxLayout.setContentsMargins(self, 0, 0, 0, 0)


def createContainer(layout_type):
    # 工厂函数
    if layout_type == "row":
        return HContainer
    elif layout_type == "col":
        return VContainer
    else:
        raise Exception ("input layout type muse be row or col")

