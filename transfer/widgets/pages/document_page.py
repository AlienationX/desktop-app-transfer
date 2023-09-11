
from PySide6.QtWidgets import QWidget, QTextEdit, QTextBrowser, QVBoxLayout
from PySide6.QtCore import QFile, QTextStream, QDir, QIODevice
from PySide6.QtGui import QTextDocument


class DocumentWidget(QWidget):
    
    def __init__(self, resource_path=""):
        super().__init__()
        
        self.document = QTextEdit(self)
        file = QFile(":/texts/home.md")
        file.open(QIODevice.ReadOnly | QIODevice.Text)
        stream_file = QTextStream(file)
        self.document.setMarkdown(stream_file.readAll())
        self.document.setReadOnly(True)
#         self.document.setStyleSheet("""
#                                     QScrollBar:vertical {
#     border: 2px solid grey;
#     background: #32CC99;
#     width: 15px;
#     margin: 22px 0 22px 0;
# }
# QScrollBar::handle:vertical {
#     background: white;
#     min-height: 20px;
# }
# QScrollBar::add-line:vertical {
#     border: 2px solid grey;
#     background: #32CC99;
#     height: 20px;
#     subcontrol-position: bottom;
#     subcontrol-origin: margin;
# }

# QScrollBar::sub-line:vertical {
#     border: 2px solid grey;
#     background: #32CC99;
#     height: 20px;
#     subcontrol-position: top;
#     subcontrol-origin: margin;
# }
# QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
#     border: 2px solid grey;
#     width: 3px;
#     height: 3px;
#     background: white;
# }

# QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
#     background: none;
# }""")

        # 创建布局
        self.layout = QVBoxLayout()
        # self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.document)
        self.setLayout(self.layout)

        