#类的模版
class Dog:

    #构造方法
    def __init__(self,name,weight,power):
        self.name = name
        self.weight =weight
        self.power = power
        self.blood = 10
    #方法
    def attack(self):
        print(f'名字{self.name},体重{self.weight}能量{self.power}')

#类的实例化
d1 = Dog('大黄',15,100)
d2 = Dog('小牛',30,80)

# #访问属性   实例名.属性
print(d1.name,d1.weight)
print(d2.name,d2.weight)
print(d1.blood)
print(d2.blood)

#访问方法  实例名.方法名（）
d1.attack()