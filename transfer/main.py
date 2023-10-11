import sys

from PySide6.QtWidgets import QApplication, QStyleFactory, QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon
import qtawesome as qta

from widgets.main_window import MainWindow


import platform
if platform.system() == "Windows":  # Windows / Linux / Darwin(MacOS)
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("my-secret-appid")  # windows平台任务栏图标同窗体图标


if __name__ == "__main__":
    
    app = QApplication(sys.argv)  # 支持命令行启动传参，提高可扩展性
    # app.setWindowIcon(QIcon(":ego_logo.png"))
    # app.setWindowIcon(QIcon(":svgs/JSON-LD.svg"))
    app.setWindowIcon(qta.icon("msc.terminal-debian"))
    window = MainWindow()
    
    # 当前平台自带的风格，'Windows', 'Fusion' 太丑了，没人会用
    # list_style = QStyleFactory.keys()  # 当前平台支持的 QStyle 窗口风格样式, 默认vista ['windowsvista', 'Windows', 'Fusion']
    # print(list_style)
    # app.setStyle(QStyleFactory.create(list_style[0]))  # 给 App 设置窗口风格, 其他Widget默认(无设置)使用App的风格

    # # 创建系统托盘图标
    # tray_icon = QSystemTrayIcon(QIcon(":logo.png"), app)
    # # 创建托盘菜单
    # menu = QMenu()
    # action = menu.addAction("Open")
    # action = menu.addAction("Exit")
    # tray_icon.setContextMenu(menu)
    # # 显示系统托盘图标
    # tray_icon.show()
    
    # 1. pip install qtmodern，还可以，就是input文字也是黑的，看不清。不再维护
    # import qtmodern.styles
    # import qtmodern.windows
    # qtmodern.styles.light(app)
    # mw = qtmodern.windows.ModernWindow(window)
    # mw.show()
    
    # 2. pip install pyqtdarktheme，白色主题还不错。还在维护
    # import qdarktheme
    # qdarktheme.setup_theme("light")  # dark, light, auto
    
    # 3. pip install qdarkstyle，一般
    # import qdarkstyle
    # app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside'))
    
    # 4. pip install qt-material，感觉好丑，主要间距太宽
    # from qt_material import apply_stylesheet
    # apply_stylesheet(app, theme='light_blue.xml')
    
    window.show()
    sys.exit(app.exec())
