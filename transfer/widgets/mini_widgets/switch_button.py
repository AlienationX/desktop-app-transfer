from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import qtawesome as qta

class SwitchButton(QPushButton):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.state = False  # 按钮状态：True表示开，False表示关
        self.icon_map = {
            True: qta.icon("mdi.toggle-switch", color=QColor(76, 175, 80)),
            False: qta.icon("mdi.toggle-switch-off", color=QColor(137, 137, 137))
        }
        
        self.setIcon(self.icon_map[self.state])
        self.setIconSize(QSize(100, 50))
        self.setFixedSize(50, 26)
        self.setStyleSheet("border: 0;")
        
        self.clicked.connect(self.changeState)
    
    def re_size(self, width, height):
        self.setFixedSize(width, height)
    
    @Slot()
    def changeState(self):
        self.state = not self.state
        self.setIcon(self.icon_map[self.state])
        
class _MySwitchButton1(QPushButton):
    """自定义Switch按钮"""

    def __init__(self, parent=None):
        super().__init__(parent)

        # 设置无边框和背景透明
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.resize(70, 30)
        self.state = False  # 按钮状态：True表示开，False表示关
        
        self.setStyleSheet("""
            border: 0px;
        """)

    def mousePressEvent(self, event):
        """鼠标点击事件：用于切换按钮状态"""
        super().mousePressEvent(event)

        self.state = False if self.state else True
        self.update()

    def paintEvent(self, event):
        """绘制按钮"""
        super(SwitchButton, self).paintEvent(event)

        # 创建绘制器并设置抗锯齿和图片流畅转换
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

        # 定义字体样式
        # font = QFont('Microsoft YaHei')
        # font.setPixelSize(13)
        # painter.setFont(font)

        # 开关为开的状态
        if self.state:
            # 绘制背景
            painter.setPen(Qt.NoPen)
            brush = QBrush(QColor('#FF475D'))
            painter.setBrush(brush)
            painter.drawRoundedRect(0, 0, self.width(), self.height(), self.height() // 2, self.height() // 2)

            # 绘制圆圈
            painter.setPen(Qt.NoPen)
            brush.setColor(QColor('#ffffff'))
            painter.setBrush(brush)
            painter.drawRoundedRect(43, 3, 24, 24, 12, 12)

            # 绘制文本
            painter.setPen(QPen(QColor('#ffffff')))
            painter.setBrush(Qt.NoBrush)
            painter.drawText(QRect(18, 4, 50, 20), Qt.AlignLeft, 'on')
        # 开关为关的状态
        else:
            # 绘制背景
            painter.setPen(Qt.NoPen)
            brush = QBrush(QColor('#FFFFFF'))
            painter.setBrush(brush)
            painter.drawRoundedRect(0, 0, self.width(), self.height(), self.height()//2, self.height()//2)

            # 绘制圆圈
            pen = QPen(QColor('#999999'))
            pen.setWidth(1)
            painter.setPen(pen)
            painter.drawRoundedRect(3, 3, 24, 24, 12, 12)

            # 绘制文本
            painter.setBrush(Qt.NoBrush)
            painter.drawText(QRect(38, 4, 50, 20), Qt.AlignLeft, 'off')


class _MySwitchButton2(QPushButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setCheckable(True)
        self.setMinimumWidth(66)
        self.setMinimumHeight(22)
        self.setStyleSheet("""
            border: 0px;
        """)

    def paintEvent(self, event):
        label = "ON" if self.isChecked() else "OFF"
        bg_color = Qt.green if self.isChecked() else Qt.gray

        radius = 10
        width = 32
        center = self.rect().center()

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(center)
        painter.setBrush(QColor(255,255,255))

        pen = QPen(Qt.black)
        pen.setWidth(1)
        painter.setPen(pen)

        painter.drawRoundedRect(QRect(-width, -radius, 2*width, 2*radius), radius, radius)
        painter.setBrush(QBrush(bg_color))
        sw_rect = QRect(-radius, -radius, width + radius, 2*radius)
        if not self.isChecked():
            sw_rect.moveLeft(-width)
        painter.drawRoundedRect(sw_rect, radius, radius)
        painter.drawText(sw_rect, Qt.AlignCenter, label)


if __name__=="__main__":
    app=QApplication([])
    w = QWidget()
    w.resize(600, 400)
    
    b = SwitchButton(w)
        
    w.show()
    app.exit(app.exec())
