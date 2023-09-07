from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

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
    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListWidget 自定义菜单")
        self.resize(400, 300)
        self.list_widget = QListWidget(self)
        self.setCentralWidget(self.list_widget)

        # 添加菜单项
        item = QListWidgetItem()
        item.setSizeHint(QSize(200, 32)) 
        # item.setText("菜单")
        widget = CustomWidget("    菜单")
        self.list_widget.insertItem(0, item)
        self.list_widget.setItemWidget(item, widget)

        # 添加菜单项
        item1 = QListWidgetItem()
        item1.setSizeHint(QSize(200, 32)) 
        # item1.setText("菜单1")
        widget1 = CustomWidget("    菜单1")
        self.list_widget.insertItem(1, item1)
        self.list_widget.setItemWidget(item1, widget1)

        # 添加菜单项
        item2 = QListWidgetItem()
        item2.setSizeHint(QSize(200, 32)) 
        # item2.setText("菜单2")
        widget2 = CustomWidget("    caidan2")
        self.list_widget.insertItem(2, item2)
        self.list_widget.setItemWidget(item2, widget2)

        self.setStyleSheet("""
            QListView::item:hover {
                background-color: green;
            }
            QListView::item:selected {
                border-left: 5px solid red;
                background-color: orange;
            }
        """)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()