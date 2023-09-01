class A:

    def foo(self):
        print("A's foo")

class B(A):
    pass

class C(A):

    def foo(self):
        print("C's foo")

class D(B, C):
    pass

d = D()

# Python中多继承的顺序是基于MRO (Method Resolution Order)算法来确定的。
# MRO算法会从当前类的类树中按照广度优先的顺序搜索要继承的方法和属性，每个类只会被搜索一次。
# MRO算法的具体实现称为C3算法，它结合了DFS和BFS算法的优点，保证了搜索的稳定性和一致性。
# 当出现多个父类时，子类继承属性或方法的优先级是按照类树的拓扑序列来决定的
d.foo()  # 返回C的foo，广度优先，然后再深度查找