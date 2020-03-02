from matplotlib import pyplot as plt
import numpy as np

'''
x = range(2,26,2)
y = [15,13,24,10,6,9,2,23,12,15,16,9]

#绘图
plt.plot(x,y)

#展示图形
plt.show()
'''

x = np.linspace(-5,5,50)
y1= 2*x + 1
y2 = x**2
'''
plt.figure()
plt.plot(x,y1)
plt.show()
'''
plt.figure()
plt.plot(x,y1,color='red',linestyle='--')
#quxian
plt.xlim((0,5))
plt.ylim((0,5))
#biaoqian
plt.xlabel('$time$')
plt.ylabel('$distance$')

plt.show()

