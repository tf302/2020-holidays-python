# 创建类
class Calculator:

    #私有属性
    name = "Calculator"
    price = "200$"

    #类方法
    def __init__(self,name,age,sex):
        self.n=name
        self.a=age
        self.s=sex

    #实例方法
    def add(self,a,b):
        result = a + b
        print("Add is ")
        print(result)

    def minus(self,a,b):
        result = a - b
        print("Minus is ")
        print(result)

#类的实例化
caltcu = Calculator("特特",18,"男")
print(caltcu.n)
print(caltcu.s)


#调用add()方法
caltcu.add(5,5)
#调用munus()方法
caltcu.minus(10,5)
