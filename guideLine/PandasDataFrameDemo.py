# encoding-utf-8
import pandas as pd
import numpy as np
# Series：一维数组，与NumPy中的一维Array类似。二者与Python基本的数据结构List也很相近，其区别是：List中的元素可以是不同的数据类型，而Array和Series中则只允许存储相同的数据类型，这样可以更有效地使用内存，提高运算效率。
# Time- Series：以时间为索引的Series。
# DataFrame：二维的表格型数据结构。很多功能与R语言中的data.frame类似。可以将DataFrame理解为Series的容器。
# Panel：三维数组，可以理解为DataFrame的容器。
myarray = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
rowindex = ['row1', 'row2', 'row3']
colname = ['col1', 'col2', 'col3']
mydataframe = pd.DataFrame(data=myarray,
                           index=rowindex, columns=colname)
print(mydataframe)
print('访问col3的数据：')
print(mydataframe['col3'])

print('访问row1的数据：')
print(mydataframe.head(0))
print(mydataframe.head(1))

# http://pandas.pydata.org/pandas-docs/stable/