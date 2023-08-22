
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

import pandas as pd

from pathlib import Path


class ExcelToCsvWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        self.inputFiles = []
        self.outputPath = ""
        
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
        
        self.inputLineEdit = QLineEdit()
        self.inputLineEdit.setPlaceholderText("请选择Excel文件或目录")
        self.inputLineEdit.setReadOnly(True)
        self.openBtn = QPushButton("打开文件")

        self.radioBtn1 = QRadioButton("单个文本使用双引号转义")
        self.radioBtn1.setToolTip("如果字段内容包括逗号，则该内容会额外增加双引号对字段内容进行包裹，以来防止串列问题")
        self.radioBtn1.setChecked(True)
        self.radioBtn2 = QRadioButton("所有文本字段默认增加双引号")
        self.radioBtn2.setToolTip("所有文本字段默认额外增加双引号对字段内容进行包裹")
        self.radioBtn3 = QRadioButton("不带双引号")
        self.radioBtn3.setToolTip("所有字段都用逗号分隔，如果内容存在逗号，打开文件可能会导致串列问题")
        
        self.enterCheckBox = QCheckBox("包括子文件夹下的Excel文件")
        
        self.outputLineEdit = QLineEdit()
        self.outputLineEdit.setPlaceholderText("请选择保存的路径")
        self.outputLineEdit.setReadOnly(True)
        self.saveBtn = QPushButton("保存文件")
        
        self.radioBtn4 = QRadioButton("UTF8")
        self.radioBtn4.setToolTip("UTF8编码")
        self.radioBtn4.setChecked(True)
        self.radioBtn5 = QRadioButton("ANSI/GBK")
        self.radioBtn5.setToolTip("中文编码")
        
        self.overwriteCheckBox = QCheckBox("覆盖已存在文件")
        
        self.startBtn = QPushButton("执行")
        
        self.progressBar = QProgressBar()
        self.progressBar.setAlignment(Qt.AlignCenter)

        # 创建布局
        self.gridLayout = QGridLayout()
        # 将组件添加到布局中
        self.gridLayout.addWidget(self.label, 1, 1)
        self.gridLayout.addWidget(self.inputLineEdit, 2, 1)
        self.gridLayout.addWidget(self.openBtn, 2, 2)
        self.gridLayout.addWidget(self.radioBtn1, 3, 1)
        self.gridLayout.addWidget(self.radioBtn2, 4, 1)
        self.gridLayout.addWidget(self.radioBtn3, 5, 1)
        self.gridLayout.addWidget(self.outputLineEdit, 6, 1)
        self.gridLayout.addWidget(self.saveBtn, 6, 2)
        self.gridLayout.addWidget(self.overwriteCheckBox, 7, 1)
        self.gridLayout.addWidget(self.startBtn, 8, 1, 1, 2)
        self.gridLayout.setRowStretch(9, 1)
        self.gridLayout.addWidget(self.progressBar, 10, 1, 1, 2)  

        # 为窗体添加布局
        self.setLayout(self.gridLayout)
        
        # 添加点击事件
        self.openBtn.clicked.connect(self.open)
        self.saveBtn.clicked.connect(self.save)
        self.startBtn.clicked.connect(self.execute)
        
    @Slot()
    def open(self):
        dir_path = QFileDialog.getExistingDirectory(
            self, "Open Directory Or File", QDir.homePath(), QFileDialog.ShowDirsOnly
        )

        if dir_path:
            dest_dir = QDir(dir_path)
            self.inputLineEdit.setText(QDir.fromNativeSeparators(dest_dir.path()))
            for item in dest_dir.entryList():
                extension = item.split(".")[-1]
                if extension in ["xlsx", "xls"]:
                    file = dest_dir.filePath(item)
                    self.inputFiles.append(file)
            self.gridLayout.addWidget(self.enterCheckBox, 3, 2)
    
    @Slot()
    def save(self):
        dir_path = QFileDialog.getExistingDirectory(
            self, "Open Directory", QDir.homePath(), QFileDialog.ShowDirsOnly
        )

        if dir_path:
            dest_dir = QDir(dir_path)
            self.outputLineEdit.setText(QDir.fromNativeSeparators(dest_dir.path()))
            self.outputPath = dest_dir.path()
    
    @Slot()
    def execute(self):
        print("inputFiles = ", self.inputFiles)
        print("outputPath = ", self.outputPath)
        self.inputFiles =  [r'C:/Users/Admin/Desktop/in/副本赣州市皮肤病医院（赣州市皮肤病研究所、赣州市麻风病康复中心、赣州市性病防治中心）-医保-src-彩色多普勒超声-收费项目明细-20230821172226247.xlsx', r'C:/Users/Admin/Desktop/in/北京一体机开发环境.xlsx']
        self.outputPath = "C:/Users/Admin/Desktop/out"
        if not self.inputFiles:
            QMessageBox.warning(self, "Input Error", "请选择Excel文件或目录")
            return
        if not self.outputPath:
            QMessageBox.warning(self, "Output Error", "请选择保存的路径")
            return
        
        self.startBtn.setText("执行中......")
        self.startBtn.setEnabled(False)
        self.openBtn.setEnabled(False)
        self.saveBtn.setEnabled(False)
        
        for file in self.inputFiles:
            from_file =  file
            to_file = Path(self.outputPath).joinpath(Path(file).name)
            print(from_file, to_file)
            self.excelToCsv(from_file, to_file)
            
        self.startBtn.setText("执行")
        self.startBtn.setEnabled(True)
        self.openBtn.setEnabled(True)
        self.saveBtn.setEnabled(True)
        
    def excelToCsv(self, from_file, to_file):
        df = pd.read_excel(from_file)
        df.to_csv(to_file)

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
        