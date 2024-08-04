# 5. Write a program to perform Addition, Subtraction Operation In Encapsulation. 

class Calculator:
    def __init__(self):
        self.__result = 0 

    def add(self, value):
        self.__result += value

    def subtract(self, value):
        self.__result -= value

    def get_result(self):
        return self.__result

calc = Calculator()

calc.add(10)
print("After adding 10, result is:", calc.get_result())

calc.subtract(4)
print("After subtracting 4, result is:", calc.get_result())
