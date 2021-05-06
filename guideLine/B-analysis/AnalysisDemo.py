
# 7个维度查看数据
# 简单地查看数据。
from pandas import read_csv
# 显示数据的行和列数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
print(data.dtypes)
#其他
data.columns                     # 查看数据列名
data.shape                       # 查看数据框中有多少个观测值
data.head(4)                     # 打印数据的前四行
data.head(4)['Rings']            # 打印前四行中Rings的值
data.tail(3)                     # 提取数据集的最后三行
data.tail(3)['Weight']           # 输出最后三行鲍鱼的重量
data.loc[577]['Diameter']        # 输出第577行的直径值
data.mean()['Height']            # 输出高度列的平均值


# 审查数据的维度。
# 显示数据的行和列数据
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
print(data.shape)

# 审查数据的类型和属性。
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
print(data.dtypes)

# 总结查看数据分类的分布情况。
data = read_csv(filename, names=names)
print(data.groupby('class').size())

# 通过描述性统计分析数据。
from pandas import set_option
data = read_csv(filename, names=names)
set_option('display.width', 100)
# 设置数据的精确度
set_option('precision', 4)
print(data.describe())

# 理解数据属性的相关性。
# 显示数据的相关性
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
set_option('display.width', 100)
# 设置数据的精确度
set_option('precision', 2)
print(data.corr(method='pearson'))

# 审查数据的分布状况。
# 计算数据的高斯偏离-通过分析数据的高斯分布情况来确认数据的偏离情况
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
print(data.skew())
