from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import qtawesome as qta

import sys

class MessageBox(QWidget):
    """
    msgBox.setWindowTitle("Message Box Titil")  # 设置标题，附加一个关闭按钮
    msgBox.setTitle("The document has been modified.")  # 主文本
    msgBox.setText("Do you want to save your changes?")  # 副文本
    # msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)  # 按钮 自定义
    # msgBox.setDefaultButton(QMessageBox.Save)  # 默认(选中)按钮
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # 隐藏边框且总在最前
        self.setAttribute(Qt.WA_TranslucentBackground, True)  # 背景透明
        self.setMaximumWidth(400)
        
        # 添加阴影
        # shadow = QGraphicsDropShadowEffect(self)
        # shadow.setBlurRadius(12)
        # shadow.setOffset(1, 1)
        # shadow.setColor(Qt.gray)
        # self.setGraphicsEffect(shadow)
        
        # 重点： 这个frame作为背景和圆角
        self.frame = QFrame()
        self.frame.setObjectName("backgroundWidget")
        # shadow = QGraphicsDropShadowEffect(self, blurRadius=10, xOffset=2, yOffset=2, color=Qt.gray)
        # self.frame.setGraphicsEffect(shadow)  # 只能在frame上设置阴影
        
        _layout = QVBoxLayout(self)
        _layout.setContentsMargins(0, 0, 0, 0)  # 设置无外边距则显示存在问题，所以阴影不适合能全屏的应用
        _layout.addWidget(self.frame)

        self.windowTitleLable = QLabel("MESSAGE TITLE")
        self.windowTitleLable.setObjectName("titleLable")
        font = QFont()
        # font.setPointSize(11)
        font.setBold(True)
        self.windowTitleLable.setFont(font)
        self.closeBtn = QPushButton()
        self.closeBtn.setIcon(qta.icon("msc.close", color=QColor(174, 174, 174)))
        self.closeBtn.setIconSize(QSize(20, 20))
        self.closeBtn.clicked.connect(self.close)

        self.titleLable = QLabel()
        self.titleLable.setWordWrap(True)
        self.titleLable.setFont(font)
        
        self.contentLabel = QLabel(self)
        self.contentLabel.setText("在 CSS 中，border-radius 属性可以设置圆角，对应左上角、右上角、右下角、左下角的圆角可以通过 border-top-left-radius、border-top-right-radius、border-bottom-right-radius、border-bottom-left-radius 四个属性进行设置。在 CSS 中，border-radius 属性可以设置圆角，对应左上角、右上角、右下角、左下角的圆角可以通过 border-top-left-radius、border-top-right-radius、border-bottom-right-radius、border-bottom-left-radius 四个属性进行设置。")
        self.contentLabel.setObjectName("contentLabel")
        self.contentLabel.setWordWrap(True)  # 自动换行
        # self.contentLabel.adjustSize()
        self.contentLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        
        self.layout = QVBoxLayout(self.frame)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.titleWidget = QWidget()
        self.titleWidget.setObjectName("messageBoxTitle")
        self.titleLayout = QHBoxLayout(self.titleWidget)
        self.titleLayout.setContentsMargins(0, 0, 0, 0)
        self.titleLayout.addWidget(self.windowTitleLable)
        self.titleLayout.addStretch()
        self.titleLayout.addWidget(self.closeBtn)
        self.titleWidget.setContentsMargins(6, 6, 6, 6)

        self.contentWidget = QWidget()
        self.contentWidget.setObjectName("messageBoxContent")
        self.contentLayout = QHBoxLayout(self.contentWidget)
        self.contentLayout.setContentsMargins(0, 0, 0, 0)
        
        self.contentLabel.setContentsMargins(6, 6, 6, 6)
        self.layout.addWidget(self.titleWidget)
        # self.layout.addWidget(self.titleLable)
        self.layout.addWidget(self.contentLabel)
        
        # 为了获取messagebox的实际大小，只有show之后才会获取到真实大小，没有show之前是默认的640×480
        # https://blog.csdn.net/weixin_42108411/article/details/108023828
        self.show()
        self.hide()
        print("box", self.width(), self.height())
        print("box", self.geometry())
        
        
        self.setStyleSheet("""
            QWidget {
                border-radius: 5px;
                background-color: rgb(31, 31, 31);
                color: rgb(174, 174, 174);
            }
            QPushButton:hover {
                background-color: rgb(49, 50, 50);
            }
            #contentLabel {
                border-top-left-radius: 0px;
                border-top-right-radius: 0px;
                background-color: rgb(44, 45, 46);
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
        #     #contentLabel {
        #         border-top-left-radius: 0px;
        #         border-top-right-radius: 0px;
        #         background-color: white;
        #     }
        # """)
    
        
    def setWindowTitle(self, window_title):
        self.windowTitleLable.setText(window_title)
    
    def setTitle(self, title):
        self.titleLable.setText(title)
    
    def setText(self, content):
        self.contentLabel.setText(content)
    
    def addButton(self, text):
        button = QPushButton(None, text, self)
        button.clicked.connect(self.getBtnText)

    def setDefaultButton(self, text):
        pass
    
    def getBtnText(self):
        return self.render().text()
    
    def showEvent(self, envet):
        # show之前处理的事件，可以获取真正的窗体大小
        print("envet", self.width(), self.height())
    
    def enterEvent(self, event):
        # TODO 鼠标进入增加阴影
        print("enter message box")
        # shadow = QGraphicsDropShadowEffect(self, blurRadius=10, xOffset=2, yOffset=2, color=Qt.gray)
        # self.frame.setGraphicsEffect(shadow)  # 只能在frame上设置阴影
        # self.setStyleSheet("""
        # QWidget {
        #         border-radius: 5px;
        #         background-color: rgb(31, 31, 31);
        #         color: rgb(174, 174, 174);
        #                    border: 1px solid red;
        #     }
        #     QPushButton:hover {
        #         background-color: rgb(49, 50, 50);
        #     }
        #     #contentLabel {
        #         border-top-left-radius: 0px;
        #         border-top-right-radius: 0px;
        #         background-color: rgb(44, 45, 46);
        #     }                 
        # """)
    
    def leaveEvent(self, event):
        # TODO 鼠标移开取消阴影
        print("leave message box")
        # self.frame.setGraphicsEffect(None)  # 只能在frame上设置阴影  
        # self.setStyleSheet("#backgroundWidget {border: none;}")
    
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
        
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    m=MessageBox()
    m.setWindowTitle("WINDOW TITLE")
    m.setTitle("I am title")
    m.setText("当面对没有分隔开的长串英文与数字、英文符号（如 '.'就是英文符号，‘。’就是中文符号）时，QLabel无法自动换行。下面利用QFontMetrics实现换行，该类通过对font属性进行解析，提供指定font下的字符、字符串宽度等获取接口。")
    m.addButton("OK")
    m.addButton("Cancel")
    m.show()
    app.exit(app.exec())
