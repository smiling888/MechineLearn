- 平均绝对误差（Mean Absolute Error，MAE）。
平均绝对误差是所有单个观测值与算术平均值的偏差的绝对值的平均值。与平均误差相比，平均绝对误差由于离差被绝对值化，不会出现正负相抵消的情况，因而，平均绝对误差能更好地反映预测值误差的实际情况。

- 均方误差（Mean Squared Error，MSE）。
均方误差是衡量平均误差的方法，可以评价数据的变化程度。均方根误差是均方误差的算术平方根。均方误差的值越小，说明用该预测模型描述实验数据的准确度越高

- 决定系数（ଶ）'
R2:反映因变量的全部变异能通过回归关系被自变量解释的比例。拟合优度越大，自变量对因变量的解释程度越高，自变量引起的变动占总变动的百分比越高，观察点在回归直线附近越密集。

公式：R2=SSR/SST=1-SSE/SST
SST (total sum of squares)：总平方和
SSR (regression sum of squares)：回归平方和
SSE (error sum of squares) ：残差平方和。
R^2=81%，因变量Y的81%变化由我们的自变量X来解释。
R^2 的缺陷：当我们人为的向系统中添加过多的自变量，SSE会减少，从而R^2变大。因此我们采用校正R方，惩罚了过多无意义的自变量：
https://upload-images.jianshu.io/upload_images/9640232-bdb219b01cee4afb.png?imageMogr2/auto-orient/strip|imageView2/2/format/webp