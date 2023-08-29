
from PySide6.QtWidgets import QWidget, QTextEdit, QTextBrowser, QVBoxLayout
from PySide6.QtCore import QFile, QTextStream, QDir, QIODevice
from PySide6.QtGui import QTextDocument


class DocumentWidget(QWidget):
    
    def __init__(self, resource_path=""):
        super().__init__()
        
        self.document = QTextBrowser(self)
        file = QFile(":/texts/home.md")
        file.open(QIODevice.ReadOnly | QIODevice.Text)
        stream_file = QTextStream(file)
        self.document.setMarkdown(stream_file.readAll())
        self.document.setReadOnly(True)

        # 创建布局
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.document)
        self.setLayout(self.layout)

        