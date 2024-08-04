# 3. Write a program to perform multiple inheritance.

class Parent1:
    def __init__(self):
        self.str1 = "Parent1"
        print("Parent1 Constructor")

    def method1(self):
        print("Method from Parent1")

class Parent2:
    def __init__(self):
        self.str2 = "Parent2"
        print("Parent2 Constructor")

    def method2(self):
        print("Method from Parent2")


class Child(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)
        print("Child Constructor")

    def child_method(self):
        print("Method from Child")


child_object = Child()


child_object.method1()
child_object.method2()
child_object.child_method()

print(child_object.str1)
print(child_object.str2)
