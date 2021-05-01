# encoding-utf-8
import pandas as pd
import numpy as np
# 三种导入数据方式
# 通过标准的Python库导入CSV文件。
from csv import reader
import numpy as np

# 使用标准的Python类库导入CSV数据
filename = '../../dataset/abalone/abalone.data'
def load1():

    with open(filename, 'rt') as raw_data:
        readers = reader(raw_data, delimiter=',')
        x = list(readers)
        data = np.array(x)
        print(data.shape)
load1()
# 通过NumPy导入CSV文件
from numpy import loadtxt
def load2():
    with open(filename, 'rt') as raw_data:
        data = loadtxt(raw_data, delimiter=',')
        print(data.shape)

# 通过Pandas导入CSV文件。
from pandas import read_csv
def load3():
    filename = 'pima_data.csv'
    names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
    data = read_csv(filename, names=names)
    print(data.shape)