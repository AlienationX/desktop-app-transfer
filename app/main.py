# 导入sys
import sys
from datetime import datetime

from PySide6.QtWidgets import QApplication, QMainWindow ,QWidget, QVBoxLayout, QLabel, QTreeView, QAbstractItemView
from PySide6.QtCore import Qt, Slot, QTimer
from PySide6.QtGui import QFont, QAction

# from qt_material import apply_stylesheet
from main_ui import Ui_MainWindow
 
# 继承QWidget类，以获取其属性和方法
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.view = QTreeView()
        self.view.setAlternatingRowColors(True)
        self.view.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.view.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.view.setAnimated(False)
        self.view.setAllColumnsShowFocus(True)
        self.setCentralWidget(self.view)
        
        self.bind_menu()
        
    
    def bind_menu(self):
        # 触发菜单的信号
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(lambda: print("About"))
        
        # 设置主窗口右键菜单
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.openFile = QAction("Open")
        self.closeFile = QAction("Close")
        self.openFile.triggered.connect(lambda: print("Open"))
        self.closeFile.triggered.connect(lambda: print("Close"))
        # self.addAction(self.openFile)
        # self.addAction(self.closeFile)
        self.addActions([self.openFile, self.closeFile])
        
        # 对控件添加右键菜单，供参考
        self.sendValue = QAction("send value")
        self.sendValue.triggered.connect(lambda: print("Send Value"))
        self.lable = QLabel("HAHAHHAHAHA")
        # self.lable.setText()
        self.lable.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.lable.addAction(self.sendValue)
        # 将控件添加到布局中
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.lable)
        self.ui.centralwidget.setLayout(mainLayout)
        
    
class LoadWindow(QWidget):
    """可以放入图片，并打印相关信息，处理完毕后显示主窗口"""
    def __init__(self):
        super().__init__()
        
        self.label = QLabel("加载中...")
        self.label.setFont(QFont("微软雅黑", 30))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.label)
        self.setLayout(self.mainLayout)
        
        QTimer.singleShot(2000, self.openMainWindow)
        
    def openMainWindow(self):
        self.close()
        self.mainWindow = MainWindow()
        self.mainWindow.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # apply_stylesheet(app, theme='light_blue.xml')
    window = LoadWindow()
    window.show()
    sys.exit(app.exec())
