#排序数字
'''
my_list= []
for i in range(3):
    x = int(input("请输入："))
    my_list.append(x)
my_list.sort(reverse=True)
print(my_list)
'''
#一个列表的数据复制到另一个列表
'''

a = []
b = [3,4,5]
a=b[:]
print(a)
'''
#每隔1秒打印实践 使用模块time（）的 sleep（）函数
'''
import time
print(time.strftime('%Y-%m-%d- %H:%M:%S'),time.localtime(time.time()))
time.sleep(1)
print(time.strftime('%Y-%m-%d- %H:%M:%S'),time.localtime(time.time()))
'''
'''
#水仙花数---各个数字的立方和等于本身
for x in range(1,10):
    for y in range(0,10):
        for z in range(0,10):
            t1 = x*100+y*10+z
            t2 = pow(x,3)+pow(y,3)+pow(z,3)
            if t1 == t2:
                print(t1)
'''
#矩阵相加
'''
a = [[1,2,3],
     [3,4,5],
     [5,6,7]
     ]
b = [[10,2,3],
     [3,40,5],
     [5,6,70]
     ]
c = [[0,0,0],
     [0,0,0],
     [0,0,0]
     ]
for i in  range(3):
    for j in range(3):
        c[i][j] = a[i][j] + b[i][j]
for k in c:
    print(k)'''
#查找字符串的位置 find()
'''
a = "gkhfjlahsf"
b = "l"
print(a.find(b))
'''
