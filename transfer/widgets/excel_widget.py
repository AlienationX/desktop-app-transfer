
from PySide6.QtWidgets import (
    QWidget, 
    QLabel,
    QMessageBox,
    QRadioButton,
    QCheckBox,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QGridLayout,
    QVBoxLayout,
    QFileDialog
)
from PySide6.QtCore import Slot, Qt, QSize, QStandardPaths, QUrl, QFile, QSaveFile, QDir, QIODevice
from PySide6.QtGui import QFont


class ExcelToCsvWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setupUi()
    
    def setupUi(self):
        """页面初始化"""
        
        self.label = QLabel("WELCOME EXCEL TO CSV PAGE\nThank you for support")
        # self.label.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        
        self.inputFile = QLineEdit()
        self.inputFile.setPlaceholderText("请选择Excel文件")
        self.inputFile.setReadOnly(True)
        self.openBtn = QPushButton("打开文件")

        self.radioBtn1 = QRadioButton("单个文本使用双引号转义")
        self.radioBtn1.setToolTip("如果字段内容包括逗号，则该内容会额外增加双引号对字段内容进行包裹，以来防止串列问题")
        self.radioBtn1.setChecked(True)
        self.radioBtn2 = QRadioButton("所有文本字段默认增加双引号")
        self.radioBtn2.setToolTip("所有文本字段默认额外增加双引号对字段内容进行包裹")
        self.radioBtn3 = QRadioButton("不带双引号")
        self.radioBtn3.setToolTip("所有字段都用逗号分隔，如果内容存在逗号，打开文件可能会导致串列问题")
        
        self.outputFile = QLineEdit()
        self.outputFile.setPlaceholderText("请选择保存的路径")
        self.outputFile.setReadOnly(True)
        self.saveBtn = QPushButton("保存文件")
        
        self.overwriteCheckBox = QCheckBox("覆盖已存在文件")
        
        self.startBtn = QPushButton("执行")
        
        self.progressBar = QProgressBar()
        self.progressBar.setAlignment(Qt.AlignCenter)

        # 创建布局
        self.gridLayout = QGridLayout()
        # 将组件添加到布局中
        self.gridLayout.addWidget(self.label, 1, 1)
        self.gridLayout.addWidget(self.inputFile, 2, 1)
        self.gridLayout.addWidget(self.openBtn, 2, 2)
        self.gridLayout.addWidget(self.radioBtn1, 3, 1)
        self.gridLayout.addWidget(self.radioBtn2, 4, 1)
        self.gridLayout.addWidget(self.radioBtn3, 5, 1)
        self.gridLayout.addWidget(self.outputFile, 6, 1)
        self.gridLayout.addWidget(self.saveBtn, 6, 2)
        self.gridLayout.addWidget(self.overwriteCheckBox, 7, 1)
        self.gridLayout.addWidget(self.startBtn, 8, 1, 1, 2)
        self.gridLayout.setRowStretch(9, 1)
        self.gridLayout.addWidget(self.progressBar, 10, 1, 1, 2)  

        # 为窗体添加布局
        self.setLayout(self.gridLayout)


class ExcelSplitWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setupUi()
    
    def setupUi(self):
        """页面初始化"""
        
        self.label = QLabel("WELCOME EXCEL SPLIT PAGE")

        # 创建布局
        self.layout = QVBoxLayout()
        # 将组件添加到布局中
        self.layout.addWidget(self.label)

        # 为窗体添加布局
        self.setLayout(self.layout)
        