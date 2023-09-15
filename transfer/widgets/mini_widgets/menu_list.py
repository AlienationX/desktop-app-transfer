from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import qtawesome as qta

from transfer.widgets.mini_widgets.addons_widget import HContainer
from transfer.widgets.pages import ExcelToCsvWidget, ExcelSplitWidget, CsvToExcelWidget, WordToPDFWidget, DocumentWidget
import sys

class MenuList(QWidget):
    
    """列表菜单，支持二级菜单"""
    
    def __init__(self):
        super().__init__()
        self.resize(300, 400)
        
        self.menus = [
            {"id":  0, "pid": -1, "expended": False, "objectName": "home", "text": "HOME", "icon": "ri.menu-fill", "class": DocumentWidget()},
            {"id":  1, "pid": -1, "expended": False, "objectName": "excel", "text": "EXCEL", "icon": "ri.file-excel-2-line", "class": ""},
            {"id":  2, "pid":  1, "expended": False, "objectName": "ExcelToCsvWidget", "text": "转换成CSV", "icon": "msc.bookmark", "class": ExcelToCsvWidget()},
            {"id":  3, "pid":  1, "expended": False, "objectName": "ExcelSplitWidget", "text": "文件拆分", "icon": "msc.bookmark", "class": ExcelSplitWidget()},
            # {"id":  4, "pid":  1, "expended": False, "objectName": "ExcelOverviewWidget", "text": "数据概况", "icon": "msc.bookmark", "class": ExcelOverviewWidget()},
            {"id":  5, "pid": -1, "expended": False, "objectName": "word", "text": "WORD", "icon": "ri.file-word-2-line", "class": ""},
            {"id":  6, "pid":  5, "expended": False, "objectName": "WordToPDFWidget", "text": "转换成PDF", "icon": "msc.bookmark", "class": WordToPDFWidget()},
            {"id":  7, "pid": -1, "expended": False, "objectName": "csv", "text": "CSV", "icon": "msc.go-to-file", "class": ""},
            {"id":  8, "pid":  7, "expended": False, "objectName": "CsvToExcelWidget", "text": "转换成EXCEL", "icon": "msc.bookmark", "class": CsvToExcelWidget()},
            {"id":  9, "pid": -1, "expended": False, "objectName": "file", "text": "FILE", "icon": "msc.go-to-file", "class": ""},
            {"id": 10, "pid":  9, "expended": False, "objectName": "file_todo1", "text": "批量重命名", "icon": "msc.bookmark", "class": ""},
            {"id": 11, "pid":  9, "expended": False, "objectName": "file_todo1", "text": "批量替换", "icon": "msc.bookmark", "class": ""},
            {"id": 11, "pid":  9, "expended": False, "objectName": "file_todo1", "text": "批量替换", "icon": "msc.bookmark", "class": ""},
            {"id": 11, "pid":  9, "expended": False, "objectName": "file_todo1", "text": "批量替换", "icon": "msc.bookmark", "class": ""},
            {"id": 11, "pid":  9, "expended": False, "objectName": "file_todo1", "text": "批量替换", "icon": "msc.bookmark", "class": ""},
            {"id": 11, "pid":  9, "expended": False, "objectName": "file_todo1", "text": "批量替换", "icon": "msc.bookmark", "class": ""},
            {"id": 11, "pid":  9, "expended": False, "objectName": "file_todo1", "text": "批量替换", "icon": "msc.bookmark", "class": ""},
            {"id": 11, "pid":  9, "expended": False, "objectName": "file_todo1", "text": "批量替换", "icon": "msc.bookmark", "class": ""},
            {"id": 11, "pid":  9, "expended": False, "objectName": "file_todo1", "text": "批量替换", "icon": "msc.bookmark", "class": ""},
            {"id": 11, "pid":  9, "expended": False, "objectName": "file_todo1", "text": "批量替换", "icon": "msc.bookmark", "class": ""},
            {"id": 11, "pid":  9, "expended": False, "objectName": "file_todo1", "text": "批量替换", "icon": "msc.bookmark", "class": ""},
            {"id": 11, "pid":  9, "expended": False, "objectName": "file_todo1", "text": "批量替换", "icon": "msc.bookmark", "class": ""},
            {"id": 11, "pid":  9, "expended": False, "objectName": "file_todo1", "text": "批量替换", "icon": "msc.bookmark", "class": ""},
            {"id": 11, "pid":  9, "expended": False, "objectName": "file_todo1", "text": "批量替换", "icon": "msc.bookmark", "class": ""},
            {"id": 11, "pid":  9, "expended": False, "objectName": "file_todo1", "text": "批量替换", "icon": "msc.bookmark", "class": ""},
            {"id": 11, "pid":  9, "expended": False, "objectName": "file_todo1", "text": "批量替换", "icon": "msc.bookmark", "class": ""},
            {"id": 11, "pid":  9, "expended": False, "objectName": "file_todo1", "text": "批量替换", "icon": "msc.bookmark", "class": ""},
            {"id": 11, "pid":  9, "expended": False, "objectName": "file_todo1", "text": "批量替换", "icon": "msc.bookmark", "class": ""},
        ]
        
        self.listWidget = QListWidget()
        self.listWidget.setObjectName("leftMenu")
        for i in range(len(self.menus)):
            menu_item = self.menus[i]

            list_item = QListWidgetItem()
            list_item.setSizeHint(QSize(220, 32))  # 必须设置大小，否则显示不出来

            list_item._data = menu_item  # 每个对象添加_data属性简化遍历和查找

            listWidgetHContainer = HContainer()
            if menu_item["pid"] == -1:
                list_item.leftIcon = QLabel()
                list_item.leftIcon.setStyleSheet("margin-left: 10px")
                list_item.leftIcon.setPixmap(qta.icon(menu_item["icon"], color=QColor(200, 200, 200)).pixmap(QSize(20, 20)))
                listWidgetHContainer.addWidget(list_item.leftIcon)
                listWidgetHContainer.addWidget(QLabel(menu_item["text"]))
                listWidgetHContainer.addStretch()
                if menu_item["text"] != "HOME":
                    list_item.rightIcon = QLabel()
                    list_item.rightIcon.setPixmap(qta.icon("msc.chevron-down", color=QColor(200, 200, 200)).pixmap(QSize(16, 16)))
                    # list_item.rightIcon.setStyleSheet("margin-right: 10px")
                    listWidgetHContainer.addWidget(list_item.rightIcon)
            else:
                textLable = QLabel(menu_item["text"])
                textLable.setStyleSheet("margin-left: 34px")
                listWidgetHContainer.addWidget(textLable)

            self.listWidget.addItem(list_item)
            self.listWidget.setItemWidget(list_item, listWidgetHContainer)  # addItem 和 setItemWidget 必须一起使用
            
            if menu_item["pid"] != -1:
                list_item.setHidden(True)
            
        self.layout = HContainer()
        self.layout.addWidget(self.listWidget)
        self.setLayout(self.layout)
        
        self.setStyleSheet("""
            QWidget {
                border-radius: 5px;
                background-color: rgb(31, 31, 31);
                color: rgb(200, 200, 200);
                font-size: 13px;
            }
            QListView {
                outline: none;  /* 禁用被选中的虚线 */
            }
            QListView::item:hover {
                background-color: rgb(4, 57, 94);
            }
            QListView::item:selected {
                border-left: 5px solid rgb(30, 74, 28);
                background-color: rgb(58, 46, 86);
            }
            QListView QWidget {
                background-color: transparent;  /* 重点，设置为透明 */
                border-radius: 0px;
                color: rgb(200, 200, 200);
            }
        """)
        
        self.listWidget.itemClicked.connect(self.change)
        
    def change(self, item):
        # for label in self.listWidget.itemWidget(item).findChildren(QLabel):
        #     print(label)
        print(item._data)
        if item._data["text"] != "HOME" and item._data["pid"] == -1 and item._data["expended"] == True:
            item.rightIcon.setPixmap(qta.icon("msc.chevron-down", color=QColor(200, 200, 200)).pixmap(QSize(16, 16)))
            item._data["expended"] = False
        elif item._data["text"] != "HOME" and item._data["pid"] == -1 and item._data["expended"] == False:
            item.rightIcon.setPixmap(qta.icon("msc.chevron-up", color=QColor(200, 200, 200)).pixmap(QSize(16, 16)))
            item._data["expended"] = True
        
        for i in range(self.listWidget.count()):
            list_item = self.listWidget.item(i)
            if list_item._data["pid"] == item._data["id"]:
                if item._data["expended"] == True:
                    list_item.setHidden(False)
                else:
                    list_item.setHidden(True)
                
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    m=MenuList()
    m.show()
    app.exit(app.exec())