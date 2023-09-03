
class Widget:

    def __init__(self) -> None:
        print("widget init")

    def setLayout(self):
        print(self, "set layout")

    
class HLayout:

    def __init__(self) -> None:
        print("hlayout init")

    def addWidget(self):
        print(self, "add H widget")
    
    def setLayout(self):
        print(self, "set H layout")

class VLayout:

    def __init__(self) -> None:
        print("vlayout init")

    def addWidget(self):
        print(self, "add V widget")
    
    def setLayout(self):
        print(self, "set V layout")


class Mix(Widget, HLayout):
    """
    继承顺序：
    构造函数不重新，会执行第1个类的构造函数
    继承的2个类存在重复的方法，会执行第1个类的方法
    动态继承：
    
    """
    def __init__(self) -> None:
        super().__init__()      # 这样写会执行第1个类的构造函数（按照查找顺序，如果没有会往下查找，所以推荐使用super ）
        HLayout.__init__(self)   # 如果想调用制定类的构造函数或方法，直接使用类名即可，但是需要传入self

m = Mix()
m.addWidget()
m.setLayout()
print(isinstance(m, Widget))
print(isinstance(m, HLayout))

# 动态继承类，创建工厂函数
def createClass(layout_type):
    class MixClass(Widget, HLayout if layout_type=="row" else VLayout):
        def __init__(self) -> None:
            super().__init__()
            super().addWidget()
    return MixClass()


m = createClass("row")  # 打印 add H widget
m = createClass("col")  # 打印 add V widget