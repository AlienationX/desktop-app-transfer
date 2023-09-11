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
    def __init__(self):
        super().__init__()
        
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
        self.frame = QFrame(self)
        self.frame.setObjectName("backgroundWidget")
        # shadow = QGraphicsDropShadowEffect(self, blurRadius=10, xOffset=2, yOffset=2, color=Qt.gray)
        # self.frame.setGraphicsEffect(shadow)  # 只能在frame上设置阴影
        _layout = QVBoxLayout(self)
        # _layout.setContentsMargins(0, 0, 0, 0)  # 设置无外边距则显示存在问题，所以阴影不适合能全屏的应用
        _layout.addWidget(self.frame)

        self.titleLable = QLabel("Message Title")
        self.titleLable.setObjectName("titleLable")
        font = QFont()
        # font.setPointSize(11)
        font.setBold(True)
        self.titleLable.setFont(font)
        self.closeBtn = QPushButton()
        self.closeBtn.setIcon(qta.icon("msc.close", color=QColor(174, 174, 174)))
        self.closeBtn.setIconSize(QSize(20, 20))
        self.closeBtn.clicked.connect(self.close)
        
        self.contentLabel = QLabel("在 CSS 中，border-radius 属性可以设置圆角，对应左上角、右上角、右下角、左下角的圆角可以通过 border-top-left-radius、border-top-right-radius、border-bottom-right-radius、border-bottom-left-radius 四个属性进行设置。在 CSS 中，border-radius 属性可以设置圆角，对应左上角、右上角、右下角、左下角的圆角可以通过 border-top-left-radius、border-top-right-radius、border-bottom-right-radius、border-bottom-left-radius 四个属性进行设置。")
        self.contentLabel.setObjectName("messageBoxText")
        self.contentLabel.setWordWrap(True)  # 自动换行
        self.contentLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        
        self.layout = QVBoxLayout(self.frame)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.titleWidget = QWidget()
        self.titleWidget.setObjectName("messageBoxTitle")
        self.titleLayout = QHBoxLayout(self.titleWidget)
        self.titleLayout.setContentsMargins(0, 0, 0, 0)
        self.titleLayout.addWidget(self.titleLable)
        self.titleLayout.addStretch()
        self.titleLayout.addWidget(self.closeBtn)
        self.titleWidget.setContentsMargins(6, 6, 6, 6)
        self.contentLabel.setContentsMargins(6, 6, 6, 6)
        self.layout.addWidget(self.titleWidget)
        self.layout.addWidget(self.contentLabel)
        
        # 为了获取messagebox的实际大小，只有show之后才会获取到真实大小，没有show之前是默认的640×480
        # https://blog.csdn.net/weixin_42108411/article/details/108023828
        self.show()
        self.hide()
        
        self.setStyleSheet("""
            QWidget {
                border-radius: 5px;
                background-color: rgb(31, 31, 31);
                color: rgb(174, 174, 174);
            }
            QPushButton:hover {
                background-color: rgb(49, 50, 50);
            }
            #messageBoxText {
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
        #     #messageBoxText {
        #         border-top-left-radius: 0px;
        #         border-top-right-radius: 0px;
        #         background-color: white;
        #     }
        # """)
        
    def setWindowTitle(self, window_title):
        pass
    
    def setTitle(self, title):
        self.titleLable.setText(title)
    
    def setText(self, content):
        self.contentLabel.setText(content)
    
    def enterEvent(self, event):
        # 鼠标进入增加阴影
        shadow = QGraphicsDropShadowEffect(self, blurRadius=10, xOffset=2, yOffset=2, color=Qt.gray)
        self.frame.setGraphicsEffect(shadow)  # 只能在frame上设置阴影
    
    def leaveEvent(self, event):
        # 鼠标移开取消阴影
        self.frame.setGraphicsEffect(None)  # 只能在frame上设置阴影  

        
if __name__=="__main__":
    app=QApplication(sys.argv)
    m=MessageBox()
    m.show()
    app.exit(app.exec())