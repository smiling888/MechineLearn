# encoding-utf-8
import numpy as np

# 创建数组
myarr=np.array([[1,2,3],[1,2,3],[1,2,3]])
myarr2=np.array([[1,2,3],[1,2,3],[1,2,3]])
print(myarr)
# 访问数据
print(myarr[0][0])
print(myarr[1])
# 计算
print(myarr+myarr2)
print(myarr*myarr2)