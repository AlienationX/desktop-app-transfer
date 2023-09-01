from PySide6.QtWidgets import QWidget, QBoxLayout, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Slot, QStandardPaths, QUrl, QFile, QSaveFile, QDir, QIODevice


class Container(QWidget, QBoxLayout):
    
    # TODO 实现一个容器
    
    """ 
    headerContainer = Container("row", "container")

    # 是个容器，有添加部件、添加弹簧、添加间距的功能
    headerContainer.addWidget(self.logoLabel)
    headerContainer.addStretch()
    headerContainer.addWidget(self.minBtn)
    headerContainer.addWidget(self.maxBtn)
    headerContainer.addWidget(self.closeBtn)
    
    # 同时也是个widget，可以被addWidget
    self.centralLayout.addWidget(self.headerContainer)
    """
    
    def __init__(self, direction="row", name="container"):
        super().__init__()
        self.widget = QWidget()
        self.widget.setObjectName(name)
        if direction == "row":
            self.layout = QHBoxLayout(self.widget)
        else:
            self.layout = QVBoxLayout(self.widget)
        self.layout.setContentsMargins(0, 0, 0, 0)  # 去掉默认边距