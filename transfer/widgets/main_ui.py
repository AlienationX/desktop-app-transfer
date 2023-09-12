from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import qtawesome as qta

from transfer.widgets.mini_widgets.addons_widget import HContainer, VContainer
from transfer.widgets.mini_widgets.message_box import MessageBox
from transfer.widgets.excel_to_csv_page import ExcelToCsvWidget
from transfer.widgets.excel_split_page import ExcelSplitWidget
# from .excel_overvire_page import ExcelOverviewWidget
from transfer.widgets.csv_page import CsvToExcelWidget
from transfer.widgets.word_page import WordToPDFWidget
from transfer.widgets.document_page import DocumentWidget
from transfer.utils.common import CommonHelper
from transfer.resources import resources_rc

class Ui_Transfer:
    
    def setupUi(self, parent):
        
        # self.setWindowIcon(QIcon(r"E:\Codes\Python\desktop-app-transfer\transfer\resources\icons\logo.ico"))
        # self.setWindowIcon(QIcon(r"transfer/resources/icons/logo.png"))  # png也是可以的
        # self.setWindowIcon(QIcon(":/logo.ico"))
        # self.setWindowIcon(QIcon(":/icons/8687850_ic_fluent_tag_regular_icon_48.png"))
        # logoIcon = qta.icon("msc.twitter")
        # self.setWindowIcon(logoIcon)
        
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint) # 隐藏边框并始终在其他窗口之上
    
        # 重点： 这个widget作为背景和圆角
        self.widget = QWidget()
        self.widget.setObjectName("backgroundWidget")
        _layout = QVBoxLayout(parent)
        _layout.setContentsMargins(0, 0, 0, 0)
        _layout.addWidget(self.widget)

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
        
        self.setStyleSheet("""
            QWidget {
                border-radius: 5px;
                background-color: rgb(31, 31, 31);
                color: rgb(200, 200, 200);
            }
        """)
        self.headerHContainer.setStyleSheet("""
            QPushButton:hover {
                background-color: rgb(49, 50, 50);
            }
        """)
        # self.bodyHContainer.setStyleSheet("""
        #     QWidget {
        #         border-radius: 0px;
        #         background-color: rgb(41, 41, 41);
        #         color: rgb(200, 200, 200);
        #     }
        # """)
        # QListWidget和QListWidgetItem都不继承QWidget，所以需要单独配置
        self.menuVContainer.setStyleSheet("""
            QListView {
                outline: none;  /* 禁用被选中的虚线 */
            }
            QListView::item:hover {
                background-color: green;
            }
            QListView::item:selected {
                border-left: 5px solid red;
                background-color: orange;
            }
            QListView QWidget {
                background-color: transparent;  /* 重点，设置为透明 */
            }
        """)
        
        self.stackedWidget.setStyleSheet("""
            QStackedWidget {
                background-color: rgb(51, 51, 51);
            }
            QWidget {
                border-radius: 3px;
            }
            QPushButton {
                background-color: rgb(0, 120, 212);
                padding: 3px 10px;
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
        self.maxBtn = QPushButton(qta.icon("msc.collapse-all", color=QColor(200, 200, 200)), "")
        self.closeBtn = QPushButton(qta.icon("msc.close", color=QColor(200, 200, 200)), "")
        self.minBtn.setObjectName("minBtn")
        self.minBtn.setToolTip("最小化")
        self.maxBtn.setObjectName("maxBtn")
        self.maxBtn.setToolTip("最大化")
        self.closeBtn.setObjectName("closeBtn")
        self.closeBtn.setToolTip("关闭")
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
            self.showNormal()
            self.maxBtn.setToolTip("最大化")
        else:
            self.showMaximized()
            self.maxBtn.setToolTip("还原")
            
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
        self.listWidget = QListWidget()
        self.listWidget.setObjectName("leftMenu")
        self.menus = [
            {"id": 0, "objectName": "home", "text": "HOME", "icon": "mdi.menu-open", "class": DocumentWidget(), "level": 1},
            {"id": 1, "objectName": "excel", "text": "EXCEL", "icon": "ri.file-excel-2-line", "class": "", "level": 1},
            {"id": 2, "objectName": "ExcelToCsvWidget", "text": "转换成CSV", "icon": "msc.bookmark", "class": ExcelToCsvWidget(), "level": 2},
            {"id": 3, "objectName": "ExcelSplitWidget", "text": "文件拆分", "icon": "msc.bookmark", "class": ExcelSplitWidget(), "level": 2},
            # {"id": 4, "objectName": "ExcelOverviewWidget", "text": "数据概况", "icon": "msc.bookmark", "class": ExcelOverviewWidget(), "level": 2},
            {"id": 5, "objectName": "work", "text": "WORD", "icon": "ri.file-word-2-line", "class": "", "level": 1},
            {"id": 6, "objectName": "WordToPDFWidget", "text": "转换成PDF", "icon": "msc.bookmark", "class": WordToPDFWidget(), "level": 2},
            {"id": 7, "objectName": "csv", "text": "CSV", "icon": "msc.go-to-file", "class": "", "level": 1},
            {"id": 8, "objectName": "CsvToExcelWidget", "text": "转换成EXCEL", "icon": "msc.bookmark", "class": CsvToExcelWidget(), "level": 2},
            {"id": 9, "objectName": "file", "text": "FILE", "icon": "msc.go-to-file", "class": "", "level": 1},
            {"id": 10, "objectName": "file_todo1", "text": "批量重命名", "icon": "msc.bookmark", "class": "", "level": 2},
            # {"id": 10, "objectName": "file_todo1", "text": "批量重命名", "icon": "msc.bookmark", "class": "", "level": 2},
            # {"id": 10, "objectName": "file_todo1", "text": "批量重命名", "icon": "msc.bookmark", "class": "", "level": 2},
            # {"id": 10, "objectName": "file_todo1", "text": "批量重命名", "icon": "msc.bookmark", "class": "", "level": 2},
            # {"id": 10, "objectName": "file_todo1", "text": "批量重命名", "icon": "msc.bookmark", "class": "", "level": 2},
            # {"id": 10, "objectName": "file_todo1", "text": "批量重命名", "icon": "msc.bookmark", "class": "", "level": 2},
            # {"id": 10, "objectName": "file_todo1", "text": "批量重命名", "icon": "msc.bookmark", "class": "", "level": 2},
            # {"id": 10, "objectName": "file_todo1", "text": "批量重命名", "icon": "msc.bookmark", "class": "", "level": 2},
            # {"id": 10, "objectName": "file_todo1", "text": "批量重命名", "icon": "msc.bookmark", "class": "", "level": 2},
            # {"id": 10, "objectName": "file_todo1", "text": "批量重命名", "icon": "msc.bookmark", "class": "", "level": 2},
            # {"id": 10, "objectName": "file_todo1", "text": "批量重命名", "icon": "msc.bookmark", "class": "", "level": 2},
            # {"id": 10, "objectName": "file_todo1", "text": "批量重命名", "icon": "msc.bookmark", "class": "", "level": 2},
        ]
        
        # 设置stackedWidget
        self.stackedWidget = QStackedWidget()
        
        for i in range(len(self.menus)):
            item = self.menus[i]
            # list_item = QListWidgetItem(item["text"])
            # list_item.setIcon(qta.icon(item["icon"]))
            # self.listWidget.addItem(list_item)
            
            list_item = QListWidgetItem()
            list_item.setSizeHint(QSize(200, 36))  # 必须设置大小，否则显示不出来

            leftIcon = QLabel()
            leftIcon.setPixmap(qta.icon(item["icon"], color=QColor(200, 200, 200)).pixmap(QSize(20, 20)))
            # leftIcon.setPixmap(QPixmap(":/logo2.ico"))
            rightIcon = QLabel()
            # rightIcon.setPixmap(QPixmap(":/icons/24.svg"))
            # rightIcon.setPixmap(QIcon(":/icons/24.svg").pixmap(QSize(16, 16)))
            rightIcon.setPixmap(qta.icon("msc.chevron-down", color=QColor(200, 200, 200)).pixmap(QSize(20, 20)))
            # rightIcon.setScaledContents(True)  # 自适应
            # rightIcon.setFixedSize(QSize(16, 16))
            
            # listWidgetHContainer = HContainer()
            # listWidgetHContainer.addWidget(leftIcon)
            # listWidgetHContainer.addWidget(QLabel(item["text"]))
            # listWidgetHContainer.addStretch()
            # listWidgetHContainer.addWidget(rightIcon)
            
            listWidgetHContainer = QWidget()
            listWidgetHLayout = QHBoxLayout(listWidgetHContainer)
            listWidgetHLayout.addWidget(leftIcon)
            listWidgetHLayout.addWidget(QLabel(item["text"]))
            listWidgetHLayout.addStretch()
            listWidgetHLayout.addWidget(rightIcon)
            
            self.listWidget.addItem(list_item)
            self.listWidget.setItemWidget(list_item, listWidgetHContainer)  # addItem 和 setItemWidget 必须一起使用
            
            setattr(self, item["objectName"], item["class"])  # 把所有widget绑定到self上便于操作，但是也增加了内存消耗。可以优化在切换的时候创建
            if item["class"]:
                self.stackedWidget.addWidget(getattr(self, item["objectName"]))  # 添加到stackedWidget上
        
        # TODO 给子组件的信号绑定处理函数
        childw1 = getattr(self, "ExcelToCsvWidget")
        childw1.message_signal.connect(lambda msg: self.print_message(msg))
        childw2 = getattr(self, "ExcelSplitWidget")
        childw2.message_signal.connect(lambda msg: self.print_message(msg))
        
        # QListWidget绑定信号
        self.listWidget.currentRowChanged.connect(self.router)
        
        # 底部的按钮
        self.msgBtn = QPushButton("Show Message")  # TODO 弹出消息窗口，遮罩
        
        self.settingsBtn = QPushButton("Settings")  # TODO 弹出设置窗口，挤走部件
        self.settingsBtn.setObjectName("settings")
        
        # 创建布局
        self.menuVContainer = VContainer()
        
        self.menuVContainer.setMaximumWidth(240)
        self.menuVContainer.addWidget(self.listWidget)
        self.menuVContainer.addWidget(self.msgBtn)
        self.menuVContainer.addWidget(self.settingsBtn)

        self.settingsVContainer = VContainer()
        self.x = QPushButton("x")
        self.x.clicked.connect(self.settingsVContainer.hide)
        self.settingsVContainer.addWidget(self.x)
        self.settingsVContainer.hide()
        
        self.bodyHContainer = HContainer()
        self.bodyHContainer.setContentsMargins(12, 0, 12, 0)
        self.bodyHContainer.setSpacing(0)
        self.bodyHContainer.addWidget(self.menuVContainer)
        self.bodyHContainer.addWidget(self.settingsVContainer)
        self.bodyHContainer.addWidget(self.stackedWidget)
        self.mainVContainer.addWidget(self.bodyHContainer)
        # self.centralLayout.addLayout(self.headerLaylout)  # 其实可以添加多个布局，但是就无法修改背景色等
        # self.centralLayout.addLayout(self.bodyLaylout)    # 其实可以添加多个布局，但是就无法修改背景色等
        # self.centralLayout.addLayout(self.footerLaylout)  # 其实可以添加多个布局，但是就无法修改背景色等

        self.msgBtn.clicked.connect(self.showMessage)
        self.settingsBtn.clicked.connect(self.settingsVContainer.show)
        
    @Slot()
    def router(self, currentRow):
        print("menubar ==> ", currentRow)
        
        for i in range(len(self.menus)):
            item = self.menus[i]
            if currentRow == i and item["class"]:
                self.stackedWidget.setCurrentWidget(getattr(self, item["objectName"]))
                return
    
    
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
        
    
    def showMessage(self):
        """弹出信息"""
        self.messageBox = MessageBox()
        self.messageBox.setTitle("Message")
        print(self.messageBox.width(), self.messageBox.height())
        x = self.geometry().right() - self.messageBox.width()
        y = self.geometry().bottom() - self.messageBox.height()
        self.messageBox.move(x, y)
        self.messageBox.show()

    def print_message(self, msg):
        print("==============>", self.width())
        self.messageLable.setMaximumWidth(self.width() - 220)  # TODO 名称太长会改变窗体大小
        self.messageLable.setText(msg)
        self.messageLable.setToolTip(msg)
        
        # 增加样式
        self.setStyle()
        
    def bind(self):
        pass
        
    def setStyle(self):
        # 添加自定义样式
        # theme = parent.settings["theme"]
        # if theme in ["light_theme", "dark_theme", "color_theme"]:
        #     qssStyle = CommonHelper.readQssResource(f":/styles/{theme}.css")  # 可以直接起名为css(其实是qss)
        #     self.setStyleSheet(qssStyle)
        pass
    
    def setLightStyle(self):
        pass
    
    def setDarkStype(self):
        pass
    
        
if __name__ == "__main__":
    class MainWindow(QWidget):
    
        def __init__(self):
            super().__init__()

            # 设置窗体大小及标题
            self.resize(960, 500)
            self.setWindowTitle("TransferS - 转换工具")
            self.setWindowIconText("Transfer")
            
            self.ui = Ui_Transfer()
            self.ui.setupUi(self)
        
    import sys
    app = QApplication(sys.argv)  # 支持命令行启动传参，提高可扩展性
    window = MainWindow()
    window.show()
    sys.exit(app.exec())