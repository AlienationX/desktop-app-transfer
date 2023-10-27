from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class CommonHelper:

    @staticmethod
    def readQssResource(resource_path):
        stream = QFile(resource_path)
        stream.open(QIODevice.ReadOnly)
        return QTextStream(stream).readAll()

    @staticmethod
    def repalceAllColors():
        pass
    
    @staticmethod
    def animation(widget, action, start_x, start_y, end_x, end_y, duration, callback=None):
        anime = QPropertyAnimation(widget, b"geometry")
        anime.setStartValue(QRect(start_x, start_y, widget.width(), widget.height()))
        anime.setEndValue(QRect(end_x, end_y, widget.width(), widget.height()))
        anime.setDuration(duration)
        if action=="hide":
            anime.finished.connect(widget.hide)  # 动画完成后执行隐藏
        elif action=="show":
            anime.finished.connect(widget.show)
        anime.start()
        
    @staticmethod
    def animation_center_show(widget, action, start_x, start_y, end_x, end_y, duration, callback=None):
        anime = QPropertyAnimation(widget, b"geometry")
        anime.setStartValue(QRect(start_x, start_y, widget.width(), widget.height()))
        anime.setEndValue(QRect(end_x, end_y, widget.width(), widget.height()))
        anime.setDuration(duration)
        if action=="hide":
            anime.finished.connect(widget.hide)  # 动画完成后执行隐藏
        elif action=="show":
            anime.finished.connect(widget.show)
        anime.start()