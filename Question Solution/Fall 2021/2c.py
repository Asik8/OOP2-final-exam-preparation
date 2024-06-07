class Base1:
    def method1(self):
        print("Method1 from Base1")

class Base2:
    def method2(self):
        print("Method2 from Base2")

class Derived(Base1, Base2):
    def method3(self):
        print("Method3 from Derived")

obj = Derived()
obj.method1()
obj.method2()
obj.method3()
