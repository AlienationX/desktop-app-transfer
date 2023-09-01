from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtCore import Slot, QStandardPaths, QUrl, QFile, QSaveFile, QDir, QIODevice


class SystemBar(QListWidgetItem):
    
    def __init__(self, text, icon, state_icon):
        super().__init__()
        self.setText = text
        self.setIcon = icon

    def mousePressEvent(self, event):
        # 实现鼠标拖拽功能，记录鼠标按下的时候的坐标
        print(self.headerWidget.geometry(), "press")
        self.pressX = event.x()
        self.pressY = event.y()
 
    def mouseMoveEvent(self, event):
        pass
    

    def mouseReleaseEvent (self, event):
        pass
    
    def mouseDoubleClickEvent (self, event):
        "实现双击系统栏最大化和还原"
        pass