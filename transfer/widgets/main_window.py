
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
from PySide6.QtCore import Slot, QSize, Qt
from PySide6.QtGui import QIcon, QPixmap
import qtawesome as qta

from widgets.excel_widget import ExcelToCsvWidget, ExcelSplitWidget
from widgets.csv_widget import CsvToExcelWidget
from widgets.word_widget import WordToPDFWidget
from widgets.document_widget import DocumentWidget
from resources import resources_rc


class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setupUi()
    
    def setupUi(self):
        """页面初始化"""
        # 设置窗体大小及标题
        self.resize(960, 500)
        self.setWindowTitle("TransferS - 转换工具")
        
        # self.setWindowIcon(QIcon(r"E:\Codes\Python\desktop-app-transfer\transfer\resources\icons\logo.ico"))
        # self.setWindowIcon(QIcon(r"transfer/resources/icons/logo.png"))  # png也是可以的
        # self.setWindowIcon(QIcon(":/logo.ico"))
        # self.setWindowIcon(QIcon(":/icons/8687850_ic_fluent_tag_regular_icon_48.png"))
        # logoIcon = qta.icon("msc.twitter")
        # self.setWindowIcon(logoIcon)
        
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint) # 隐藏边框并始终在其他窗口之上
        self.setWindowFlags(Qt.FramelessWindowHint) # 隐藏边框
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明
        
        self.centralLayout = QVBoxLayout()
        self.setHeader()
        self.setBody()
        self.setFooter()
        self.setLayout(self.centralLayout)
        
        # 为窗体添加布局
        # self.centralLayout = QVBoxLayout()
        # self.setHeader()
        # self.setBody()
        # self.setFooter()
        # self.centralWidget = QWidget()
        # self.centralWidget.setLayout(self.centralLayout)
        # self.setCentralWidget(self.centralWidget)
        
        # QStatusBar        
        # self.statusbar = QStatusBar()
        # label1 = QLabel("Welcome")
        # label2 = QLabel("CopyRight @ shuli.me 2023 v1.0.0")
        # # addWidget 在左侧添加临时控件
        # self.statusbar.addWidget(label1)
        # # addWidget 在右侧添加永久控件
        # self.statusbar.addPermanentWidget(label2)
        # self.setStatusBar(self.statusbar)
    
        # MainWindow的三个组件设置方法
        # setMenuBar(self.menubar)
        # setCentralWidget(self.centralwidget)
        # setStatusBar(self.statusbar)
        
    def setHeader(self):
        # header
        self.headerLayout = QHBoxLayout()
        self.logoLabel = QLabel("Logo.png")
        self.minBtn = QPushButton(qta.icon("msc.chrome-minimize"), "")
        self.maxBtn = QPushButton(qta.icon("msc.chrome-restore"), "")
        self.closeBtn = QPushButton(qta.icon("msc.chrome-close"), "")
        self.headerLayout.addWidget(self.logoLabel)
        self.headerLayout.addStretch()
        self.headerLayout.addWidget(self.minBtn)
        self.headerLayout.addWidget(self.maxBtn)
        self.headerLayout.addWidget(self.closeBtn)
        self.centralLayout.addLayout(self.headerLayout)
        
        self.minBtn.clicked.connect(self.showMinimized)
        self.maxBtn.clicked.connect(self.showMaximized)  # TODO 只能最大化，不能还原...
        self.closeBtn.clicked.connect(self.close) 
        
        
    def mousePressEvent(self, event):
        # 实现鼠标拖拽功能，记录鼠标按下的时候的坐标
        self.pressX = event.x()
        self.pressY = event.y()
 
    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()   # 获取移动后的坐标
        moveX = x - self.pressX
        moveY = y - self.pressY  # 计算移动了多少
 
        positionX = self.frameGeometry().x() + moveX
        positionY = self.frameGeometry().y() + moveY    # 计算移动后主窗口在桌面的位置
        self.move(positionX, positionY)    # 移动主窗口
        
    def setBody(self):
        # QTreeWidget组件定义
        self.treeWidget = QTreeWidget()
        self.treeWidget.header().setVisible(False)           # 隐藏标头
        # self.treeWidget.setStyleSheet("border:none;")        # 隐藏边框
        # self.treeWidget.headerItem().setText(0, "参数名")    # 给第1列设置标题
        # self.treeWidget.setColumnWidth(0, 200)               # 给第1列设置列宽200
        self.treeWidget.setMaximumSize(QSize(200, 16777215))
        
        # QTreeWidget组件内容设置
        self.menus = {
            "EXCEL": {
                "icon" : qta.icon("ri.file-excel-2-line"),
                "children" : [
                    {
                        "name" : "excelToCsvWidget",
                        "text" : "转换成CSV",
                        "icon" : qta.icon("msc.bookmark"),
                        "class": ExcelToCsvWidget()
                    },
                    {
                        "name" : "excelSplitWidget",
                        "text" : "文件拆分",
                        "icon" : qta.icon("msc.bookmark"),
                        "class": ExcelSplitWidget()
                    }
                ]},
            "WORD": {
                "icon" : qta.icon("ri.file-word-2-line"),
                "children" : [
                    {
                        "name" : "wordToPDFWidget",
                        "text" : "转换成PDF",
                        "icon" : qta.icon("msc.bookmark"),
                        "class": WordToPDFWidget(),
                    }
                ]
            },
            "CSV": {
                "icon" : qta.icon("fa5s.file-csv"),
                "children" : [
                    {
                        "name" : "csvToExcelWidget",
                        "text" : "转换成EXCEL",
                        "icon" : qta.icon("msc.bookmark"),
                        "class": CsvToExcelWidget(),
                    }
                ]
            },
        }
        
        self.homeItem = QTreeWidgetItem()
        self.homeItem.setText(0, "HOME")
        self.treeWidget.addTopLevelItem(self.homeItem)
        
        # 设置stackedWidget
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(DocumentWidget())  # 添加home主页显示
        
        for text in self.menus:
            rootItem = QTreeWidgetItem()
            rootItem.setText(0, text)
            rootItem.setIcon(0, self.menus[text]["icon"])
            for menu_list in self.menus[text]["children"]:
                childItem = QTreeWidgetItem()
                childItem.setText(0, menu_list["text"])
                childItem.setIcon(0, menu_list["icon"])
                rootItem.addChild(childItem)
                setattr(self, menu_list["name"], menu_list["class"])  # 把所有widget绑定到self上便于操作，但是也增加了内存消耗。可以优化在切换的时候创建
                self.stackedWidget.addWidget(getattr(self, menu_list["name"]))  # 添加到stackedWidget上
            self.treeWidget.addTopLevelItem(rootItem)
        
        # TODO 给子组件的信号绑定处理函数
        childw = getattr(self, "excelToCsvWidget")
        childw.message_signal.connect(lambda msg: self.print_message(msg))
        
        # QTreeWidget绑定信号
        self.treeWidget.itemClicked.connect(self.router)
        
        # 创建布局
        self.bodyLayout = QHBoxLayout()
        self.bodyLayout.addWidget(self.treeWidget)
        self.bodyLayout.addWidget(self.stackedWidget)
        self.centralLayout.addLayout(self.bodyLayout)
    
    def setFooter(self):
        # 自定义状态栏
        self.messageLable = QLabel("Welcome")
        self.versionLable = QLabel("CopyRight @ shuli.me 2023 v1.0.0")
        self.statusLayout = QHBoxLayout()
        self.statusLayout.addWidget(self.messageLable)
        self.statusLayout.addStretch()
        self.statusLayout.addWidget(self.versionLable)
        self.centralLayout.addLayout(self.statusLayout)

    @Slot()
    def router(self, item, column):
        print("menubar ==> ", item.text(0))
        if item.text(0) == "HOME":
            self.stackedWidget.setCurrentIndex(0)
            return
        
        i = 1
        for text in self.menus:
            # 如果等于一级节点则展开
            if item.text(0) == text:
                item.setExpanded(not item.isExpanded())
            # 如果等于二级节点则切换页面
            for menu_list in self.menus[text]["children"]:
                if item.text(0) == menu_list["text"]:
                    self.stackedWidget.setCurrentIndex(i)
                    return
                i += 1
    
    def print_message(self, msg):
        self.statusbar.showMessage(msg)
        self.statusbar.setToolTip(msg)