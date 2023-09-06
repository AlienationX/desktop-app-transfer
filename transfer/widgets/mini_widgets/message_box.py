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
        self.setMaximumWidth(300)
        
        # 重点： 这个widget作为背景和圆角
        _layout = QVBoxLayout(self)
        self.widget = QWidget(self)
        self.widget.setObjectName('backgroundWidget')
        _layout.addWidget(self.widget)

        self.titleLable = QLabel("Message")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.titleLable.setFont(font)
        self.closeBtn = QPushButton("")
        self.closeBtn.setIcon(qta.icon("msc.close", color=QColor(174, 174, 174)))
        self.closeBtn.setIconSize(QSize(20, 20))
        self.closeBtn.clicked.connect(self.close)
        
        self.textLabel = QLabel("QDialog实现自定义消息框，QPropertyAnimation实现动画效果，比如隐藏和弹出、调整大小等。QSplitter实现拖动控件之间的边界")
        self.textLabel.setObjectName("messageBoxText")
        self.textLabel.setWordWrap(True)  # 自动换行
        self.textLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        
        self.layout = QVBoxLayout(self.widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.titleWidget = QWidget()
        self.titleWidget.setObjectName("messageBoxTitle")
        self.titleLayout = QHBoxLayout(self.titleWidget)
        self.titleLayout.setContentsMargins(0, 0, 0, 0)
        self.titleLayout.addWidget(self.titleLable)
        self.titleLayout.addStretch()
        self.titleLayout.addWidget(self.closeBtn)
        self.titleWidget.setContentsMargins(6,6,6,6)
        self.textLabel.setContentsMargins(6,0,6,6)
        self.layout.addWidget(self.titleWidget)
        self.layout.addWidget(self.textLabel)
        
        # self.setStyleSheet("""
        #     QWidget {
        #         border-radius: 5px;
        #         background-color: rgb(31, 31, 31);
        #         color: rgb(174, 174, 174);
        #         font-family: Consolas;
        #     }
        #     QPushButton:hover {
        #         background-color: rgb(49, 50, 50);
        #     }
        # """)
        
        self.setStyleSheet("""
            #backgroundWidget {
                border-radius: 5px;
                background-color: white;
                color: rgb(174, 174, 174);
            }
            QWidget {
                font-family: Consolas;
            }
            QPushButton {
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: rgb(49, 50, 50);
            }
            #messageBoxTitle {
                border-radius: 5px;
                background-color: rgb(235, 235, 235);
            }
            #messageBoxText {
                border-radius: 5px;
                background-color: white;
            }
        """)
        
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    m=MessageBox()
    m.show()
    app.exit(app.exec())