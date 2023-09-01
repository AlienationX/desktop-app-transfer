from PySide6.QtWidgets import QWidget, QBoxLayout, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Slot, QStandardPaths, QUrl, QFile, QSaveFile, QDir, QIODevice


class MessageBox(QWidget, QBoxLayout):
    
    # TODO 实现一个自定义的消息框
    
    def __init__(self, direction="row", name="container"):
        super().__init__()
        self.widget = QWidget()
        self.widget.setObjectName(name)
        if direction == "row":
            self.layout = QHBoxLayout(self.widget)
        else:
            self.layout = QVBoxLayout(self.widget)
        self.layout.setContentsMargins(0, 0, 0, 0)  # 去掉默认边距