#numpy的创建array
'''
import numpy as np
a = np.array([10,20,30])
print(a)
'''
#矩阵的相乘
'''
import numpy as np
a = np.array([[1,2],
              [0,1]])
b = np.arange(4).reshape((2,2))
c=np.dot(a,b)
print(c)
'''
