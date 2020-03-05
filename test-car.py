'''1.汽车:
创建一个名为Car的类，其方法__init__() 设置两个属性:name和brand(品牌)。
定义一个名为show()的方法，功能是打印出汽车的名称和品牌。
定义一个名为run()的方法，打印:汽车XX跑起来了。其中XX表示汽车的name.
根据这个类创建一个名为car的实例，先通过属性直接打印其两个属性，再调用上面的两个方法。'''

class Car:
    def __init__(self,name,brand):
        self.name = name
        self.brand = brand
    def show(self):
        print(f'该汽车的名字：{self.name} 品牌为：{self.brand}')

#类的实例化
car1 = Car('亚洲龙','丰田')
car2 = Car('雅阁  ','丰=本田')
car3 = Car('a4   ','奥迪')
#通过属性打印
print(car1.name,car1.brand)
#通过方法打印
car1.show()
car2.show()
car3.show()




