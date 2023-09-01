# 导入sys
import sys
from datetime import datetime

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Slot, Qt
from message_ui import Ui_Form
 
# 继承QWidget类，以获取其属性和方法
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.bind()
        
    def bind(self):
        self.ui.sendPushButton.clicked.connect(self.send)
    
    @Slot()
    def send(self):
        text = self.ui.inputLineEdit.text()
        if text:
            print(text)
            self.ui.plainTextEdit.appendPlainText(str(datetime.now()) + ' - ' + text)
            self.ui.inputLineEdit.clear()
        self.ui.inputLineEdit.setFocus()  # 在message_ui.py里面设置了快捷键发送消息


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
