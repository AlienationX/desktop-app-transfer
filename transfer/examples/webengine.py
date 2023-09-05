import sys
import os
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView  # 需要额外安装 pip install PySide6-Addons

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.browser=QWebEngineView()
        # self.browser.load(QUrl("https://www.baidu.com"))
        url = "/Users/tangzy/code/python/desktop-app-transfer/output_file.html"
        self.browser.load(QUrl.fromLocalFile(url))
        self.setCentralWidget(self.browser)
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    app.exit(app.exec())