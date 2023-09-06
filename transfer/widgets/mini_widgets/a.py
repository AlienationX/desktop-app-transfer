
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys

class CustomWidget(QWidget):

    def __init__(self, text, *args, **kwargs):
        super(CustomWidget, self).__init__(*args, **kwargs)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(QLineEdit(text, self))
        layout.addWidget(QPushButton('x', self))

    def sizeHint(self):
        # 决定item的高度
        return QSize(200, 40)


class ListView(QListView):

    def __init__(self, *args, **kwargs):
        super(ListView, self).__init__(*args, **kwargs)
        # 模型
        self._model = QStandardItemModel(self)
        self.setModel(self._model)

        # 循环生成10个自定义控件
        for i in range(10):
            item = QStandardItem()
            self._model.appendRow(item)  # 添加item

            # 得到索引
            index = self._model.indexFromItem(item)
            widget = CustomWidget(str(i))
            item.setSizeHint(widget.sizeHint())  # 主要是调整item的高度
            # 设置自定义的widget
            self.setIndexWidget(index, widget)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = ListView()
    w.show()
    sys.exit(app.exec_())