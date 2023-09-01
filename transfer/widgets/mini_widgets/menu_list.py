from PySide6.QtWidgets import QWidget, QListWidgetItem
from PySide6.QtCore import Slot, QStandardPaths, QUrl, QFile, QSaveFile, QDir, QIODevice


class MenuList(QWidget):
    
    """列表菜单，支持二级菜单"""
    
    def __init__(self, text, icon, state_icon):
        super().__init__()
        self.setText = text
        self.setIcon = icon
