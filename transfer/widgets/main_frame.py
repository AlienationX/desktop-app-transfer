from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import qtawesome as qta

from transfer.widgets.mini_widgets import HContainer, VContainer, MaskWidget, MenuList, MessageBox, SettingsHierarchy
import sys

class MainFrame(QWidget):
    
    """主窗口"""
    
    def __init__(self):
        super().__init__()
        
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(12, 0, 12, 0)
        self.layout.setSpacing(0)
        
        self.menuList = MenuList()
        self.stackedWidget = QStackedWidget()
         
        for i in range(len(self.menuList.menus)):        
            menu_item = self.menuList.menus[i]
            setattr(self, menu_item["objectName"], menu_item["class"])  # TODO 把所有widget绑定到self上便于操作，但是也增加了内存消耗。可以优化在切换的时候创建，但是无法保证stackedWidget的顺序
            if menu_item["class"]:
                self.stackedWidget.addWidget(getattr(self, menu_item["objectName"]))  # 添加到stackedWidget上
        
        # 底部的按钮
        self.extendHContainer = HContainer()
        # self.extendHContainer.setContentsMargins(0, 0, 0, 0)
        self.msgBtn = QPushButton()  # TODO 测试
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
        self.ellipsisBtn.setMenu(self.ellipsisMenu)  # TODO 增加样式
        self.ellipsisBtn.setToolTip("其他功能按钮")
    
        self.hideMenuBtn = QPushButton(qta.icon("fa.angle-double-left", color=QColor(200, 200, 200)), "")
        self.hideMenuBtn.setIconSize(QSize(20, 20))
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
        
        self.menuVContainer.setFixedWidth(230)
        # self.menuVContainer.setMinimumWidth(230)
        # self.menuVContainer.setMaximumWidth(600)
        self.menuVContainer.addWidget(self.menuList)
        self.menuVContainer.addWidget(self.extendHContainer)
        
        self.pageHContainer = HContainer()
        self.pageHContainer.addWidget(self.stackedWidget)
        
        # TODO 最大化后布局大小改变
        # self.splitter = QSplitter(self)
        # self.splitter.addWidget(self.menuVContainer)
        # self.splitter.addWidget(self.stackedWidget)
        # self.layout.addWidget(self.splitter, alignment=Qt.AlignTop)
        
        self.layout.addWidget(self.menuVContainer)
        self.layout.addWidget(self.pageHContainer)

        self.settingsVContainer = SettingsHierarchy(self)
        self.maskWidget = MaskWidget(self)
        
        self.showMenuBtn = QPushButton(qta.icon("fa.angle-double-right", color=QColor(200, 200, 200)), "", self)
        self.showMenuBtn.setIconSize(QSize(20, 20))
        self.showMenuBtn.setToolTip("弹出菜单栏")
        self.showMenuBtn.resize(32, 28)
        self.showMenuBtn.setHidden(True)
        
        self.bind()
        
        self.menuVContainer.setStyleSheet("""
            QPushButton:hover {
                background-color: rgb(49, 50, 50);
            }
        """)
        
        self.showMenuBtn.setStyleSheet("""
        QPushButton {
            background-color: transparent;  /* 重点，设置为透明 */
            border-radius: 3px;
            margin: 0;
            padding: 0;
        }
        QPushButton:hover {
            background-color: transparent;  /* 重点，设置为透明 */
            border-radius: 3px;
            margin: 0;
            padding: 0;
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
                color: white;
                width: 120px;
                background-color: rgb(51, 118, 205);
                border: 1px solid rgb(31, 31, 31);
            }
            QPushButton:hover {
                color: white;
                background-color: rgb(47, 108, 187);
            }
        """)
        

    def bind(self):
        # QListWidget绑定事件
        self.menuList.listWidget.currentRowChanged.connect(self.router)
        
        self.hideMenuBtn.clicked.connect(self.hide_menu)
        self.showMenuBtn.clicked.connect(self.show_menu)
        self.showMenuBtn.enterEvent = lambda e: self.showMenuBtn.setIconSize(QSize(24, 24))  # 扩展enterEvent方法
        self.showMenuBtn.leaveEvent = lambda e: self.showMenuBtn.setIconSize(QSize(20, 20))
        
        self.settingsBtn.clicked.connect(self.show_settings)
        self.msgBtn.clicked.connect(self.showMessage)
        
    @Slot()
    def router(self, currentRow):
        # 菜单和页面的切换
        menu_item = self.menuList.menus[currentRow]
        if menu_item["class"]:
            self.stackedWidget.setCurrentWidget(getattr(self, menu_item["objectName"]))
    
    @Slot()
    def hide_menu(self):
        self.menuVContainer.hide()
        x = 0
        y = self.height() - self.showMenuBtn.height()
        self.showMenuBtn.move(x, y)
        self.showMenuBtn.show()
        self.showMenuBtn.raise_()
        
    @Slot()
    def show_menu(self):
        self.menuVContainer.show()
        self.showMenuBtn.hide()

    @Slot()
    def show_settings(self):
        # 添加遮罩层
        # self.maskWidget.resize(self.width() - self.settingsVContainer.width() + 1, self.height())
        self.maskWidget.showMaskAll()
        self.settingsVContainer.raise_()
        self.settingsVContainer.show()
    
    def delay_mask(self):
        self.maskWidget.hide()
        
    def resizeEvent(self, event) -> None:
        # 设置组件也随着窗体移动
        self.settingsVContainer.resize(self.settingsVContainer.width(), self.height())
        x = self.width() - self.settingsVContainer.width()
        y = 0
        self.settingsVContainer.move(x, y)
        
        # 左下角showMenuBtn也跟着移动
        self.showMenuBtn.move(0, self.height() - self.showMenuBtn.height())
        
        # maskWidget也随着调整大小
        self.maskWidget.resize(self.width() - self.settingsVContainer.width(), self.height())
        
        # messageBox也跟着移动 # TODO 多个消息框如何处理？
        if hasattr(self, "messageBox"):
            x = self.width() - self.messageBox.width() - 1
            y = self.height() - self.messageBox.height() - 1
            self.messageBox.move(x, y)
        
    def mousePressEvent(self, event) -> None:
        if not self.settingsVContainer.underMouse():
            print("click")
            self.maskWidget.hide()
            self.settingsVContainer.hideSelf()
                
    def showMessage(self):
        """弹出信息"""
        self.messageBox = MessageBox(self)
        self.messageBox.setWindowTitle("Message")
        self.messageBox.set_text("上图中直观展示出C2时共有2个异常值点，如果对C2进行分析，且分析方法对异常值敏感时（比如相关分析，回归分析等），此时需要对该2个异常值点进行处理成null或者填充，或者在分析时进行过滤。")
        self.messageBox.add_button("OK")
        self.messageBox.set_button_color("OK")
        self.messageBox.resize(self.messageBox.sizeHint())  # 关键，show之前获取建议的尺寸
        x = self.width() - self.messageBox.width() - 1
        y = self.height() - self.messageBox.height() - 1
        self.messageBox.move(x, y)
        self.messageBox.show()
    
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    m=MainFrame()
    m.show()
    app.exit(app.exec())