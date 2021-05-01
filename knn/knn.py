# #encoding-utf-8
#
# from numpy import *
# import operator
#
# def createdataSet():
#     group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
#     labels=['A','A','B','B']
#     return group,labels
#
# def classify0(inX,dataSet,labels,k):
#     dataSetSize=dataSet.shape[0]
#     diffmat=tile(inX,(dataSetSize,1))-dataSet
#     sqlDiffMat=diffmat**2
#     distances=sqlDiffMat.sum(axis=1)
#     sortedDistIndices=distances.argsort()
#     classCount={}
#     for i in range(k):
#         votelabel=labels[sortedDistIndices[i]]
#         classCount[votelabel]=classCount.get(votelabel,0)+1
#     sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
#     return sortedClassCount[0][0]
#
#
# group,labels=createdataSet()
#
# print classify0([1,2],group,labels,3)
#
# print group
# print labels
#
#
#
#
#
#
