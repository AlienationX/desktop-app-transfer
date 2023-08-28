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


class OpenButton(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setupUi()
    
    def setupUi(self):
        self.inputLineEdit = QLineEdit()
        self.inputLineEdit.setPlaceholderText("请选择Excel文件或目录")
        self.inputLineEdit.setReadOnly(True)
        
        # openBtnIcon  = qta.icon("msc.folder-opened")
        # self.openBtn = QPushButton(openBtnIcon, "打开文件")
        self.openBtn = QPushButton("打开文件")

        # 创建布局
        self.layout = QHBoxLayout()
        # 将组件添加到布局中
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.editLine)