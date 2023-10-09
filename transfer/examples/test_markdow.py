import sys
import os
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout

import markdown

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        with open("transfer/resources/texts/home.md", "r", encoding="utf-8") as f:
            markdown_text = f.read()
        html = markdown.markdown(markdown_text)
        print(html)
        
        self.label = QLabel()
        self.label.setText(html)
        self.label.setWordWrap(True)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.label)
        
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    app.exit(app.exec())