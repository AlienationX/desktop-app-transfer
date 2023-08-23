
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget, 
    QLabel,
    QMessageBox,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QFileDialog,
    QTreeWidget,
    QTreeWidgetItem,
    QStatusBar,
    QStackedWidget
)
from PySide6.QtCore import Slot, QSize, QStandardPaths, QUrl, QFile, QSaveFile, QDir, QIODevice
import qtawesome as qta

from widgets.excel_widget import ExcelToCsvWidget, ExcelSplitWidget
from widgets.csv_widget import CsvToExcelWidget
from widgets.word_widget import WordToPDFWidget


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi()
    
    def setupUi(self):
        """页面初始化"""
        # 设置窗体大小及标题
        self.resize(700, 400)
        self.setWindowTitle("Transfer - 转换工具")
        
        # QTreeWidget组件定义
        self.treeWidget = QTreeWidget()
        self.treeWidget.header().setVisible(False)           # 隐藏标头
        self.treeWidget.setStyleSheet("border:none;")       # 隐藏边框
        # self.treeWidget.headerItem().setText(0, "参数名")    # 给第1列设置标题
        # self.treeWidget.setColumnWidth(0, 200)               # 给第1列设置列宽200
        self.treeWidget.setMaximumSize(QSize(200, 16777215))
        
        # QTreeWidget组件内容设置
        self.menu_map = {
            "EXCEL": {
                "转换成CSV": {
                    "name" : "excelToCsvWidget",
                    "icon" : qta.icon("ri.file-excel-2-line", color="red"),
                    "class" : ExcelToCsvWidget()
                },
                "文件拆分": {
                    "name" : "excelSplitWidget",
                    "icon" : qta.icon("ri.file-excel-2-line", color="red"),
                    "class" : ExcelSplitWidget()
                }
            },
            "CSV":{
                "转换成EXCEL": {
                    "name" : "csvToExcelWidget",
                    "icon" : qta.icon("ri.file-excel-2-line", color="red"),
                    "class" : CsvToExcelWidget(),
                }
            },
            "WORD":{
                "转换成PDF": {
                    "name" : "wordToPDFWidget",
                    "icon" : qta.icon("ri.file-excel-2-line", color="red"),
                    "class" : WordToPDFWidget(),
                }
            }
        }
        
        # self.homeItem = QTreeWidgetItem()
        # self.homeItem.setText(0, "HOME")
        # self.treeWidget.addTopLevelItem(self.homeItem)
        
        # 设置stackedWidget
        self.stackedWidget = QStackedWidget()
        
        for k in self.menu_map:
            rootItem = QTreeWidgetItem()
            rootItem.setText(0, k)
            for key, value in self.menu_map[k].items():
                rootItem.setIcon(0, value["icon"])
                childItem = QTreeWidgetItem()
                childItem.setText(0, key)
                rootItem.addChild(childItem)
                setattr(self, value["name"], value["class"])  # 把所有widget绑定到self上便于操作，但是也增加了内存消耗。可以优化在切换的时候创建
                self.stackedWidget.addWidget(getattr(self, value["name"]))  # 添加到stackedWidget上
            self.treeWidget.addTopLevelItem(rootItem)
        
        # QTreeWidget绑定信号
        self.treeWidget.currentItemChanged.connect(self.router)
        
        
        # 创建布局
        self.layout = QHBoxLayout()
        # 将组件添加到布局中
        self.layout.addWidget(self.treeWidget)
        self.layout.addWidget(self.stackedWidget)

        # 为窗体添加布局
        self.centralwidget=QWidget()
        self.centralwidget.setLayout(self.layout)
        self.setCentralWidget(self.centralwidget)
        
        # 状态栏
        # a = QWidget()
        # b = QHBoxLayout()
        # # b.addStretch(8)
        # b.addWidget(QLabel("v1.0.0"))
        # a.setLayout(b)
        
        # llll = QLabel("v1.0.0")
        # b.addWidget(llll)
        self.statusbar = QStatusBar()
        # self.statusbar.addWidget(a)
        self.statusbar.showMessage("当前剩余次数: 10")
        self.setStatusBar(self.statusbar)
    
        # MainWindow的三个组件设置方法
        # setMenuBar(self.menubar)
        # setCentralWidget(self.centralwidget)
        # setStatusBar(self.statusbar)

    @Slot()
    def router(self, current, previous):
        # print(current, previous)
        # print(current.text(0))
        
        i = 0
        for k in self.menu_map:
            
            if current.text(0) == k:
                current.setExpanded(not current.isExpanded())  # TODO
            
            for key in self.menu_map[k]:
                if current.text(0) == key:
                    self.stackedWidget.setCurrentIndex(i)
                i += 1