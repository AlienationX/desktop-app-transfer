from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import sys

#!/usr/bin/env python
# encoding: utf-8
'''
@author: JHC 
@license: None
@contact: JHC000abc@gmail.com
@file: QT.py
@time: 2022/07/19/ 16:53
@desc:
'''

from CDrawer import CDrawer
import sys
import cgitb
sys.excepthook = cgitb.enable(1, None, 5, '')
from PySide6.QtWidgets import QApplication

class DrawerWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(DrawerWidget, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('DrawerWidget{background:white;}')
        self.lineedit = QLineEdit(self)


        layout = QVBoxLayout(self)
        layout.addWidget(self.lineedit)
        layout.addWidget(QPushButton('button', self,clicked=self._click))
        layout.addWidget(QPushButton('button2', self, clicked=self._click2))



    def _click(self):
        if self.lineedit.text() != "":
            print("框中输入的文字为:{}".format(self.lineedit.text()))
            self.lineedit.clear()
        else:
            print("框中未输入的文字为")

    def _click2(self):
        print("没用")





class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.resize(480, 960)
        self.entermouse = 0
        self.flag = 0

        self.x = 0
        self.y = 0
        # layout = QGridLayout(self)
        # layout.addWidget(QPushButton('侧边栏', self, clicked=self.doOpenLeft), 1, 0)

    def mouseMoveEvent(self, event):
        print("-----------------------mouseMoveEvent-----------------------")
        if self.entermouse == 1:
            self.x = event.x()
            self.y = event.y()
            self.flag = 1
            if self.x < 100 :
                self.doOpenLeft()
        self.update()


    def mousePressEvent(self, event):
        if self.entermouse == 1 and self.flag == 1 and event.button() == Qt.LeftButton:
            self.x = event.x()
            self.y = event.y()
            print("按压 ",self.x,self.y)

        else:
            pass
        self.update()



    def mouseReleaseEvent(self, event):
        if self.entermouse == 1 and self.flag == 1 and event.button() == Qt.LeftButton:
            self.x = event.x()
            self.y = event.y()
            print("松开 ", self.x, self.y)
        else:
            pass
        self.update()

    def enterEvent(self, *args, **kwargs):
        if self.entermouse == 0:
            self.entermouse = 1
        else:
            pass

    def leaveEvent(self, *args, **kwargs):
        if self.entermouse == 1:
            self.entermouse = 0
        else:
            pass



    def doOpenLeft(self):
        if not hasattr(self, 'leftDrawer'):
            self.leftDrawer = CDrawer(self, direction=CDrawer.LEFT)
            self.leftDrawer.setWidget(DrawerWidget(self.leftDrawer))
        self.leftDrawer.show()

    def paintEvent(self, event):
        super().paintEvent(event)
        self.painter = QPainter()
        self.painter.begin(self)
        self.update()
        if self.x != 0 and self.y != 0 and self.entermouse == 1:
            # print("self.x,self.y ",self.x,self.y)
            self.update()
        else:
            self.update()
        self.update()
        self.painter.end()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
