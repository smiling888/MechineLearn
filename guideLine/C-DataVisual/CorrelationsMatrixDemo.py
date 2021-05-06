from pandas import read_csv
import matplotlib.pyplot as plt
import numpy as np
filename = '../../dataset/abalone/abalone.data'
names = ['Sex', 'Length', 'Diameter', 'Height', 'Whole-weight', 'Shucked-weight', 'Viscera-weight', 'Shell-weight', 'Rings']
data = read_csv(filename, names=names)
correlations = data.corr()
# 相关矩阵图
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0, 9, 1)

ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
plt.show()


#散点图
from pandas import read_csv
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
filename = 'pima_data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
scatter_matrix(data)
plt.show()