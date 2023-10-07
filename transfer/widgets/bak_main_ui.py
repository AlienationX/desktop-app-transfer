from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import qtawesome as qta

from transfer.widgets.mini_widgets.addons_widget import HContainer, VContainer
from transfer.widgets.mini_widgets.prompt_box import MessageBox
from transfer.widgets.mini_widgets.menu_list import MenuList

from transfer.utils.common import CommonHelper
from transfer.resources import resources_rc

class Ui_Transfer(QWidget):
    
    def __init__(self, parent):
        super().__init__(parent)

    
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
        self.parent().setWindowFlags(Qt.FramelessWindowHint) # 隐藏边框
        self.parent().setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明

        # 重点： 这个frame作为背景和圆角
        self.frame = QFrame()
        self.frame.setObjectName("backgroundFrame")
        # shadow = QGraphicsDropShadowEffect(self, blurRadius=20, xOffset=5, yOffset=5, color=QColor(31, 31, 31))
        # self.frame.setGraphicsEffect(shadow)  # 只能在frame上设置阴影
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.frame)

        # 添加自定义样式
        # theme = self.settings["theme"]
        # if theme in ["light_theme", "dark_theme", "color_theme"]:
        #     qssStyle = CommonHelper.readQssResource(f":/styles/{theme}.css")  # 可以直接起名为css(其实是qss)
        #     self.setStyleSheet(qssStyle)
        
        self.mainVContainer = VContainer()
        self.mainVContainer.setSpacing(0)
        self.setHeader()
        self.setBody()
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
        
        self.setStyleSheet("""
            QWidget {
                border-radius: 5px;
                background-color: rgb(31, 31, 31);
                color: rgb(200, 200, 200);
                font-size: 13px;
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
    width: 8px;
    margin: 0;	  /* 21px 0 21px 0;	中间外边距*/
    border-radius: 0px;
}
QScrollBar::handle:vertical {		
    background: rgb(189, 147, 249);
    min-height: 25px;	
    border-radius: 4px
}
QScrollBar::add-line:vertical {
    border: none;
    background: rgb(55, 63, 77);
    height: 0px;	/* 20px 上高度*/
    border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical {	
    border: none;
    background: rgb(55, 63, 77);
    height: 0px;    /* 20px 下高度*/
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
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
        self.menuVContainer.setStyleSheet("""
            QPushButton:hover {
                background-color: rgb(49, 50, 50);
            }
        """)
        self.stackedWidget.setStyleSheet("""
            QStackedWidget {
                border-radius: 0px;
                background-color: rgb(51, 51, 51);
            }
            QStackedWidget QWidget {
                border-radius: 3px;
                padding: 4px 10px;
            }
            QPushButton {
                background-color: rgb(51, 118, 205);
            }
            QPushButton:hover {
                background-color: rgb(47, 108, 187);
            }
        """)
        
        
    def setHeader(self):
        # header
        self.headerHContainer = HContainer()
        self.headerHContainer.setContentsMargins(12, 6, 12, 6)
        self.logoLabel = QLabel()
        self.logoLabel.setPixmap(QPixmap(":/TransferS-title_black.png"))
        self.logoLabel.setFixedSize(120, 32)
        self.logoLabel.setScaledContents(True)  # 自适应
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
        self.headerHContainer.addStretch()
        self.headerHContainer.addWidget(self.minBtn)
        self.headerHContainer.addWidget(self.maxBtn)
        self.headerHContainer.addWidget(self.closeBtn)
        self.mainVContainer.addWidget(self.headerHContainer)
        
        self.minBtn.clicked.connect(self.showMinimized)
        self.maxBtn.clicked.connect(self.changeMaxOrReset)
        self.closeBtn.clicked.connect(self.close) 
    
    @Slot()
    def changeMaxOrReset(self):
        if self.isMaximized():
            self.maxBtn.setToolTip("最大化")
            self.maxBtn.setIcon(qta.icon("msc.chrome-maximize", color=QColor(200, 200, 200)))
            # self.layout.setContentsMargins(6, 6, 6, 6)
            # self.shadow = QGraphicsDropShadowEffect(self, blurRadius=10, xOffset=5, yOffset=5, color=QColor(31, 31, 31))
            # self.frame.setGraphicsEffect(self.shadow)  # 只能在frame上设置阴影
            self.showNormal()
        else:
            self.maxBtn.setToolTip("还原")
            self.maxBtn.setIcon(qta.icon("msc.chrome-restore", color=QColor(200, 200, 200)))
            # self.layout.setContentsMargins(0, 0, 0, 0)
            # self.frame.setGraphicsEffect(None)  # 最大化无阴影
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
            
        
    def setBody(self):
        
        self.menuList = MenuList()
        self.menuList.setMinimumWidth(230)
        self.menuList.setMaximumWidth(300)
        self.stackedWidget = QStackedWidget()
         
        for i in range(len(self.menuList.menus)):        
            menu_item = self.menuList.menus[i]
            setattr(self, menu_item["objectName"], menu_item["class"])  # 把所有widget绑定到self上便于操作，但是也增加了内存消耗。可以优化在切换的时候创建
            if menu_item["class"]:
                self.stackedWidget.addWidget(getattr(self, menu_item["objectName"]))  # 添加到stackedWidget上
        
        
        # 底部的按钮
        self.extendHContainer = HContainer()
        self.msgBtn = QPushButton()  # 弹出设置窗口，挤走部件  # 弹出消息窗口，遮罩
        self.msgBtn.setIcon(qta.icon("msc.comment", color=QColor(200, 200, 200)))
        self.msgBtn.setIconSize(QSize(20, 20))
        
        self.settingsBtn = QPushButton(qta.icon("msc.settings-gear", color=QColor(200, 200, 200)), "")
        self.settingsBtn.setIconSize(QSize(20, 20))
        self.settingsBtn.setToolTip("设置")

        self.helpBtn = QPushButton(qta.icon("mdi.help-circle-outline", color=QColor(200, 200, 200)), "")
        self.helpBtn.setIconSize(QSize(20, 20))
        self.helpBtn.setToolTip("帮助")
        
        self.ellipsisBtn = QPushButton(qta.icon("msc.ellipsis", color=QColor(200, 200, 200)), "")
        self.ellipsisBtn.setIconSize(QSize(20, 20))
        self.ellipsisMenu = QMenu()
        self.ellipsisMenu.addAction(qta.icon("msc.feedback", color=QColor(200, 200, 200)), "Feedback")  # 反馈
        self.ellipsisMenu.addAction(qta.icon("mdi.math-log", color=QColor(200, 200, 200)), "UpdateLog")  # 更新日志
        self.ellipsisMenu.addAction(qta.icon("ph.snapchat-logo", color=QColor(200, 200, 200)), "About")  # 关于
        self.ellipsisBtn.setMenu(self.ellipsisMenu)  # 增加弹出按钮菜单
        self.ellipsisBtn.setToolTip("其他功能按钮")
    
        self.hideMenuBtn = QPushButton(qta.icon("fa.angle-double-left", color=QColor(200, 200, 200)), "")
        self.hideMenuBtn.setIconSize(QSize(16, 16))
        self.hideMenuBtn.setToolTip("隐藏菜单栏")
        
        
        self.extendHContainer.addWidget(self.msgBtn)
        self.extendHContainer.addWidget(self.settingsBtn)
        self.extendHContainer.addWidget(self.helpBtn)
        self.extendHContainer.addWidget(self.ellipsisBtn)
        self.extendHContainer.addStretch()
        self.extendHContainer.addWidget(self.hideMenuBtn)
        
        # 创建布局
        self.menuVContainer = VContainer()
        self.menuVContainer.setObjectName("menuVContainer")
        
        self.menuVContainer.setMaximumWidth(240)
        self.menuVContainer.addWidget(self.menuList)
        self.menuVContainer.addWidget(self.extendHContainer)

        self.settingsVContainer = VContainer()
        self.x = QPushButton("pushbutton")
        self.settingsVContainer.addWidget(self.x)
        self.settingsVContainer.hide()
        
        self.bodyHContainer = HContainer()
        self.bodyHContainer.setContentsMargins(12, 0, 12, 0)
        self.bodyHContainer.setSpacing(0)
        self.bodyHContainer.addWidget(self.menuVContainer)
        self.bodyHContainer.addWidget(self.stackedWidget)
        # self.bodyHContainer.addWidget(self.settingsVContainer)
        self.mainVContainer.addWidget(self.bodyHContainer)
        # self.centralLayout.addLayout(self.headerLaylout)  # 其实可以添加多个布局，但是就无法修改背景色等
        # self.centralLayout.addLayout(self.bodyLaylout)    # 其实可以添加多个布局，但是就无法修改背景色等
        # self.centralLayout.addLayout(self.footerLaylout)  # 其实可以添加多个布局，但是就无法修改背景色等
        
    
    def setFooter(self):
        # 自定义状态栏
        self.messageLable = QLabel("Welcome")
        self.versionLable = QLabel("Copyright © 2023 by shuli. All rights reserved.")
        self.statusHContainer = HContainer()
        self.statusHContainer.setContentsMargins(12, 6, 12, 6)
        self.statusHContainer.addWidget(self.messageLable)
        self.statusHContainer.addStretch()
        self.statusHContainer.addWidget(self.versionLable)
        self.mainVContainer.addWidget(self.statusHContainer)
        print("statusbar", self.messageLable.width())
        print("versionLable", self.versionLable.width())
        print("statusHContainer", self.statusHContainer.width())
    
        
if __name__ == "__main__":
    class MainWindow(QWidget):
    
        def __init__(self):
            super().__init__()

            # 设置窗体大小及标题
            self.resize(960, 500)
            self.setWindowTitle("TransferS - 转换工具")
            self.setWindowIconText("Transfer")
            
            self.ui = Ui_Transfer(self)
            self.ui.setupUi()
        
    import sys
    app = QApplication(sys.argv)  # 支持命令行启动传参，提高可扩展性
    window = MainWindow()
    window.show()
    sys.exit(app.exec())