from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtCore import Slot, QStandardPaths, QUrl, QFile, QSaveFile, QDir, QIODevice


class ListItem(QListWidgetItem):
    
    def __init__(self, text, icon, state_icon):
        super().__init__()
        self.setText = text
        self.setIcon = icon
