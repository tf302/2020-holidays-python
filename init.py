# 创建类
class Calculator:

    #构造函数
    def __init__(self,name,price,width,high):
        self.n=name
        self.p=price
        self.w=width
        self.h=high

    #方法 +
    def add(self,a,b):
        result = a + b
        print("Add is ")
        print(result)

    #方法 -
    def minus(self,a,b):
        result = a - b
        print("Minus is ")
        print(result)

c=Calculator("Bad calculator",100,50,30)
print(c.p)


#_init_(self,) 构造函数
#https://www.cnblogs.com/Taxus215/p/9486527.html