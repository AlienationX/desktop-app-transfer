
from PySide6.QtWidgets import (
    QWidget, 
    QLabel,
    QMessageBox,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QFileDialog
)
from PySide6.QtCore import Slot, QStandardPaths, QUrl, QFile, QSaveFile, QDir, QIODevice


class WordToPDFWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setupUi()
    
    def setupUi(self):
        """页面初始化"""
        
        self.label = QLabel("WELCOME CSV")
        self.editLine = QLineEdit("haha")

        # 创建布局
        self.layout = QVBoxLayout()
        # 将组件添加到布局中
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.editLine)

        # 为窗体添加布局
        self.setLayout(self.layout)

        