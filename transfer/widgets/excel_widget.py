
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QMessageBox,
    QGroupBox,
    QComboBox,
    QRadioButton,
    QCheckBox,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QGridLayout,
    QVBoxLayout,
    QFileDialog,
)
from PySide6.QtCore import Slot, Qt, QSize, QStandardPaths, QFile, QSaveFile, QDir, QThread, QThreadPool, Signal
from PySide6.QtGui import QFont

import qtawesome as qta
import pandas as pd
from loguru import logger

from pathlib import Path
from datetime import datetime
import csv
import time


class ExcelToCsvWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        self.inputFiles = []
        self.outputPath = ""
        self.options = {
            "encoding": "utf-8",         # utf-8, gbk
            "quoting": csv.QUOTE_NONE,   # "QUOTE_MINIMAL", "QUOTE_ALL", "QUOTE_NONNUMERIC", "QUOTE_NONE"
        }
        
        self.setupUi()
    
    def setupUi(self):
        """页面初始化"""
        
        self.label = QLabel("WELCOME EXCEL TO CSV PAGE\nThanks for your support")
        # self.label.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter|Qt.AlignLeft|Qt.AlignTop)
        
        self.choiceComboBox = QComboBox()
        self.choiceComboBox.addItem("文件")
        self.choiceComboBox.addItem("文件夹")
        self.choiceComboBox.setToolTip("VIP用户支持选择文件夹，进行文件批量转换")
        # self.choiceComboBox.activated.connect(lambda x: print("choice ", x))
        
        self.inputLineEdit = QLineEdit()
        self.inputLineEdit.setPlaceholderText("请选择Excel文件或目录")
        self.inputLineEdit.setReadOnly(True)
        
        openBtnIcon  = qta.icon("msc.folder-opened", color="blue")
        self.openBtn = QPushButton(openBtnIcon, "打开文件")

        self.outputLineEdit = QLineEdit()
        self.outputLineEdit.setPlaceholderText("请选择保存的路径")
        self.outputLineEdit.setReadOnly(True)
        
        saveBtnIcon  = qta.icon("msc.folder-active", color="blue")
        self.saveBtn = QPushButton(saveBtnIcon, "保存文件")
        
        self.radioBtn1 = QRadioButton("保持原始数据")
        self.radioBtn1.setToolTip("所有字段都用逗号分隔，如果内容存在逗号，\n打开文件可能会导致串列问题，不推荐")
        self.radioBtn2 = QRadioButton("单个文本使用双引号转义")
        self.radioBtn2.setToolTip("如果字段内容包括逗号，则该内容会额外增加双引号对字段内容进行包裹，\n以防止串列问题，默认值")
        self.radioBtn2.setChecked(True)
        self.radioBtn3 = QRadioButton("所有文本字段增加双引号")
        self.radioBtn3.setToolTip("所有文本字段默认额外增加双引号对字段内容进行包裹，\n不包括数字")
        self.radioBtn4 = QRadioButton("所有字段增加双引号")
        self.radioBtn4.setToolTip("所有字段默认额外增加双引号对字段内容进行包裹，\n包括非文本")
        vboxLayout1 = QVBoxLayout()
        vboxLayout1.addWidget(self.radioBtn1)
        vboxLayout1.addWidget(self.radioBtn2)
        vboxLayout1.addWidget(self.radioBtn3)
        vboxLayout1.addWidget(self.radioBtn4)
        vboxLayout1.addStretch()
        self.groupBox1 = QGroupBox("引号")
        self.groupBox1.setLayout(vboxLayout1)
        
        self.radioBtn5 = QRadioButton("UTF8")
        self.radioBtn5.setToolTip("UTF8编码")
        self.radioBtn5.setChecked(True)
        self.radioBtn6 = QRadioButton("ANSI/GBK")
        self.radioBtn6.setToolTip("中文编码")
        vboxLayout2 = QVBoxLayout()
        vboxLayout2.addWidget(self.radioBtn5)
        vboxLayout2.addWidget(self.radioBtn6)
        vboxLayout2.addStretch()
        self.groupBox2 = QGroupBox("编码")
        self.groupBox2.setLayout(vboxLayout2)
        
        self.coverCheckBox = QCheckBox("覆盖已存在文件")
        self.coverCheckBox.setChecked(True)
        self.coverCheckBox.setEnabled(False)
        vboxLayout3 = QVBoxLayout()
        vboxLayout3.addWidget(self.coverCheckBox)
        vboxLayout3.addStretch()
        self.groupBox3 = QGroupBox("选项")
        self.groupBox3.setLayout(vboxLayout3)
        
        self.startBtnIcon  = qta.icon("msc.play", color="blue")
        self.startBtn = QPushButton(self.startBtnIcon, "执行")
        
        self.progressBar = QProgressBar()
        self.progressBar.setAlignment(Qt.AlignCenter)

        # 创建布局
        self.gridLayout = QGridLayout()
        # 将组件添加到布局中（N行N列）初始值序号是0，(行, 列, 宽度, 高度)
        self.gridLayout.addWidget(self.label, 0, 0)
        self.gridLayout.addWidget(self.choiceComboBox, 1, 0)
        self.gridLayout.addWidget(self.inputLineEdit, 2, 0, 1, 5)
        self.gridLayout.addWidget(self.openBtn, 2, 5)
        self.gridLayout.addWidget(self.outputLineEdit, 3, 0, 1, 5)
        self.gridLayout.addWidget(self.saveBtn, 3, 5)
        self.gridLayout.addWidget(self.groupBox1, 4, 0)
        self.gridLayout.addWidget(self.groupBox2, 4, 1)
        self.gridLayout.addWidget(self.groupBox3, 4, 2)
        # self.gridLayout.addWidget(self.overwriteCheckBox, 5, 3, alignment=Qt.AlignLeft|Qt.AlignTop)  # 可以设置grid的位置
        self.gridLayout.addWidget(self.startBtn, 5, 0, 1, self.gridLayout.columnCount())
        self.gridLayout.setRowStretch(6, 1)
        self.gridLayout.addWidget(self.progressBar, 7, 0, 1, self.gridLayout.columnCount())
        # self.gridLayout.setVerticalSpacing(10)        # 设置每行之间的间距
        # self.gridLayout.setHorizontalSpacing(10)    # 设置每列之间的间距
        print(self.gridLayout.verticalSpacing())
        print(self.gridLayout.horizontalSpacing())
        print(self.gridLayout.rowCount(), "行", self.gridLayout.columnCount(), "列")
        
        # 动态图标
        fa5_button = QPushButton('Font Awesome! (regular)')
        spin_icon = qta.icon('fa5s.spinner', color='blue', animation=qta.Spin(fa5_button))
        fa5_button.setIcon(spin_icon)
        self.gridLayout.addWidget(fa5_button, 99, 0, 1, self.gridLayout.columnCount())
        
        # 为窗体添加布局
        self.setLayout(self.gridLayout)
        
        # 添加点击事件
        self.openBtn.clicked.connect(self.open)
        self.saveBtn.clicked.connect(self.save)
        self.startBtn.clicked.connect(self.execute)
        
    @Slot()
    def open(self):
        print(self.choiceComboBox.currentIndex())
        if self.choiceComboBox.currentIndex() == 0:
            pass
        else:
            dir_path = QFileDialog.getExistingDirectory(
                self, "Open Directory", QDir.homePath(), QFileDialog.ShowDirsOnly
            )
            if dir_path:
                dest_dir = QDir(dir_path)
                self.inputLineEdit.setText(QDir.fromNativeSeparators(dest_dir.path()))
                for item in dest_dir.entryList():
                    suffix = item.split(".")[-1]
                    if suffix in ["xlsx", "xls"]:
                        file = dest_dir.filePath(item)
                        self.inputFiles.append(file)
    
    @Slot()
    def save(self):
        if self.choiceComboBox.currentIndex() == 0:
            pass
        else:
            dir_path = QFileDialog.getExistingDirectory(
                self, "Choice Directory", QDir.homePath(), QFileDialog.ShowDirsOnly
            )
            if dir_path:
                dest_dir = QDir(dir_path)
                self.outputLineEdit.setText(QDir.fromNativeSeparators(dest_dir.path()))
                self.outputPath = dest_dir.path()
    
    @Slot()
    def execute(self):
        print("inputFiles = ", self.inputFiles)
        print("outputPath = ", self.outputPath)
        self.inputFiles =  [
            r'C:/Users/Admin/Desktop/in/副本赣州市皮肤病医院（赣州市皮肤病研究所、赣州市麻风病康复中心、赣州市性病防治中心）-医保-src-彩色多普勒超声-收费项目明细-20230821172226247.xlsx', 
            r'C:/Users/Admin/Desktop/in/北京一体机开发环境.xlsx',
            r'C:/Users/Admin/Desktop/in/1.xlsx',
            r'C:/Users/Admin/Desktop/in/2.xlsx',
            r'C:/Users/Admin/Desktop/in/3.xlsx',
            r'C:/Users/Admin/Desktop/in/4.xlsx',
            r'C:/Users/Admin/Desktop/in/5.xlsx',
        ]
        self.outputPath = r"C:/Users/Admin/Desktop/out"
        if not self.inputFiles:
            QMessageBox.warning(self, "Input Error", "请选择Excel文件或目录")  # 只支持QMessageBox.Icon
            return
        if not self.outputPath:
            QMessageBox.warning(self, "Output Error", "请选择保存的路径")
            return
        
        self.progressBar.setValue(1)                                         # 预先设置为1%
        self.updateOptions()                                                 # 更新选项值
        
        workThread = WorkThread(self)                                        # 将self传进去，绑定到部件上
        workThread.setArgs(self.inputFiles, self.outputPath, self.options)   # 设置参数，传递进线程
        workThread.signal.connect(lambda x: self.progressBar.setValue(x))
        workThread.started.connect(self.setStartStatus)
        workThread.finished.connect(self.setEndStatus)
        workThread.finished.connect(workThread.deleteLater)                  # 完成后销毁线程
        workThread.start()
    
    def updateOptions(self):
        if self.radioBtn1.isChecked():
            self.options["quoting"] = csv.QUOTE_NONE
        if self.radioBtn2.isChecked():
            self.options["quoting"] = csv.QUOTE_MINIMAL
        if self.radioBtn3.isChecked():
            self.options["quoting"] = csv.QUOTE_NONNUMERIC
        if self.radioBtn4.isChecked():
            self.options["quoting"] = csv.QUOTE_ALL
        print(self.options)
    
    def setStartStatus(self):
        runBtnIcon = qta.icon('fa5s.spinner', color='blue', animation=qta.Spin(self.startBtn))
        self.startBtn.setIcon(runBtnIcon)
        self.startBtn.setText("执行中......")
        self.startBtn.setEnabled(False)
        self.openBtn.setEnabled(False)
        self.saveBtn.setEnabled(False)
    
    def setEndStatus(self):
        self.startBtn.setIcon(self.startBtnIcon)
        self.startBtn.setText("执行")
        self.startBtn.setEnabled(True)
        self.openBtn.setEnabled(True)
        self.saveBtn.setEnabled(True)  


class WorkThread(QThread):
    signal = Signal(int)
    # signal = Signal(int, str)  # 可以发送多个值
    
    # 参数
    input_files = []
    output_path = ""
    option = {}
    
    # 设置参数
    def setArgs(self, input_files, output_path, options):
        self.input_files = input_files
        self.output_path = output_path
        self.options = options
    
    # start执行的函数
    def run(self):
        count = len(self.input_files)
        i = 0
        for file in self.input_files:
            from_file =  file
            filename = Path(file).name
            to_file = Path(self.output_path).joinpath(filename).with_suffix(".csv")
            print(datetime.now(), from_file, to_file)
            self.excelToCsv(from_file, to_file)
            
            i += 1
            time.sleep(1)
            self.signal.emit(int(i / count *100))

    def excelToCsv(self, from_file, to_file):
        df = pd.read_excel(from_file)
        df.to_csv(to_file, index=False, encoding=self.options["encoding"], quoting=self.options["quoting"])
        
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
        