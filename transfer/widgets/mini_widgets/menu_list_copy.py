from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import qtawesome as qta

class CustomWidget(QWidget):
    def __init__(self, text):
        super().__init__()
        
        self.button = QLabel(text, self)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.button.setFont(font)
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addWidget(self.button)
        self.layout.addWidget(QLabel("HAHA"))
        self.layout.addStretch()
        self.layout.addWidget(QPushButton(qta.icon("msc.chevron-down"), ""))
        leftIcon = QLabel()
        leftIcon.setPixmap(qta.icon("msc.chevron-down", color=QColor(200, 200, 200)).pixmap(QSize(20, 20)))
        self.layout.addWidget(leftIcon)
    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListWidget 自定义菜单")
        self.resize(400, 300)
        self.setWindowFlags(Qt.FramelessWindowHint) # 隐藏边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明
        
        self.widget = QWidget()
        self.widgetLayout = QVBoxLayout(self.widget)
        
        self.widget1 = QWidget()
        self.widgetLayout1 = QVBoxLayout(self.widget1)
        
        self.widget2 = QWidget()
        self.widgetLayout2 = QVBoxLayout(self.widget2)
        
        self.widgetLayout.addWidget(self.widget1)
        self.widgetLayout1.addWidget(self.widget2)
        
        
        self.btn = QPushButton("OK")
        self.btn.clicked.connect(self.close)
        self.list_widget = QListWidget()
        self.widgetLayout2.addWidget(self.btn)
        self.widgetLayout2.addWidget(self.list_widget)
        self.setCentralWidget(self.widget)

        # # 添加菜单项
        # item = QListWidgetItem()
        # item.setSizeHint(QSize(200, 32)) 
        # # item.setText("菜单")
        # widget = CustomWidget("    菜单")
        # self.list_widget.insertItem(0, item)
        # self.list_widget.setItemWidget(item, widget)

        # # 添加菜单项
        # item1 = QListWidgetItem()
        # item1.setSizeHint(QSize(200, 32)) 
        # # item1.setText("菜单1")
        # widget1 = CustomWidget("    菜单1")
        # self.list_widget.insertItem(1, item1)
        # self.list_widget.setItemWidget(item1, widget1)

        # # 添加菜单项
        # item2 = QListWidgetItem()
        # item2.setSizeHint(QSize(200, 32)) 
        # # item2.setText("菜单2")
        # widget2 = CustomWidget("    caidan2")
        # self.list_widget.insertItem(2, item2)
        # self.list_widget.setItemWidget(item2, widget2)
        
        for i in range(3):
            item2 = QListWidgetItem()
            item2.setSizeHint(QSize(200, 32)) 
            # item2.setText("菜单2")
            widget2 = CustomWidget("    caidan" + str(i))
            self.list_widget.addItem(item2)
            self.list_widget.setItemWidget(item2, widget2)
            
        self.list_widget.currentRowChanged.connect(lambda: print("bind1"))
        self.list_widget.currentRowChanged.connect(lambda: print("bind2"))

        self.setStyleSheet("""
            QWidget {
                border-radius: 0px;
                background-color: rgb(41, 41, 41);
                color: rgb(200, 200, 200);
            }
            QPushButton {
                background-color: rgb(50, 50, 50);
            }
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
                background-color: transparent;
            }
        """)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()