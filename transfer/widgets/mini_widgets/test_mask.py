from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import sys

from addons_widget import MaskWidget
        
class TestMaskWidget(QWidget):
    """测试遮罩的显示效果
    """
    def __init__(self):
        super().__init__()
        # 设置白色背景，方便显示出遮罩
        # self.setStyleSheet('background:white;')
        main_layout = QVBoxLayout()
        self.button = QPushButton('点击显示遮罩')
        self.button.clicked.connect(self.show_dialog)
        main_layout.addWidget(self.button, 1, Qt.AlignCenter)
        self.setLayout(main_layout)
        self.show()
 
    def show_dialog(self):
        maskWidget = MaskWidget(self)
        maskWidget.showMaskAll()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TestMaskWidget()
    w.show()
    app.exec()