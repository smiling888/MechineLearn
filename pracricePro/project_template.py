# Python机器学习项目模版
import numpy as np
from matplotlib import pyplot
from pandas import read_csv
from pandas.plotting import scatter_matrix
from pandas import set_option
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier

# 1. 准备
# a) 导入类库
# b) 导入数据集

# 2. 理解数据
# a) 描述性统计
# b) 数据可视化

# 3. 数据准备
# a) 数据清洗
# b) 特征选择
# c) 数据转换


#- 通过删除重复数据、标记错误数值，甚至标记错误的输入数据来清洗数据。特征选择，包括移除多余的特征属性和增加新的特征属性。数据转化，对数据尺度进行调整，或者调整数据的分布，以便更好地展示问

# 4. 评估算法
# a) 分离数据集
# b) 评估选项和评估矩阵
# c) 算法审查
# d) 算法比较

# 5. 改善模型
# a) 算法调参
# b) 集成算法

# 6. 结果部署
# a) 预测评估数据集
# b) 利用整个数据集生产模型
# c) 序列化模型