# 1 直方图
from pandas import read_csv
import matplotlib.pyplot as plt
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
data.hist()
plt.show()

#2 密度图
data.plot(kind="density",subplots=True,layout=(3,3),sharex=False)
plt.show()

#3 箱线图
# 画一条中位数线，然后以下四分位数和上四分位数画一个盒子，上下各有一条横线，表示上边缘和下边缘。
# 通过横线来显示数据的伸展状况，游离在边缘之外的点为异常值
data.plot(kind="box",subplots=True,layout=(3,3),sharex=False)
plt.show()