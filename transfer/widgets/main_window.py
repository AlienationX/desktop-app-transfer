
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import qtawesome as qta

from transfer.widgets.mini_widgets.addons_widget import HContainer, VContainer, MaskWidget
from transfer.widgets.mini_widgets.prompt_box import MessageBox, ConfirmBox
from transfer.widgets.mini_widgets.menu_list import MenuList
from transfer.widgets.mini_widgets.settings_hierarchy import SettingsHierarchy

from transfer.widgets.main_frame import MainFrame
from transfer.utils.common import CommonHelper
from transfer.resources import resources_rc


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

        # 重点： 这个frame作为背景和圆角
        self.frame = QFrame()
        # shadow = QGraphicsDropShadowEffect(self, blurRadius=20, xOffset=5, yOffset=5, color=QColor(31, 31, 31))
        # self.frame.setGraphicsEffect(shadow)  # 只能在frame上设置阴影
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.frame)

        # 添加自定义样式
        theme = self.settings["theme"]
        if theme in ["light_theme", "dark_theme", "color_theme"]:
            qssStyle = CommonHelper.readQssResource(f":/styles/{theme}.css")  # 可以直接起名为css(其实是qss)
            self.setStyleSheet(qssStyle)
        
        self.mainVContainer = VContainer()
        self.mainVContainer.setSpacing(0)
        self.setHeader()
        self.mainFrame = MainFrame()
        self.mainVContainer.addWidget(self.mainFrame)
        self.setFooter()
        self.frame.setLayout(self.mainVContainer)
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
        
        # 绑定事件
        self.bind()
        
        self.setStyleSheet("""
            QWidget {
                border-radius: 5px;
                background-color: rgb(31, 31, 31);
                color: rgb(200, 200, 200);
                font-size: 12px;
            }
/* /////////////////////////////////////////////////////////////////////////////////////////////////
ScrollBars */
QScrollBar:horizontal {
    border: none;
    background: rgb(52, 59, 72);
    height: 8px;
    margin: 0px 21px 0 21px;
	border-radius: 0px;
}
QScrollBar::handle:horizontal {
    background: rgb(189, 147, 249);
    min-width: 25px;
	border-radius: 4px
}
QScrollBar::add-line:horizontal {
    border: none;
    background: rgb(55, 63, 77);
    width: 20px;
	border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal {
    border: none;
    background: rgb(55, 63, 77);
    width: 20px;
	border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}
QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {
    background: none;
}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}
QScrollBar:vertical {	
    border: none;
    background: rgb(52, 59, 72);
    width: 4px;
    margin: 0;	  /* 21px 0 21px 0;	中间外边距*/
    border-radius: 0px;
}
QScrollBar::handle:vertical {		
    background: rgb(189, 147, 249);
    min-height: 25px;	
    border-radius: 2px
}
QScrollBar::add-line:vertical {
    border: none;
    background: rgb(55, 63, 77);
    height: 0px;	/* 20px 上高度*/
    border-bottom-left-radius: 2px;
    border-bottom-right-radius: 2px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical {	
    border: none;
    background: rgb(55, 63, 77);
    height: 0px;    /* 20px 下高度*/
    border-top-left-radius: 2px;
    border-top-right-radius: 2px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}
QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
    background: none;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}
        """)
        self.headerHContainer.setStyleSheet("""
            QPushButton:hover {
                background-color: rgb(49, 50, 50);
            }
        """)
              
        
    def setHeader(self):
        # header
        self.headerHContainer = HContainer()
        # self.headerHContainer.setFixedHeight(44)
        self.headerHContainer.setContentsMargins(12, 6, 12, 6)
        self.logoLabel = QLabel()
        self.logoLabel.setPixmap(QPixmap(":/TransferS-title_black.png"))
        self.logoLabel.setFixedSize(120, 32)
        self.logoLabel.setScaledContents(True)  # 自适应
        
        self.logoTextLabel = QLabel()
        self.logoTextLabel.setText("TransferS")
        logoFont = QFont()
        logoFont.setBold(True)
        logoFont.setFamily("Segoe UI")
        logoFont.setPixelSize(40)
        self.logoTextLabel.setFont(logoFont)
        
        self.minBtn = QPushButton(qta.icon("msc.chrome-minimize", color=QColor(200, 200, 200)), "")
        self.minBtn.setObjectName("minBtn")
        self.minBtn.setToolTip("最小化")
        self.minBtn.setIconSize(QSize(20, 20))
        self.maxBtn = QPushButton(qta.icon("msc.chrome-maximize", color=QColor(200, 200, 200)), "")
        self.maxBtn.setObjectName("maxBtn")
        self.maxBtn.setToolTip("最大化")
        self.maxBtn.setIconSize(QSize(20, 20))
        self.closeBtn = QPushButton(qta.icon("msc.close", color=QColor(200, 200, 200)), "")
        self.closeBtn.setObjectName("closeBtn")
        self.closeBtn.setToolTip("关闭")
        self.closeBtn.setIconSize(QSize(20, 20))
        self.headerHContainer.addWidget(self.logoLabel)
        self.headerHContainer.addWidget(self.logoTextLabel)
        self.headerHContainer.addStretch()
        self.headerHContainer.addWidget(self.minBtn)
        self.headerHContainer.addWidget(self.maxBtn)
        self.headerHContainer.addWidget(self.closeBtn)
        self.mainVContainer.addWidget(self.headerHContainer)
        
        self.minBtn.clicked.connect(self.showMinimized)
        self.maxBtn.clicked.connect(self.changeMaxOrReset)
        self.closeBtn.clicked.connect(self.confirmClose)
    
    @Slot()
    def changeMaxOrReset(self):
        if self.isMaximized():
            self.maxBtn.setToolTip("最大化")
            self.maxBtn.setIcon(qta.icon("msc.chrome-maximize", color=QColor(200, 200, 200)))
            self.layout.setContentsMargins(6, 6, 6, 6)
            self.shadow = QGraphicsDropShadowEffect(self, blurRadius=10, xOffset=3, yOffset=3, color=Qt.black)
            self.frame.setGraphicsEffect(self.shadow)  # 只能在frame上设置阴影
            self.showNormal()
        else:
            self.maxBtn.setToolTip("还原")
            self.maxBtn.setIcon(qta.icon("msc.chrome-restore", color=QColor(200, 200, 200)))
            self.layout.setContentsMargins(0, 0, 0, 0)
            self.frame.setGraphicsEffect(None)  # 最大化无阴影，TODO 且都是直角
            self.showMaximized()
            
    def mouseDoubleClickEvent (self, event):
        # 实现双击标题栏最大化和还原
        if self.headerHContainer.underMouse():
            self.changeMaxOrReset()
        
    def mousePressEvent(self, event):
        # 实现鼠标拖拽功能，记录鼠标按下的时候的坐标，仅限标题栏支持拖拽移动
        if self.headerHContainer.underMouse():
            self.pressX = event.x()
            self.pressY = event.y()
 
    def mouseMoveEvent(self, event):
        if self.headerHContainer.underMouse():
            x = event.x()
            y = event.y()   # 获取移动后的坐标
            moveX = x - self.pressX
            moveY = y - self.pressY  # 计算移动了多少
    
            positionX = self.frameGeometry().x() + moveX
            positionY = self.frameGeometry().y() + moveY    # 计算移动后主窗口在桌面的位置
            self.move(positionX, positionY)    # 移动主窗口
            
    # def closeEvent(self, event):
    #     # 关闭程序弹出提示框确认
    #     reply = QMessageBox.question(self, 
    #                 "提示",
    #                 "是否要关闭所有窗口?",
    #                 QMessageBox.Yes | QMessageBox.No,
    #                 QMessageBox.No)
    #     if reply == QMessageBox.Yes:
    #         # event.accept()
    #         # sys.exit(0)   # 退出程序
    #         self.close()
    #     else:
    #         event.ignore()  # 一定要增加ignore，否则还是会关闭
    
    @Slot()
    def confirmClose(self):
        # 关闭程序弹出提示框确认，使用自定义的message_box
        self.confirm = ConfirmBox()
        self.confirm.set_title("Are you sure exit?")
        self.confirm.signal.connect(lambda x: self.confirmExit(x))
        self.confirm.show()
        
        
    @Slot()
    def confirmExit(self, reply_text):
        if reply_text == "OK": 
            self.close()
    
    def setFooter(self):
        # 自定义状态栏
        self.messageLable = QLabel("Welcome")
        self.versionLable = QLabel("Copyright © 2023 by shuli. All rights reserved.")
        self.statusHContainer = HContainer()
        # self.statusHContainer.setFixedHeight(30)
        self.statusHContainer.setContentsMargins(12, 6, 12, 6)
        self.statusHContainer.addWidget(self.messageLable)
        self.statusHContainer.addStretch()
        self.statusHContainer.addWidget(self.versionLable)
        self.mainVContainer.addWidget(self.statusHContainer)
    
    def bind(self):
        # TODO 给子组件的信号绑定处理函数
        childw1 = getattr(self.mainFrame, "ExcelToCsvWidget")
        childw1.message_signal.connect(lambda msg: self.print_status_message(msg))
        childw2 = getattr(self.mainFrame, "ExcelSplitWidget")
        childw2.message_signal.connect(lambda msg: self.print_status_message(msg))
       
    def print_status_message(self, msg):
        self.messageLable.setMaximumWidth(self.width() - self.versionLable.width() - 50)
        self.messageLable.setText(msg)
        self.messageLable.setToolTip(msg)
        
    def switch_theme(self, style_name):
        # self.setStyle(QStyleFactory.create(style_name))
        pass