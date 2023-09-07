from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import qtawesome as qta

from addons_widget import HContainer
import sys

class MenuList(QWidget):
    
    """列表菜单，支持二级菜单"""
    
    def __init__(self):
        super().__init__()
        
        self.menus = [
            {"id": 0, "objectName": "home", "text": "HOME", "icon": "mdi.menu-open", "class": "DocumentWidget()", "level": 1},
            {"id": 1, "objectName": "excel", "text": "EXCEL", "icon": "ri.file-excel-2-line", "class": "", "level": 1},
            {"id": 2, "objectName": "ExcelToCsvWidget", "text": "转换成CSV", "icon": "msc.bookmark", "class": "ExcelToCsvWidget()", "level": 2},
            {"id": 3, "objectName": "ExcelSplitWidget", "text": "文件拆分", "icon": "msc.bookmark", "class": "ExcelSplitWidget()", "level": 2},
            # {"id": 4, "objectName": "ExcelOverviewWidget", "text": "数据概况", "icon": "msc.bookmark", "class": ExcelOverviewWidget(), "level": 2},
            {"id": 5, "objectName": "work", "text": "WORD", "icon": "ri.file-word-2-line", "class": "", "level": 1},
            {"id": 6, "objectName": "WordToPDFWidget", "text": "转换成PDF", "icon": "msc.bookmark", "class": "WordToPDFWidget()", "level": 2},
            {"id": 7, "objectName": "csv", "text": "CSV", "icon": "msc.go-to-file", "class": "", "level": 1},
            {"id": 8, "objectName": "CsvToExcelWidget", "text": "转换成EXCEL", "icon": "msc.bookmark", "class": "CsvToExcelWidget()", "level": 2},
            {"id": 9, "objectName": "file", "text": "FILE", "icon": "msc.go-to-file", "class": "", "level": 1},
            {"id": 10, "objectName": "file_todo1", "text": "批量重命名", "icon": "msc.bookmark", "class": "", "level": 2},
        ]
        
        self.listWidget = QListWidget()
        self.listWidget.setMinimumWidth(260)
        self.listWidget.setObjectName("leftMenu")
        for i in range(len(self.menus)):
            item = self.menus[i]
            # list_item = QListWidgetItem(item["text"])
            # list_item.setIcon(qta.icon(item["icon"]))
            # self.listWidget.addItem(list_item)
            
            list_item = QListWidgetItem()
            list_item.setSizeHint(QSize(200, 32))  # 必须设置大小，否则显示不出来

            leftIcon = QLabel()
            leftIcon.setPixmap(qta.icon(item["icon"], color=QColor(200, 200, 200)).pixmap(QSize(20, 20)))
            # leftIcon.setPixmap(QPixmap(":/logo2.ico"))
            rightIcon = QLabel()
            # rightIcon.setPixmap(QPixmap(":/icons/24.svg"))
            # rightIcon.setPixmap(QIcon(":/icons/24.svg").pixmap(QSize(16, 16)))
            rightIcon.setPixmap(qta.icon("msc.chevron-down", color=QColor(200, 200, 200)).pixmap(QSize(20, 20)))
            # rightIcon.setScaledContents(True)  # 自适应
            # rightIcon.setFixedSize(QSize(16, 16))
            
            listWidgetHContainer = HContainer()
            listWidgetHContainer.addWidget(leftIcon)
            listWidgetHContainer.addWidget(QLabel(item["text"]))
            listWidgetHContainer.addStretch()
            listWidgetHContainer.addWidget(rightIcon)
            
            self.listWidget.addItem(list_item)
            self.listWidget.setItemWidget(list_item, listWidgetHContainer)  # addItem 和 setItemWidget 必须一起使用
            
        self.layout = HContainer()
        self.layout.addWidget(self.listWidget)
        self.layout.addWidget(QPushButton("ok"))
        self.setLayout(self.layout)
        
        self.setStyleSheet("""
            QListView {
                border-radius: 0px;
                background-color: rgb(41, 41, 41);
                color: white;
            }
            QListView::item {
                background: green;
                background-color: green;
            }
            QListView::item:alternate {
                background: yellow;
                background-color: yellow;
            }
            QListView::item:hover {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                            stop: 0 #FAFBFE, stop: 1 #DCDEF1);
                background-color: red;
            }
            QListView::item:selected {
                border: 10px solid red;
                background-color: blue;
            }
            # QListView QWidget {
            #     border: 10px solid red;
            # }
        """)
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    m=MenuList()
    m.show()
    app.exit(app.exec())