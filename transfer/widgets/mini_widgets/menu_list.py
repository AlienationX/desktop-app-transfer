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
        self.resize(300, 600)
        
        self.menus = [
            {"id": 0, "objectName": "home", "text": "HOME", "icon": "mdi.menu-open", "class": "DocumentWidget()", "pid": -1},
            {"id": 1, "objectName": "excel", "text": "EXCEL", "icon": "ri.file-excel-2-line", "class": "", "pid": -1},
            {"id": 2, "objectName": "ExcelToCsvWidget", "text": "转换成CSV", "icon": "msc.bookmark", "class": "ExcelToCsvWidget()", "pid": 1},
            {"id": 3, "objectName": "ExcelSplitWidget", "text": "文件拆分", "icon": "msc.bookmark", "class": "ExcelSplitWidget()", "pid": 1},
            # {"id": 4, "objectName": "ExcelOverviewWidget", "text": "数据概况", "icon": "msc.bookmark", "class": ExcelOverviewWidget(), "pid": 1},
            {"id": 5, "objectName": "word", "text": "WORD", "icon": "ri.file-word-2-line", "class": "", "pid": -1},
            {"id": 6, "objectName": "WordToPDFWidget", "text": "转换成PDF", "icon": "msc.bookmark", "class": "WordToPDFWidget()", "pid": 5},
            {"id": 7, "objectName": "csv", "text": "CSV", "icon": "msc.go-to-file", "class": "", "pid": -1},
            {"id": 8, "objectName": "CsvToExcelWidget", "text": "转换成EXCEL", "icon": "msc.bookmark", "class": "CsvToExcelWidget()", "pid": 7},
            {"id": 9, "objectName": "file", "text": "FILE", "icon": "msc.go-to-file", "class": "", "pid": -1},
            {"id": 10, "objectName": "file_todo1", "text": "批量重命名", "icon": "msc.bookmark", "class": "", "pid": 9},
            {"id": 11, "objectName": "file_todo1", "text": "批量替换", "icon": "msc.bookmark", "class": "", "pid": 9},
        ]
        
        self.listWidget = QListWidget()
        self.listWidget.setMinimumWidth(260)
        self.listWidget.setObjectName("leftMenu")
        for i in range(len(self.menus)):
            item = self.menus[i]

            list_item = QListWidgetItem()
            list_item.setSizeHint(QSize(200, 32))  # 必须设置大小，否则显示不出来

            list_item.leftIcon = QLabel()
            list_item.leftIcon.setPixmap(qta.icon(item["icon"], color=QColor(200, 200, 200)).pixmap(QSize(20, 20)))
            list_item.rightIcon = QLabel()
            list_item.rightIcon.setPixmap(qta.icon("msc.chevron-down", color=QColor(200, 200, 200)).pixmap(QSize(20, 20)))
            
            listWidgetHContainer = HContainer()
            listWidgetHContainer.addWidget(list_item.leftIcon)
            listWidgetHContainer.addWidget(QLabel(item["text"]))
            listWidgetHContainer.addStretch()
            listWidgetHContainer.addWidget(list_item.rightIcon)
            
            self.listWidget.addItem(list_item)
            self.listWidget.setItemWidget(list_item, listWidgetHContainer)  # addItem 和 setItemWidget 必须一起使用
            
            if item["pid"] != -1:
                list_item.setHidden(True)
            
        self.layout = HContainer()
        self.layout.addWidget(self.listWidget)
        self.layout.addWidget(QPushButton("ok"))
        self.setLayout(self.layout)
        
        self.setStyleSheet("""
            QWidget {
                border-radius: 0px;
                background-color: rgb(41, 41, 41);
                color: rgb(200, 200, 200);
            }
            QPushButton {
                background-color: rgb(50, 50, 50);
            }
            QListView {
                outline: none;  /* 禁用被选中的虚线 */
            }
            QListView::item:hover {
                background-color: rgb(20, 113, 145);
            }
            QListView::item:selected {
                border-left: 5px solid rgb(218, 112, 214);
                background-color: rgb(4, 57, 94);
            }
            QListView QWidget {
                background-color: transparent;  /* 重点，设置为透明 */
                border-radius: 0px;
                color: rgb(200, 200, 200);
            }
        """)
        
        self.listWidget.itemClicked.connect(self.change)
        
    def change(self, item):
        print(item)
        print(self.listWidget.itemWidget(item))
        for label in self.listWidget.itemWidget(item).findChildren(QLabel):
            print(label)
            
        item.rightIcon.setPixmap(qta.icon("msc.chevron-up", color=QColor(200, 200, 200)).pixmap(QSize(20, 20)))
            
        # for i in range(len(self.menus)):
        #     menu_item = self.menus[i]
        #     if item["pid"] == -1:
        #         self.listWidget.itemWidget(menu_item).findChildren(QLabel)[2].setPixmap(qta.icon("msc.chevron-up", color=QColor(200, 200, 200)).pixmap(QSize(20, 20)))
                
                
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    m=MenuList()
    m.show()
    app.exit(app.exec())