from PySide6.QtWidgets import QWidget, QBoxLayout, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Slot, QStandardPaths, QUrl, QFile, QSaveFile, QDir, QIODevice

"""TODO 间距和背景色设置无效"""

class HContainer(QWidget, QHBoxLayout):
    
    def __init__(self):
        super().__init__()
        QHBoxLayout.__init__(self, self)     # 调用QHBoxLayout的构造函数，第二个self代表绑定到自己的QWidget上
        
        # self.setStyleSheet("background-color: green;")
        print("HContainer", self.getContentsMargins())
        self.setContentsMargins(0, 0, 0, 0)  # 去掉默认边距
        print("HContainer", self.getContentsMargins())


class VContainer(QWidget, QVBoxLayout):
    
    def __init__(self):
        super().__init__()
        QVBoxLayout.__init__(self, self)
    
        # self.setStyleSheet("background-color: green;")
        print("VContainer", self.getContentsMargins())
        self.setContentsMargins(0, 0, 0, 0)  # 去掉默认边距
        print("VContainer", self.getContentsMargins())


def createContainer(layout_type):
    # 工厂函数
    if layout_type == "row":
        return HContainer
    else:
        return VContainer
    