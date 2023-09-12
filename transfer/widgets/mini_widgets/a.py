from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import sys


class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QDialog案例")
        self.resize(300, 200)

        self.button = QPushButton(self)
        self.button.setText('弹出对话框')
        self.button.move(50, 50)
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog = QDialog()
        #将按钮放到dialog上面
        button = QPushButton('确定', dialog)
        # 将button绑定dialog的关闭
        button.clicked.connect(dialog.close)
        #将button移动到(50, 50)的位置
        button.move(50, 50)
        #设置对话框的标题
        dialog.setWindowTitle("对话框")
        #除了该对话框其他都能不使用
        dialog.setWindowModality(Qt.ApplicationModal)
        #运行对话框
        dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = QDialogDemo()
    main.show()

    sys.exit(app.exec_())