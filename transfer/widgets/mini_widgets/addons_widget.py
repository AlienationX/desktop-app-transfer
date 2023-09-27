
from typing import Optional
from PySide6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QWidget, QApplication
from PySide6.QtCore import Qt


class HContainer(QFrame, QHBoxLayout):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        QHBoxLayout.__init__(self, self)     # 调用QHBoxLayout的构造函数，第二个self代表绑定到自己的QFrame上
        
        # self.setAttribute(Qt.WA_StyledBackground, True)  # 无法继承背景色的设置，需要手动设置，便于测试 https://www.cnpython.com/qa/1523133
        self.setContentsMargins(0, 0, 0, 0)      # 去掉默认边距 # QFrame和QHBoxLayout都有该方法，执行QHBoxLayout的才会起作用
    
    def setContentsMargins(self, left, top, right, bottom):
        # overwrite QFrame setContentsMargins
        QHBoxLayout.setContentsMargins(self, left, top, right, bottom)


class VContainer(QFrame, QVBoxLayout):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        QVBoxLayout.__init__(self, self)
    
        # self.setAttribute(Qt.WA_StyledBackground, True)  # 无法继承背景色的设置，需要手动设置，便于测试
        # self.setContentsMargins(0, 0, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)
    
    def setContentsMargins(self, left, top, right, bottom):
        QVBoxLayout.setContentsMargins(self, left, top, right, bottom)


def createContainer(layout_type):
    # 工厂函数
    if layout_type == "row":
        return HContainer
    elif layout_type == "col":
        return VContainer
    else:
        raise Exception ("input layout type muse be row or col")


# https://www.cnblogs.com/apocelipes/p/10268108.html
class MaskWidget(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        self.setAttribute(Qt.WA_StyledBackground)  # 自定义控件只有设置该属性后才能正常设置背景
        self.setStyleSheet("background: rgba(0, 0, 0, 102);")   # rgba第4个值代表透明度
        
        # 这样设置不行
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setStyleSheet("background-color: rgb(140, 140, 140);")  
        # self.setWindowOpacity(0.5)
        
        self.setHidden(True)  # 默认隐藏
        
    def showMaskAll(self):
        """=设置遮罩大小与parent一致"""
        parent_rect = self.parent().geometry()
        self.resize(parent_rect.width(), parent_rect.height())
        self.show()
