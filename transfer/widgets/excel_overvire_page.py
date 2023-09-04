
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QMessageBox,
    QTextEdit,
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
from PySide6.QtCore import Slot, Qt, QFile, QDir, QThread, QThreadPool, Signal, QIODevice, QTextStream
from PySide6.QtGui import QFont, QPixmap

import qtawesome as qta
import pandas as pd
from ydata_profiling import ProfileReport
from loguru import logger

from pathlib import Path
from datetime import datetime
import time
        
class ExcelOverviewWidget(QWidget):
    
    # 自定义信号，给状态栏发送信息
    message_signal = Signal(str)
    
    def __init__(self):
        super().__init__()
        self.input_file = ""
        self.options = {}
        self.setupUi()
    
    def setupUi(self):
        """页面初始化"""
        
        self.inputLineEdit = QLineEdit()
        self.inputLineEdit.setPlaceholderText("请选择Excel文件")
        self.inputLineEdit.setReadOnly(True)
        
        openBtnIcon  = qta.icon("msc.folder-opened", color="white")
        self.openBtn = QPushButton(openBtnIcon, "打开文件")
        
        self.startBtnIcon  = qta.icon("msc.play", color="white")
        self.startBtn = QPushButton(self.startBtnIcon, "预览概况")
        
        self.readLable = QLabel()
        self.readLable.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        self.readLable.setText("""
1、概要：数据类型，唯一值，缺失值，内存大小
2、分位数统计：最小值、最大值、中位数、Q1、Q3、最大值，值域，四分位
3、描述性统计：均值、众数、标准差、绝对中位差、变异系数、峰值、偏度系数
4、最频繁出现的值，直方图/柱状图
5、相关性分析可视化：突出强相关的变量，Spearman, Pearson矩阵相关性色阶图
""")

        self.report = QTextEdit(self)
        self.report.setReadOnly(True)
        
        # 创建布局
        self.gridLayout = QGridLayout(self)
        # 将组件添加到布局中
        self.gridLayout.addWidget(self.inputLineEdit, 2, 0, 1, 5)
        self.gridLayout.addWidget(self.openBtn, 2, 5)
        self.gridLayout.addWidget(self.startBtn, 5, 0, 1, self.gridLayout.columnCount())
        self.gridLayout.addWidget(self.readLable, 6, 0, 5, self.gridLayout.columnCount())
        self.gridLayout.addWidget(self.report, 12, 0, 1, self.gridLayout.columnCount())
        self.gridLayout.setRowStretch(99, 1)
        
        # 添加点击事件
        self.openBtn.clicked.connect(self.open)
        self.startBtn.clicked.connect(self.execute)

    @Slot()
    def open(self):
        # "Images (*.png *.xpm *.jpg);;Text files (*.txt);;XML files (*.xml)"
        file_tuple = QFileDialog.getOpenFileName(self, "Open Excel File", QDir.homePath(), "Excel (*.xlsx *.xls)")
        if file_tuple:
            file = file_tuple[0]
            self.inputLineEdit.setText(QDir.fromNativeSeparators(file))

    @Slot()
    def execute(self):
        # self.inputLineEdit.setText(r"C:\Users\Admin\Desktop\in\副本赣州市皮肤病医院（赣州市皮肤病研究所、赣州市麻风病康复中心、赣州市性病防治中心）-医保-src-彩色多普勒超声-收费项目明细-20230821172226247.xlsx")
        self.inputLineEdit.setText(r"C:\Users\Admin\Desktop\in\1.xlsx")
        if not self.inputLineEdit.text():
            QMessageBox.warning(self, "Input Error", "请选择Excel文件或目录")  # 只支持QMessageBox.Icon
            return
        
        input_file = Path(self.inputLineEdit.text())
        self.input_file = str(input_file)
        
        self.updateOptions()                                                 # 更新选项值
        
        workThread = WorkThread(self)                                        # 将self传进去，绑定到部件上
        workThread.setArgs(self.input_file, "self.output_path", self.options)   # 设置参数，传递进线程
        # workThread.signal.connect(lambda x: self.progressBar.setValue(x))
        workThread.signal.connect(lambda value, msg: self.execute_work_signal(value, msg))
        workThread.started.connect(self.setStartStatus)
        workThread.finished.connect(self.setEndStatus)
        workThread.finished.connect(workThread.deleteLater)                  # 完成后销毁线程
        workThread.start()
        
    def execute_work_signal(self, value, msg):
        self.message_signal.emit(msg)  # 完成一个文件，就发送给状态栏进行显示
    
    def updateOptions(self):
        print(self.options)
    
    def setStartStatus(self):
        runBtnIcon = qta.icon("fa5s.spinner", color="blue", animation=qta.Spin(self.startBtn))
        self.startBtn.setIcon(runBtnIcon)
        self.startBtn.setText("执行中......")
        self.startBtn.setEnabled(False)
        self.openBtn.setEnabled(False)
    
    def setEndStatus(self):
        # 读取html
        # file = QFile("output_file.html")
        # file.open(QIODevice.ReadOnly | QIODevice.Text)
        # stream_file = QTextStream(file)
        # self.report.setHtml(stream_file.readAll())
        
        self.startBtn.setIcon(self.startBtnIcon)
        self.startBtn.setText("预览概况")
        self.startBtn.setEnabled(True)
        self.openBtn.setEnabled(True)


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
        df = pd.read_excel(self.input_file)
        profile = ProfileReport(df, title="Report Book", minimal=True)
        profile.to_file("output_file.html")
        print("done.")
        self.signal.emit(1, self.input_file + " done .")
