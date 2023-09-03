class Parent:
    pass

class Child(Parent):
    pass

class Boy:
    pass

# 动态继承
DynamicChild = type("DynamicChild", (Child, Boy), {})

print(DynamicChild.__bases__)  # 返回第一级的继承类
print(DynamicChild.__mro__)    # 按照顺序返回所有继承类

# (<class '__main__.Child'>, <class '__main__.Boy'>)
# (<class '__main__.DynamicChild'>, <class '__main__.Child'>, <class '__main__.Parent'>, <class '__main__.Boy'>, <class 'object'>)

#  但是也需要创建工厂函数？
