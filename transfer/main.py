# 导入sys
import sys

from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon
from widgets.main_window import MainWindow

# import ctypes
# ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("my-secret-appid")  # 任务栏图标同窗体图标

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MainWindow()
    
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
    # qtmodern.styles.dark(app)
    # mw = qtmodern.windows.ModernWindow(window)
    # mw.show()
    
    # 2. pip install pyqtdarktheme，白色主题还不错。还在维护
    import qdarktheme
    qdarktheme.setup_theme("light")  # dark, light, auto
    
    # 3. pip install qdarkstyle，一般
    # import qdarkstyle
    # app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside'))
    
    # 4. pip install qt-material，感觉好丑，主要间距太宽
    # from qt_material import apply_stylesheet
    # apply_stylesheet(app, theme='light_blue.xml')
    
    window.show()
    sys.exit(app.exec())
