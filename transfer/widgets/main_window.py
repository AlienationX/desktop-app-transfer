
from PySide6.QtWidgets import *
from PySide6.QtCore import Slot, QSize, Qt, QRect
from PySide6.QtGui import QIcon, QPixmap, QColor
import qtawesome as qta

from .mini_widgets.addons_widget import HContainer, VContainer
from .mini_widgets.message_box import MessageBox

from . pages import ExcelToCsvWidget, ExcelSplitWidget, ExcelOverviewWidget, CsvToExcelWidget, WordToPDFWidget, DocumentWidget

from .main_ui import Ui_Transfer
from utils.common import CommonHelper
from resources import resources_rc


class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setObjectName("main")
        
        self.settings = {
            "is_vip": False,
            "is_radius": False,
            "theme": "light1_theme",  # system_theme, light_theme, dark_theme, color_theme
        }
        
        self.setupUi()
        self.ui = Ui_Transfer()
        self.ui.setupUi(self)
        self.bind()
    
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
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明

        # 重点： 这个widget作为背景和圆角
        self.widget = QWidget(self)
        self.widget.setObjectName("backgroundWidget")
        _layout = QVBoxLayout(self)
        _layout.setContentsMargins(0, 0, 0, 0)
        _layout.addWidget(self.widget)

        # 添加自定义样式
        theme = self.settings["theme"]
        if theme in ["light_theme", "dark_theme", "color_theme"]:
            qssStyle = CommonHelper.readQssResource(f":/styles/{theme}.css")  # 可以直接起名为css(其实是qss)
            self.setStyleSheet(qssStyle)
        
        self.mainVContainer = VContainer()
        self.mainVContainer.setSpacing(0)
        self.setHeader()
        self.setBody()
        self.setFooter()
        self.widget.setLayout(self.mainVContainer)
        # self.setContentsMargins(0, 0, 0, 0)
        
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
    
        
    def bind(self):
        pass 
        # TODO 给子组件的信号绑定处理函数
        childw1 = getattr(self, "ExcelToCsvWidget")
        childw1.message_signal.connect(lambda msg: self.print_message(msg))
        childw2 = getattr(self, "ExcelSplitWidget")
        childw2.message_signal.connect(lambda msg: self.print_message(msg))
        
        # QListWidget绑定信号
        self.menuList.listWidget.currentRowChanged.connect(self.router)
        
        self.hideMenuBtn.clicked.connect(self.hide_menu)
        
        self.x.clicked.connect(self.settingsVContainer.hide)
        
        self.msgBtn.clicked.connect(self.showMessage)
        self.settingsBtn.clicked.connect(self.settingsVContainer.show)
        