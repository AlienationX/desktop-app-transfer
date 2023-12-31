from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import qtawesome as qta

from transfer.widgets.mini_widgets import HContainer, VContainer, MaskWidget, MenuList, SettingsHierarchy, MessageBox, WarningBox, InfoBox
import sys

class MainFrame(QFrame, QWidget):
    
    """主窗口"""
    
    def __init__(self):
        super().__init__()
        
        self.setObjectName("mainFrame")
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
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
        self.extendHContainer.setContentsMargins(6, 2, 0, 2)
        
        self.settingsBtn = QPushButton(qta.icon("msc.settings-gear", color=QColor(200, 200, 200)), "")
        self.settingsBtn.setIconSize(QSize(20, 20))
        self.settingsBtn.setToolTip("设置")

        self.helpBtn = QPushButton(qta.icon("mdi.help-circle-outline", color=QColor(200, 200, 200)), "")
        self.helpBtn.setIconSize(QSize(20, 20))
        self.helpBtn.setToolTip("帮助")
        
        self.feedbackBtn = QPushButton()
        self.feedbackBtn.setIcon(qta.icon("msc.comment", color=QColor(200, 200, 200)))
        self.feedbackBtn.setIconSize(QSize(20, 20))
        
        self.ellipsisBtn = QPushButton(qta.icon("msc.ellipsis", color=QColor(200, 200, 200)), "")
        self.ellipsisBtn.setIconSize(QSize(20, 20))
        self.ellipsisMenu = QMenu()
        self.ellipsisMenu.addAction(qta.icon("msc.feedback", color=QColor(200, 200, 200)), "Feedback")   # 反馈
        self.ellipsisMenu.addAction(qta.icon("mdi.math-log", color=QColor(200, 200, 200)), "UpdateLog")  # 更新日志
        self.ellipsisMenu.addAction(qta.icon("ph.snapchat-logo", color=QColor(200, 200, 200)), "About")  # 关于
        self.ellipsisBtn.setMenu(self.ellipsisMenu)  # TODO 增加样式
        self.ellipsisBtn.setToolTip("其他功能按钮")
    
        self.hideMenuBtn = QPushButton(qta.icon("fa.angle-double-left", color=QColor(200, 200, 200)), "")
        self.hideMenuBtn.setIconSize(QSize(20, 20))
        self.hideMenuBtn.setToolTip("隐藏菜单栏")
        
        self.extendHContainer.addWidget(self.settingsBtn)
        self.extendHContainer.addWidget(self.helpBtn)
        self.extendHContainer.addWidget(self.feedbackBtn)
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
        
        self.setStyleSheet("""
            #mainFrame {
                background-color: rgb(40, 40, 40);
            }
        """)
        
        self.menuVContainer.setStyleSheet("""
            QWidget {
                background-color: rgb(40, 40, 40);
            }               
            QPushButton:hover {
                background-color: rgb(60, 60, 60);
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
                color: rgb(250, 250, 250);
                width: 120px;
                background-color: rgb(51, 118, 205);
                border: 1px solid rgb(31, 31, 31);
            }
            QPushButton:hover {
                color: rgb(250, 250, 250);
                background-color: rgb(47, 108, 187);
            }
            QPushButton:disabled {
                color: rgb(250, 250, 250);
                background-color: green;
            }
            QListView {
                outline: none;  /* 禁用被选中的虚线 */
            }
            QListView::item:hover {
                border-radius: 3px;
                background-color: rgb(4, 57, 94);
                font-size: 13px;
            }
            QListView::item:selected {
                border-radius: 3px;
                background-color: rgb(58, 46, 86);
            }
            QStackedWidget QProgressBar {
                border: 1px solid rgb(31, 31, 31);
                border-radius: 3px;
                padding: 0px;
            }
            QStackedWidget QProgressBar::chunk {
                background-color: rgb(3, 74, 21);
                /* width: 20px; */
                /* margin: 0.5px; */  /* 带间隔的进度条 */
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
        self.feedbackBtn.clicked.connect(self.showFeedback)
        
    @Slot()
    def router(self, currentRow):
        # 菜单和页面的切换
        menu_item = self.menuList.menus[currentRow]
        if menu_item["class"]:
            self.stackedWidget.setCurrentWidget(getattr(self, menu_item["objectName"]))
    
    def showwwwwwEvent(self, event) -> None:
        # self.resize(min(self.width(), self.parent().width()), self.parent().height())
        
        self.showAnim = QPropertyAnimation(self, b"geometry")
        self.showAnim.setStartValue(QRect(0, 0, self.width(), self.height()))
        self.showAnim.setEndValue(QRect(self.width(), 0, self.width(), self.height()))
        self.showAnim.setDuration(1000)
        self.showAnim.start()
        
    def hideeeeeeeEvent(self, event) -> None:   
        # self.resize(min(self.width(), self.parent().width()), self.parent().height())

        self.hideAnim = QPropertyAnimation(self, b"geometry")
        self.hideAnim.setStartValue(QRect(self.width(), 0, self.width(), self.height()))
        self.hideAnim.setEndValue(QRect(0, 0, self.width(), self.height()))
        self.hideAnim.setDuration(1000)
        # self.hideAnim.finished.connect(self.hide)  # 动画完成后执行其他操作
        self.hideAnim.start()
    
    # @Slot()
    # def hide_menu(self):
    #     self.menuVContainer.hide()
    #     x = 0
    #     y = self.height() - self.showMenuBtn.height()
    #     self.showMenuBtn.move(x, y)
    #     self.showMenuBtn.show()
    #     self.showMenuBtn.raise_()
    
    @Slot()
    def hide_menu(self):
        w = self.menuVContainer
        self.hideAnim = QPropertyAnimation(w, b"geometry")
        self.hideAnim.setStartValue(QRect(0, 0, w.width(), w.height()))
        self.hideAnim.setEndValue(QRect(w.width() * -1, 0, w.width(), w.height()))
        self.hideAnim.setDuration(200)
        self.hideAnim.finished.connect(w.hide)
        self.hideAnim.finished.connect(self.finished_action)  # TODO 动画完成后显示按钮，菜单按钮放在右上
        self.hideAnim.start()
        
        # self.menuVContainer.hide()
    
    def finished_action(self):
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
            self.maskWidget.hide()
            self.settingsVContainer.hideSelf()
                
    def showFeedback(self):
        """弹出信息"""
        self.feedbackBox = InfoBox(self)
        self.feedbackBox.setWindowTitle("Feedback")
        self.feedbackBox.set_title("请发送邮件至：<b>le7yi_ss@163.com</b>，感谢<br>")
        self.feedbackBox.set_text("您的反馈对我们非常重要，无论是称赞还是批评。这不仅可以帮助我们更好地理解您的需求和期望，还可以让我们在未来的规划和开发过程中做出更明智的决策。我们感谢您的宝贵时间和建议，期待能收到更多来自您的声音。")
        self.feedbackBox.add_shadow()
        self.feedbackBox.resize(self.feedbackBox.sizeHint())  # 关键，show之前获取建议的尺寸
        self.feedbackBox.move_center()
        self.feedbackBox.show()
    
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    m=MainFrame()
    m.show()
    app.exit(app.exec())