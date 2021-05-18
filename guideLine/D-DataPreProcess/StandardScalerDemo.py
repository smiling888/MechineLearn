import numpy as np

x_np = np.array([[1, -1., 2.],
                 [2, 2., 0.],
                 [3, 2., 0.]])
mean = np.mean(x_np, axis=0)
std = np.std(x_np, axis=0)

print('矩阵初值为：{}'.format(x_np))

print('该矩阵的均值为：{}\n 该矩阵的标准差为：{}'.format(mean, std))
# 公式 xi=(xi-平均值)/标准差
another_trans_data = x_np - mean
another_trans_data = another_trans_data / std
print('标准差标准化的矩阵为：{}'.format(another_trans_data))

from sklearn.preprocessing import StandardScaler  # 标准化工具
import numpy as np

# x_np = np.array([[1.5, -1., 2.],
#                  [2., 0., 0.]])
scaler = StandardScaler()
x_train = scaler.fit_transform(x_np)
print('矩阵初值为：{}'.format(x_np))
print('该矩阵的均值为：{}\n 该矩阵的标准差为：{}'.format(scaler.mean_, np.sqrt(scaler.var_)))
print('标准差标准化的矩阵为：{}'.format(x_train))
