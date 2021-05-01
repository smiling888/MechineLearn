#encoding-utf-8
# 鸢尾花 -项目
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

filename = 'iris2.csv'
names = ('separx-length', 'separx-width', 'petal-length', 'petal-width', 'class')


# 1）导入数据。
dataset=None
def loadData():
    # DataFrame类型
    global dataset
    dataset = read_csv(filename,names=names)
    print(dataset)
loadData()

# （2）概述数据。
def descriedata():
    # 1）数据的维度。
    dataset.shape
    # 2）查看数据自身。dataset.head(10)
    # 3）统计描述所有的数据特征。
    dataset.describe()
    # （4）数据分类的分布情况
    # 不同分类数据数量
    dataset.groupby('class').size()

    # （3）数据可视化。
    # 1-单变量可视化
    # 箱线图
    dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
    pyplot.show()

    # 直方图
    dataset.hist()
    pyplot.show()

    # 散点矩阵图
    scatter_matrix(dataset)
    pyplot.show()
# （4）评估算法。
def pinggusuanfa():
    # 1）分离出评估数据集
    # ndarray
    array = dataset.values
    X = array[:, 0:4]
    Y = array[:, 4]
    validation_size = 0.2
    seed = 7
    # 随机划分样本数据为训练集和测试集的
    X_train, X_validation, Y_train, Y_validation = \
        train_test_split(X, Y, test_size=validation_size, random_state=seed)
    print(len(X_train))

    # 2）采用10折交叉验证来评估算法模型。
    # 算法审查
    models = {}
    models['LR'] = LogisticRegression()
    models['LDA'] = LinearDiscriminantAnalysis()
    models['KNN'] = KNeighborsClassifier()
    models['CART'] = DecisionTreeClassifier()
    models['NB'] = GaussianNB()
    models['SVM'] = SVC()
    # 评估算法
    results = []
    for key in models:
        kfold = KFold(n_splits=10, random_state=seed)
        cv_results = cross_val_score(models[key], X_train, Y_train, cv=kfold, scoring='accuracy')
        results.append(cv_results)
        print('%s: %f (%f)' % (key, cv_results.mean(), cv_results.std()))

    # 箱线图比较算法
    fig = pyplot.figure()
    fig.suptitle('Algorithm Comparison')
    ax = fig.add_subplot(111)
    pyplot.boxplot(results)
    ax.set_xticklabels(models.keys())
    pyplot.show()

    # （5）实施预测。
    svm = SVC()
    svm.fit(X=X_train, y=Y_train)
    predictions = svm.predict(X_validation)
    # 算法的准确度
    print(accuracy_score(Y_validation, predictions))
    # 冲突矩阵
    print(confusion_matrix(Y_validation, predictions))
    print(classification_report(Y_validation, predictions))
pinggusuanfa()

# 3）生成6个不同的模型来预测新数据。
# 4）选择最优模型。



# print(dataset)