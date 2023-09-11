from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import sys

class Test(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.resize(400, 300)
        
        self.btn = QPushButton("show")
        self.btn.clicked.connect(self.show)
                
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.btn)
        self.setLayout(self.layout)
        
    def show(self):
        self.dialog = QDialog(self)
        self.dialog.setModal(True)
        self.dialog.show()
        
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    m=Test()
    m.show()
    app.exit(app.exec())