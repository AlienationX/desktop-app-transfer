from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys
 
app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
window.setWindowTitle('QFrame-功能测试')
 
frame = QFrame(window)
frame.setStyleSheet('background-color: green;')
frame.resize(200, 200)
frame.move(100, 100)
 
# ****************设置框架形状****************** 开始
# setFrameShape(QFrame.Shape)             # 设置框架形状
# QFrame.NoFrame              # QFrame什么都没画
# QFrame.Box                  # QFrame围绕其内容绘制一个框（有边框）（需要设置外线和中线的宽度）
# QFrame.Panel                # QFrame绘制一个面板，使内容显得凸起或凹陷（设置中线宽度没用）
# QFrame.HLine                # QFrame绘制一条没有框架的水平线（用作分隔符）
# QFrame.VLine                # QFrame绘制一条无框架的垂直线（用作分隔符）
# QFrame.StyledPanel          # 绘制一个矩形面板，其外观取决于当前的GUI样式。它可以升起或凹陷。
# QFrame.WinPanel             # 绘制一个可以像Windows 2000中那样凸起或凹陷的矩形面板，对于GUI样式独立性，建议使用StyledPanel。
 
# frame.setFrameShape(QFrame.NoFrame)
# frame.setFrameShape(QFrame.Box)
# frame.setFrameShape(QFrame.Panel)
# frame.setFrameShape(QFrame.HLine)
# frame.setFrameShape(QFrame.VLine)
# frame.setFrameShape(QFrame.StyledPanel)
# frame.setFrameShape(QFrame.WinPanel)
# ****************设置框架形状****************** 结束
 
# ****************设置框架阴影****************** 开始
# setFrameShadow(QFrame.Shadow)  # 设置框架阴影
# QFrame.Plain  # 框架和内容与周围环境呈现水平;（没有任何3D效果）
# QFrame.Raised  # 框架和内容出现; 使用当前颜色组的浅色和深色绘制3D凸起线
# QFrame.Sunken  # 框架和内容出现凹陷; 使用当前颜色组的浅色和深色绘制3D凹陷线
 
# frame.setFrameShadow(QFrame.Plain)
# frame.setFrameShadow(QFrame.Raised)
# frame.setFrameShadow(QFrame.Sunken)
# ****************设置框架阴影****************** 结束
 
# ****************设置框架线宽****************** 开始
# setLineWidth(int width)  # 设置外线宽度
# lineWidth()  # 获取外线宽度
# setMidLineWidth(int width)  # 设置中线宽度（部分框架形状，设置框架中线宽度是没用的）
# midLineWidth()  # 获取中线宽度
# frameWidth()  # 获取总宽度
 
frame.setLineWidth(5)
frame.setMidLineWidth(2)
 
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
 
frame.setFrameStyle(1|32)       
 
# 相当于 
# frame.setFrameShape(QFrame.Box)
# frame.setFrameShadow(QFrame.Raised)
 
# ****************设置框架样式****************** 结束
 
# ****************框架矩形****************** 开始
frame.setFrameRect(QRect(20,20,60,60))
 
# ****************框架矩形****************** 结束
window.show()
sys.exit(app.exec())