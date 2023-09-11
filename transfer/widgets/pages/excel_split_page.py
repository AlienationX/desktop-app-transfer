
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
from PySide6.QtGui import QFont, QPixmap

import qtawesome as qta
import pandas as pd
from loguru import logger

from pathlib import Path
from datetime import datetime
import csv
import time
        
class ExcelSplitWidget(QWidget):
    
    # 自定义信号，给状态栏发送信息
    message_signal = Signal(str)
    
    def __init__(self):
        super().__init__()
        self.input_file = ""
        self.output_path = ""
        self.options = {
            "split_col_name": ""
        }
        self.setupUi()
    
    def setupUi(self):
        """页面初始化"""
        
        self.inputLineEdit = QLineEdit()
        self.inputLineEdit.setPlaceholderText("请选择Excel文件")
        self.inputLineEdit.setReadOnly(True)
        
        openBtnIcon  = qta.icon("msc.folder-opened", color="white")
        self.openBtn = QPushButton(openBtnIcon, "打开文件")
        
        self.outputLineEdit = QLineEdit()
        self.outputLineEdit.setPlaceholderText("请选择保存的目录")
        self.outputLineEdit.setReadOnly(True)
        
        saveBtnIcon  = qta.icon("msc.folder-active", color="white")
        self.saveBtn = QPushButton(saveBtnIcon, "保存文件")
        
        self.choiceLabel = QLabel("请选择拆分的字段：")
        
        self.choiceComboBox = QComboBox()
        self.choiceComboBox.setPlaceholderText("请选择")
        self.choiceComboBox.setToolTip("VIP用户支持选择文件夹，进行文件批量转换")  
        
        self.startBtnIcon  = qta.icon("msc.play", color="white")
        self.startBtn = QPushButton(self.startBtnIcon, "执行")
        
        self.progressBar = QProgressBar()
        self.progressBar.setAlignment(Qt.AlignCenter)

        # 创建布局
        self.gridLayout = QGridLayout(self)
        # 将组件添加到布局中
        self.gridLayout.addWidget(self.inputLineEdit, 2, 0, 1, 5)
        self.gridLayout.addWidget(self.openBtn, 2, 5)
        self.gridLayout.addWidget(self.outputLineEdit, 3, 0, 1, 5)
        self.gridLayout.addWidget(self.saveBtn, 3, 5)
        self.gridLayout.addWidget(self.choiceLabel, 4, 0)
        self.gridLayout.addWidget(self.choiceComboBox, 4, 1, 1, 2)
        self.gridLayout.addWidget(self.startBtn, 5, 0, 1, self.gridLayout.columnCount())
        self.gridLayout.setRowStretch(6, 1)
        self.gridLayout.addWidget(self.progressBar, 7, 0, 1, self.gridLayout.columnCount())
        
        # 添加点击事件
        self.openBtn.clicked.connect(self.open)
        self.saveBtn.clicked.connect(self.save)
        self.startBtn.clicked.connect(self.execute)

    @Slot()
    def open(self):
        # "Images (*.png *.xpm *.jpg);;Text files (*.txt);;XML files (*.xml)"
        file_tuple = QFileDialog.getOpenFileName(self, "Open Excel File", QDir.homePath(), "Excel (*.xlsx *.xls)")
        if file_tuple:
            file = file_tuple[0]
            self.inputLineEdit.setText(QDir.fromNativeSeparators(file))
            print(file)
            df = pd.read_excel(file, nrows=1)
            columns = df.columns.tolist()
            self.choiceComboBox.clear()
            self.choiceComboBox.addItems(columns)
            
    
    @Slot()
    def save(self):
        dir_path = QFileDialog.getExistingDirectory(
            self, "Choice Directory", QDir.homePath(), QFileDialog.ShowDirsOnly
        )
        if dir_path:
            dest_dir = QDir(dir_path)
            self.outputLineEdit.setText(QDir.fromNativeSeparators(dest_dir.path()))

    @Slot()
    def execute(self):
        self.inputLineEdit.setText(r"C:\Users\Admin\Desktop\in\副本赣州市皮肤病医院（赣州市皮肤病研究所、赣州市麻风病康复中心、赣州市性病防治中心）-医保-src-彩色多普勒超声-收费项目明细-20230821172226247.xlsx")
        self.outputLineEdit.setText(r"C:/Users/Admin/Desktop/out")
        if not self.inputLineEdit.text():
            QMessageBox.warning(self, "Input Error", "请选择Excel文件或目录")  # 只支持QMessageBox.Icon
            return
        if not self.outputLineEdit.text():
            QMessageBox.warning(self, "Output Error", "请选择保存的文件或目录")
            return
        if not self.choiceComboBox.currentText():
            QMessageBox.warning(self, "Input Error", "请选择需要拆分的字段")
            return
        
        inputFile = Path(self.inputLineEdit.text())
        outputPath = Path(self.outputLineEdit.text())
        self.input_file = str(inputFile)
        self.output_path = str(outputPath)
        print("input_file = ", self.input_file)
        print("output_path = ", self.output_path)
        
        self.progressBar.setValue(1)                                         # 预先设置为1%
        self.updateOptions()                                                 # 更新选项值
        
        workThread = WorkThread(self)                                        # 将self传进去，绑定到部件上
        workThread.setArgs(self.input_file, self.output_path, self.options)   # 设置参数，传递进线程
        # workThread.signal.connect(lambda x: self.progressBar.setValue(x))
        workThread.signal.connect(lambda value, msg: self.execute_work_signal(value, msg))
        workThread.started.connect(self.setStartStatus)
        workThread.finished.connect(self.setEndStatus)
        workThread.finished.connect(workThread.deleteLater)                  # 完成后销毁线程
        workThread.start()
        
    def execute_work_signal(self, value, msg):
        self.progressBar.setValue(value)
        self.message_signal.emit(msg)  # 完成一个文件，就发送给状态栏进行显示
    
    def updateOptions(self):
        self.options["split_col_name"] = self.choiceComboBox.currentText()
        print(self.options)
    
    def setStartStatus(self):
        runBtnIcon = qta.icon("fa5s.spinner", color="blue", animation=qta.Spin(self.startBtn))
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
    signal = Signal(int, str)
    # signal = Signal(int, str)  # 可以发送多个值
    
    # 参数
    # input_file = ""
    # output_path = ""
    # options = {}
    
    # 设置参数
    def setArgs(self, input_file, output_path, options):
        self.input_file = input_file
        self.output_path = output_path
        self.options = options
    
    # start执行的函数
    def run(self):
        from_file = self.input_file
        split_col_name = self.options["split_col_name"]
        df = pd.read_excel(from_file)
        values = df[split_col_name].unique().tolist()
        count = len(values)
        for i in range(count):
            to_file = str(Path(self.output_path).joinpath(str(Path(from_file).stem) + "_" + str(values[i]) + ".xlsx"))
            print(datetime.now(), from_file, to_file)
            df[ df[split_col_name] == values[i] ].to_excel(to_file, index=False)
            time.sleep(1)  # TODO 暂时用来测试
            self.signal.emit(int((i + 1) / count *100), to_file + " done .")
