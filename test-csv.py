
import csv
with open("mytest.csv",'a') as file:

    #file.write('hahahah')     #文件的形式写入

#读取数据
    #result = csv.reader(file)
    #print(result)
    #for content in result:
     #   print(content )

#写入
    writer = csv.writer(file) #writer是实例化对象
    writer.writerow(['特','特特','特特特'])#writerow()是写入的方法，括号内的数据是列表形式

