# 数据预处理-特征工程
# 常用数据转化方法
## 调整数据尺度（Rescale Data）。
 将数据转换成0和1之间的值 .
 MinMaxScaler

## 正态化数据（Standardize Data）。
正态化数据（Standardize Data）是有效的处理符合高斯分布的数据的手段，输出结果以0为中位数，方差为1，并作为假定数据符合高斯分布的算法的输入。
StandardScaler类来进行正态化数据处理

## 标准化数据（Normalize Data）。
标准化数据（Normalize Data）处理是将每一行的数据的距离处理成1（在线性代数中矢量距离为1）的数据又叫作“归一元”处理，适合处理稀疏数据（具有很多为0的数据），归一元处理的数据对使用权重输入的神经网络和使用距离的K近邻算法的准确度的提升有显著作用。
使用scikit-learn中的Normalizer类实现

## 二值数据（Binarize Data）。
二值数据（Binarize Data）是使用值将数据转化为二值，大于阈值设置为1，小于阈值设置为0。这个过程被叫作二分数据或阈值转换。在生成明确值或特征工程增加属性的时候使用，
使用scikit-learn中的Binarizer类实现

格式化数据方法：
- 适合和多重变换（Fit and Multiple Transform）。
- 适合和变换组合（Combined Fit-and-Transform）