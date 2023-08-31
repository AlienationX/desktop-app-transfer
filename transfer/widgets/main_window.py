
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QMessageBox,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QTreeWidget,
    QListWidget,
    QListWidgetItem,
    QTreeWidgetItem,
    
    QStatusBar,
    QStackedWidget
)
from PySide6.QtCore import Slot, QSize, Qt
from PySide6.QtGui import QIcon, QPixmap
import qtawesome as qta

from .excel_widget import ExcelToCsvWidget, ExcelSplitWidget
from .csv_widget import CsvToExcelWidget
from .word_widget import WordToPDFWidget
from .document_widget import DocumentWidget
from utils.common import CommonHelper
from resources import resources_rc


class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.settings = {
            "is_vip": False,
            "is_maximized": False,
            "theme": "light_theme",
        }
        
        self.setupUi()
    
    def setupUi(self):
        """页面初始化"""
        # 设置窗体大小及标题
        self.resize(960, 500)
        self.setWindowTitle("TransferS - 转换工具")
        self.setWindowIconText("Transfer")
        
        # self.setWindowIcon(QIcon(r"E:\Codes\Python\desktop-app-transfer\transfer\resources\icons\logo.ico"))
        # self.setWindowIcon(QIcon(r"transfer/resources/icons/logo.png"))  # png也是可以的
        # self.setWindowIcon(QIcon(":/logo.ico"))
        # self.setWindowIcon(QIcon(":/icons/8687850_ic_fluent_tag_regular_icon_48.png"))
        # logoIcon = qta.icon("msc.twitter")
        # self.setWindowIcon(logoIcon)
        
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint) # 隐藏边框并始终在其他窗口之上
        self.setWindowFlags(Qt.FramelessWindowHint) # 隐藏边框
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明

        # 添加自定义样式
        theme = self.settings["theme"]
        qssStyle = CommonHelper.readQssResource(f":/styles/{theme}.css")  # 可以直接起名为css(其实是qss)
        self.setStyleSheet(qssStyle)
        
        self.centralLayout = QVBoxLayout()
        self.centralLayout.setContentsMargins(0, 5, 0, 5)
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
        self.headerLayout.setContentsMargins(5, 0, 5, 0)
        self.logoLabel = QLabel()
        self.logoLabel.setPixmap(QPixmap(":/TransferS-title_461x116.png"))
        self.logoLabel.setFixedSize(120, 32)
        self.logoLabel.setScaledContents(True)
        self.minBtn = QPushButton(qta.icon("msc.chrome-minimize"), "")
        self.maxBtn = QPushButton(qta.icon("msc.collapse-all"), "")
        self.closeBtn = QPushButton(qta.icon("msc.close"), "")
        self.minBtn.setObjectName("minBtn")
        self.maxBtn.setObjectName("maxBtn")
        self.closeBtn.setObjectName("closeBtn")
        self.headerLayout.addWidget(self.logoLabel)
        self.headerLayout.addStretch()
        self.headerLayout.addWidget(self.minBtn)
        self.headerLayout.addWidget(self.maxBtn)
        self.headerLayout.addWidget(self.closeBtn)
        self.centralLayout.addLayout(self.headerLayout)
        
        self.minBtn.clicked.connect(self.showMinimized)
        self.maxBtn.clicked.connect(self.changeMaxOrReset)  # TODO 只能最大化，不能还原...
        self.closeBtn.clicked.connect(self.close) 
    
    def changeMaxOrReset(self):
        if not self.settings["is_maximized"]:
            self.showMaximized()
            self.settings["is_maximized"] = True
        else:
            self.showNormal()
            self.settings["is_maximized"] = False
        
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
        self.listWidget = QListWidget()
        self.listWidget.setMaximumWidth(200)
        self.menus = [
            {"id": 0, "objectName": "home", "text": "HOME", "icon": "mdi.menu-open", "class": DocumentWidget(), "level": 1},
            {"id": 1, "objectName": "excel", "text": "EXCEL", "icon": "ri.file-excel-2-line", "class": "", "level": 1},
            {"id": 2, "objectName": "ExcelToCsvWidget", "text": "转换成CSV", "icon": "msc.bookmark", "class": ExcelToCsvWidget(), "level": 2},
            {"id": 3, "objectName": "ExcelSplitWidget", "text": "文件拆分", "icon": "msc.bookmark", "class": ExcelSplitWidget(), "level": 2},
            {"id": 4, "objectName": "excel_todo1", "text": "数据概况", "icon": "msc.bookmark", "class": "", "level": 2},
            {"id": 5, "objectName": "work", "text": "WORD", "icon": "ri.file-word-2-line", "class": "", "level": 1},
            {"id": 6, "objectName": "WordToPDFWidget", "text": "转换成PDF", "icon": "msc.bookmark", "class": WordToPDFWidget(), "level": 2},
            {"id": 7, "objectName": "csv", "text": "CSV", "icon": "msc.go-to-file", "class": "", "level": 1},
            {"id": 8, "objectName": "CsvToExcelWidget", "text": "转换成EXCEL", "icon": "msc.bookmark", "class": CsvToExcelWidget(), "level": 2},
            {"id": 9, "objectName": "file", "text": "FILE", "icon": "msc.go-to-file", "class": "", "level": 1},
            {"id": 10, "objectName": "file_todo1", "text": "批量重命名", "icon": "msc.bookmark", "class": "", "level": 2},
        ]
        
        # 设置stackedWidget
        self.stackedWidget = QStackedWidget()
        
        for i in range(len(self.menus)):
            item = self.menus[i]
            list_item = QListWidgetItem(item["text"])
            list_item.setIcon(qta.icon(item["icon"]))
            self.listWidget.addItem(list_item)
            setattr(self, item["objectName"], item["class"])  # 把所有widget绑定到self上便于操作，但是也增加了内存消耗。可以优化在切换的时候创建
            if item["class"]:
                self.stackedWidget.addWidget(getattr(self, item["objectName"]))  # 添加到stackedWidget上
        
        # TODO 给子组件的信号绑定处理函数
        childw = getattr(self, "ExcelToCsvWidget")
        childw.message_signal.connect(lambda msg: self.print_message(msg))
        
        # QListWidget绑定信号
        self.listWidget.currentTextChanged.connect(self.router)
        
        # 创建布局
        self.bodyLayout = QHBoxLayout()
        self.bodyLayout.setSpacing(0)
        self.bodyLayout.addWidget(self.listWidget)
        self.bodyLayout.addWidget(self.stackedWidget)
        self.centralLayout.addLayout(self.bodyLayout)
        
    @Slot()
    def router(self, currentText):
        print("menubar ==> ", currentText)
        
        for i in range(len(self.menus)):
            item = self.menus[i]
            if currentText == item["text"] and item["class"]:
                self.stackedWidget.setCurrentWidget(getattr(self, item["objectName"]))
                return
    
    
    def setFooter(self):
        # 自定义状态栏
        self.messageLable = QLabel("Welcome")
        self.versionLable = QLabel("CopyRight @ shuli.me 2023 v1.0.0")
        self.statusLayout = QHBoxLayout()
        self.statusLayout.setContentsMargins(5, 0, 5, 0)
        self.statusLayout.addWidget(self.messageLable)
        self.statusLayout.addStretch()
        self.statusLayout.addWidget(self.versionLable)
        self.centralLayout.addLayout(self.statusLayout)
        
    
    def showMessage(self):
        """弹出信息"""
        pass

    def print_message(self, msg):
        self.messageLable.setMaximumWidth(self.width() - 200)
        self.messageLable.setText(msg)
        self.messageLable.setToolTip(msg)