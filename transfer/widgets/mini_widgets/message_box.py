from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import qtawesome as qta

import sys

class MessageBox(QWidget):
    
    def __init__(self,):
        super().__init__()
        
        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏边框
        self.setAttribute(Qt.WA_TranslucentBackground, True)  # 背景透明
        # self.setMaximumWidth(300)
        
        # 重点： 这个widget作为背景和圆角
        _layout = QVBoxLayout(self)
        self.widget = QWidget(self)
        self.widget.setObjectName("backgroundWidget")
        _layout.addWidget(self.widget)

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
        
        self.contentLabel = QLabel("在 CSS 中，border-radius 属性可以设置圆角，对应左上角、右上角、右下角、左下角的圆角可以通过 border-top-left-radius、border-top-right-radius、border-bottom-right-radius、border-bottom-left-radius 四个属性进行设置。")
        self.contentLabel.setObjectName("messageBoxText")
        self.contentLabel.setWordWrap(True)  # 自动换行
        self.contentLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        
        self.layout = QVBoxLayout(self.widget)
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
        
    def setTitle(self, title):
        self.titleLable.setText(title)
    
    def setContent(self, content):
        self.contentLabel.setText(content)
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    m=MessageBox()
    m.show()
    app.exit(app.exec())