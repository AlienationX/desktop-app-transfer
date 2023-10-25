import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class MyWidget(QFrame, QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.resize(200, 20)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏边框\总在最前\禁止调整大小
        self.setAttribute(Qt.WA_StyledBackground)
        self.setProperty("name", "title")
        
        self.label = QLabel("Are you ok?")
        self.btn = QPushButton("ok")
        self.btn.clicked.connect(self.close)
        
        self.frame = QFrame(self)
        self.frameLayout = QVBoxLayout(self.frame)
        self.frameLayout.addWidget(self.label)
        self.frameLayout.addWidget(self.btn)
        
        self.layout = QVBoxLayout(self)
        # self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.frame)
        
        self.setStyleSheet("""
            QFrame {
                background-color: green;
                border: 1px solid red;
            }
        """)
        
        print(self.style())
        
        
        # ****************设置框架形状****************** 开始
        # setFrameShape(QFrame.Shape)             # 设置框架形状
        # QFrame.NoFrame              # QFrame什么都没画
        # QFrame.Box                  # QFrame围绕其内容绘制一个框（有边框）（需要设置外线和中线的宽度）
        # QFrame.Panel                # QFrame绘制一个面板，使内容显得凸起或凹陷（设置中线宽度没用）
        # QFrame.HLine                # QFrame绘制一条没有框架的水平线（用作分隔符）
        # QFrame.VLine                # QFrame绘制一条无框架的垂直线（用作分隔符）
        # QFrame.StyledPanel          # 绘制一个矩形面板，其外观取决于当前的GUI样式。它可以升起或凹陷。
        # QFrame.WinPanel             # 绘制一个可以像Windows 2000中那样凸起或凹陷的矩形面板，对于GUI样式独立性，建议使用StyledPanel。
        
        # self.frame.setFrameShape(QFrame.NoFrame)
        # self.frame.setFrameShape(QFrame.Box)
        # self.frame.setFrameShape(QFrame.Panel)
        # self.frame.setFrameShape(QFrame.HLine)
        # self.frame.setFrameShape(QFrame.VLine)
        # self.frame.setFrameShape(QFrame.StyledPanel)
        # self.frame.setFrameShape(QFrame.WinPanel)
        # ****************设置框架形状****************** 结束
        
        # ****************设置框架阴影****************** 开始
        # setFrameShadow(QFrame.Shadow)  # 设置框架阴影
        # QFrame.Plain  # 框架和内容与周围环境呈现水平;（没有任何3D效果）
        # QFrame.Raised  # 框架和内容出现; 使用当前颜色组的浅色和深色绘制3D凸起线
        # QFrame.Sunken  # 框架和内容出现凹陷; 使用当前颜色组的浅色和深色绘制3D凹陷线
        
        # self.frame.setFrameShadow(QFrame.Plain)
        # self.frame.setFrameShadow(QFrame.Raised)
        # self.frame.setFrameShadow(QFrame.Sunken)
        # ****************设置框架阴影****************** 结束
        
        # ****************设置框架线宽****************** 开始
        # setLineWidth(int width)  # 设置外线宽度
        # lineWidth()  # 获取外线宽度
        # setMidLineWidth(int width)  # 设置中线宽度（部分框架形状，设置框架中线宽度是没用的）
        # midLineWidth()  # 获取中线宽度
        # frameWidth()  # 获取总宽度
        
        self.frame.setLineWidth(5)
        self.frame.setMidLineWidth(12)
        
        # ****************设置框架线宽****************** 结束
        
        # ****************设置框架样式****************** 开始
        # 相关枚举
        # Box = 1
        # HLine = 4
        # NoFrame = 0
        # Panel = 2
        # Plain = 16
        # Raised = 32
        # Shadow_Mask = 240
        # Shape_Mask = 15
        # StyledPanel = 6
        # Sunken = 48
        # VLine = 5
        # WinPanel = 3
        
        self.frame.setFrameStyle(QFrame.Panel | QFrame.Raised)       
        
        # 相当于 
        # frame.setFrameShape(QFrame.Box)
        # frame.setFrameShadow(QFrame.Raised)
        
        # ****************设置框架样式****************** 结束
        
        # ****************框架矩形****************** 开始
        self.frame.setFrameRect(QRect(20,20,60,60))
        
        # ****************框架矩形****************** 结束
    

class MyWindow(MyWidget):
    
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setStyleSheet("""
            QFrame {
                background-color: blue;
                border: 1px solid red;
            }
        """)
        

if __name__=="__main__":
    app=QApplication(sys.argv)
    w = QWidget()
    w.resize(600, 400)
    
    m = MyWindow(w)
    m.resize(m.sizeHint())
    
    w.show()
    m.show()
    app.exit(app.exec())