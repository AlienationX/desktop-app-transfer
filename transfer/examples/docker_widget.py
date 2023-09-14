from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import sys

class QDockWidgetDemo(QMainWindow):
    def __init__(self):
        super(QDockWidgetDemo, self).__init__()

        self.resize(400, 150)
        #设置窗口标题
        self.setWindowTitle("QDockWidgetDemo")

        self.dockWidget = QDockWidget('摆放位置',self)
        label = QLabel('TopDockWidgetArea')
        self.dockWidget.setWidget(label)
        self.dockWidget.setFloating(False)
        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.RightDockWidgetArea,self.dockWidget)

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDockWidgetDemo()
    main.show()
    sys.exit(app.exec_())

