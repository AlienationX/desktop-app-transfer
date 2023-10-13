from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import qtawesome as qta

import sys

class MessageBox(QDialog):
    
    """
    msgBox.setWindowTitle("Message Box Titil")  # 设置标题，附加一个关闭按钮
    msgBox.setTitle("The document has been modified.")  # 主文本
    msgBox.setText("Do you want to save your changes?")  # 副文本
    # msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)  # 按钮 自定义
    # msgBox.setDefaultButton(QMessageBox.Save)  # 默认(选中)按钮
    """
    
    signal = Signal(str)
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.MSWindowsFixedSizeDialogHint)  # 隐藏边框\总在最前\禁止调整大小
        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏边框\总在最前\禁止调整大小
        self.setAttribute(Qt.WA_TranslucentBackground, True)  # 背景透明（添加阴影必须背景透明）
        self.setObjectName("messageBox")
        
        # 添加阴影
        # shadow = QGraphicsDropShadowEffect(self)
        # shadow.setBlurRadius(12)
        # shadow.setOffset(1, 1)
        # shadow.setColor(Qt.gray)
        # self.setGraphicsEffect(shadow)
        
        # 重点： 这个frame作为背景和圆角
        self.frame = QFrame()        
        
        _layout = QVBoxLayout(self)
        _layout.setContentsMargins(6, 6, 6, 6)  # 设置无外边距则显示存在问题，所以阴影不适合能全屏的应用
        _layout.addWidget(self.frame)

        self.windowTitleLable = QLabel()
        self.windowTitleLable.setObjectName("titleLable")
        self.font = QFont()
        # font.setPointSize(11)
        self.font.setBold(True)
        self.windowTitleLable.setFont(self.font)
        self.closeBtn = QPushButton()
        self.closeBtn.setIcon(qta.icon("msc.close", color=QColor(174, 174, 174)))
        self.closeBtn.setIconSize(QSize(20, 20))
        self.closeBtn.clicked.connect(self.close)

        self.titleLable = QLabel()
        self.titleLable.setFont(self.font)
        # self.titleLable.setWordWrap(True)
        self.titleLable.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        
        self.contentLabel = QLabel()
        self.contentLabel.setObjectName("contentLabel")
        self.contentLabel.setWordWrap(True)  # 自动换行，只有中文和单词存在空格等才会换行，如果是一长串字母是不会换行的
        self.contentLabel.setMinimumWidth(360)
        self.contentLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        
        self.layout = QVBoxLayout(self.frame)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        
        self.titleWidget = QWidget()
        self.titleWidget.setObjectName("messageBoxTitle")
        self.titleWidget.setMaximumHeight(32)
        self.titleLayout = QHBoxLayout(self.titleWidget)
        self.titleLayout.setContentsMargins(6, 6, 6, 6)
        self.titleLayout.addWidget(self.windowTitleLable)
        self.titleLayout.addStretch()
        self.titleLayout.addWidget(self.closeBtn)

        self.contentWidget = QWidget()
        self.contentWidget.setObjectName("messageBoxContent")
        self.contentLayout = QVBoxLayout(self.contentWidget)
        self.contentLayout.setContentsMargins(6, 6, 6, 6)
        
        self.buttonsWidget = QWidget()
        self.buttonsWidget.setObjectName("messageBoxButtons")
        self.buttonsLayout = QHBoxLayout(self.buttonsWidget)
        self.buttonsLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonsLayout.addStretch()  
        
        # 只增加contentWidget，其他的判断是否存在再增加
        self.layout.addWidget(self.contentWidget)
        
        self.setStyleSheet("""
            QWidget {
                border-radius: 5px;
                background-color: rgb(31, 31, 31);
                color: rgb(174, 174, 174);
            }
            QPushButton:hover {
                background-color: rgb(49, 50, 50);
            }
            #messageBoxContent {
                background-color: rgb(44, 45, 46);
            }
            #messageBoxContent QWidget {
                background-color: transparent;
            }
            #messageBoxContent QPushButton {
                padding: 3px 10px;
                color: white;
                border: 1px solid rgb(31, 31, 31);
            }
            #messageBoxContent QPushButton:hover {
                background-color: rgb(0, 120, 212);
                font-weight: bold;
            }
        """)
        
        # self.setStyleSheet("""
        #     QWidget {
        #         border-radius: 5px;
        #         background-color: rgb(235, 235, 235);
        #         color: rgb(39, 39, 39);
        #     }
        #     QPushButton:hover {
        #         background-color: rgb(200, 200, 200);
        #     }
        #     #messageBoxContent {
        #         border-top-left-radius: 0px;
        #         border-top-right-radius: 0px;
        #         background-color: white;
        #     }
        # """)
        
    def setWindowTitle(self, window_title):
        self.windowTitleLable.setText(window_title)
        self.layout.insertWidget(0, self.titleWidget)
        # 如果存在WindowTitle，则修改为上角为直角
        self.contentWidget.setStyleSheet("""
            #messageBoxContent {
                border-top-left-radius: 0px;
                border-top-right-radius: 0px;
                background-color: rgb(44, 45, 46);
            }
        """)
    
    def set_title(self, title):
        self.titleLable.setText(title)
        self.titleLable.setTextInteractionFlags(Qt.TextSelectableByMouse)  # 可以用鼠标选择复制
        self.contentLayout.insertWidget(0, self.titleLable)
    
    def set_text(self, content):
        self.contentLabel.setText(content)
        self.contentLabel.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.contentLayout.addWidget(self.contentLabel)
    
    def add_button(self, text):
        self.button = QPushButton(self)
        self.button.setText(text)
        # button.setFont(self.font)
        self.button.clicked.connect(self.getBtnText)
        self.buttonsLayout.addWidget(self.button, alignment=Qt.AlignRight | Qt.AlignBottom)
        self.contentLayout.addWidget(self.buttonsWidget)

    def set_button_color(self, buttons_text:list):
        for btn in self.buttonsWidget.findChildren(QPushButton):
            if btn.text() in buttons_text:
                btn.setStyleSheet("background-color: rgb(0, 120, 212)")
                
    def set_background_color(self):
        pass
                
    def set_min_width(self, width):
        self.contentLabel.setMinimumWidth(width)

    def add_shadow(self):
        self.shadow = QGraphicsDropShadowEffect(self, blurRadius=10, xOffset=3, yOffset=3, color=Qt.black)
        self.frame.setGraphicsEffect(self.shadow)  # 只能在frame上设置阴影
        
    def move_center(self):
        x = self.parent().width() / 2 - self.width() / 2
        y = self.parent().height() / 2 - self.height() / 2
        self.move(x, y)
    
    # @Slot()  # 需要注释掉，否则无法获取sender()的返回值
    def getBtnText(self):
        btnText = self.sender().text()
        self.signal.emit(btnText)  # 发送信号
        self.close()

    def resizeEvent(self, event) -> None:
        print("resize", self.width(), self.height())
    
    def enterEvent(self, event):
        # TODO 鼠标进入增加边框
        pass
        # self.setStyleSheet("""
        #     #backgroundFrame {
        #         border-radius: 5px;
        #         background-color: rgb(31, 31, 31);
        #         color: rgb(174, 174, 174);
        #         border: 1px solid rgb(51, 118, 205);
        #     }               
        # """)
    
    def leaveEvent(self, event):
        # TODO 鼠标移开取消边框
        pass
        # self.frame.setGraphicsEffect(None)  # 只能在frame上设置阴影  
        # self.setStyleSheet("#backgroundFrame {border: none;}")
    
    def mousePressEvent(self, event):
        # 实现鼠标拖拽功能，记录鼠标按下的时候的坐标，仅限标题栏支持拖拽移动
        if self.titleWidget.underMouse():
            self.pressX = event.x()
            self.pressY = event.y()
 
    def mouseMoveEvent(self, event):
        if self.titleWidget.underMouse():
            x = event.x()
            y = event.y()   # 获取移动后的坐标
            moveX = x - self.pressX
            moveY = y - self.pressY  # 计算移动了多少
    
            positionX = self.frameGeometry().x() + moveX
            positionY = self.frameGeometry().y() + moveY    # 计算移动后主窗口在桌面的位置
            self.move(positionX, positionY)    # 移动主窗口


class InfoBox(MessageBox):
    
    # Success
    pass

class SuccessBox(MessageBox):
    
    # Success
    pass
class ConfirmBox(MessageBox):
    
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.set_min_width(200)
        # self.setWindowTitle("Confirm")
        # self.set_title("Are you sure exit?")
        self.add_button("OK")
        self.add_button("Cancel")
        self.set_button_color("Cancel")
        self.add_shadow()
        self.setWindowModality(Qt.ApplicationModal)

class WarningBox(MessageBox):
    # 橘红
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.add_button("Close")
        self.set_button_color("Close")
        self.add_shadow()

class ErrorBox(MessageBox):
    # 深红
    pass
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    w = QWidget()
    w.resize(600, 400)
    
    m=ConfirmBox(w)
    m.set_title("Are you sure exit?")
    m.resize(m.sizeHint())  # 更新建议的尺寸，关键

    print(w.width() , m.width(), w.height() , m.height())
    x = w.width() - m.width()
    y = w.height() - m.height()
    print(x, y)
    m.move(x, y)
    
    w.show()

    app.exit(app.exec())
