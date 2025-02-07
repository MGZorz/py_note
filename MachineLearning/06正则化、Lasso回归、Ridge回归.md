# 正则化、Lasso回归、Ridge回归

## 过拟合

当样本特征很多，但是样本的数量很少的时候，模型容易进入过拟合的状态，样本数量少，一旦样本中出现了异常值或者离群点之后，模型会拼命想拟合异常的值，会导致预测的数值和真实的数值之间误差很大，也就是过犹不及的状态。
为了尽可能的避免过拟合的状态，一般有两种方法：
- 减少特征数量（人工选择重要的特征进行保留，不过会丢失部分信息）
- 正则化（L1正则和L2正则）--> 也就是减少特征参数$w$的数量级

## 正则化（Regularization）

正则化就是结构风险（经验风险+正则化项）最小化策略的体现，是在经验风险（平均损失函数）后面加一个正则化项。
作用是选择经济风险和模型复杂度同时较小的模型。

它能**防止过拟合**的原理：正则化项一般是模型复杂度的单调递增函数，而经验风险负责最小化误差，使得模型偏差尽可能小；经验风险越小，模型越复杂，正则化项的值越大。要使正则化项很小，那么模型的复杂度就要受到限制，那么也就会防止过拟合的发生了。

## 线性回归正则化

正则化的优化目标，通常都为：

![\ mathop {\ min} \ limits_ {f \ in F} \ left [{\ frac {1} {m} \ sum \ limits_ {i = 1} ^ m {L \ left（{{y_i}，f \ left （{{x_i}} \ right）} \ right）} + \ lambda J \ left（f \ right）} \ right]](https://private.codecogs.com/gif.latex?%5Cmathop%20%7B%5Cmin%20%7D%5Climits_%7Bf%20%5Cin%20F%7D%20%5Cleft%5B%20%7B%5Cfrac%7B1%7D%7Bm%7D%5Csum%5Climits_%7Bi%20%3D%201%7D%5Em%20%7BL%5Cleft%28%20%7B%7By_i%7D%2Cf%5Cleft%28%20%7B%7Bx_i%7D%7D%20%5Cright%29%7D%20%5Cright%29%7D%20&plus;%20%5Clambda%20J%5Cleft%28%20f%20%5Cright%29%7D%20%5Cright%5D)

其中$λ≧0$是用来平衡正则化项和经验风险的**权重系数**。

正则化项可以是模型参数向量的范数，经常用的有$L_{1}$范数（$||x||_{1}=\sum_{i=1}^{m}{|x|_{i}}$）、$L_{2}$范数（$||x||_{2}=\sqrt{\sum_{i=1}^{m}x_{i}^2}$）

现在我们先考虑最简单的线性回归模型

给定数据集$D = \left\{ \left( x _ { i } , y _ { i } \right) \right\} _ { i = 1 } ^ { m }$，其中，$x_i=(x_{i1},x_{i2},...x_{id})，y _ { i } \in R$，代价函数为：
$$
J(w)=\frac{1}{m}||y-w^TX||^2 = \frac{1}{m}\sum_{i=1}^{m}(y_i-w^Tx_i)^2
$$

- L1范数正则：（Lasso，Least Absolute Shrinkage and Selection Operator 最小绝对收缩选择算子）
	$$
	J(w)=\frac{1}{m}\sum_{i=1}^{m}(y_i-w^Tx_i)^2+λ||w||_{1}(λ>0)
	$$
- L2范数正则：（Ridge Regression  岭回归）
	$$
	J(w)=\frac{1}{m}\sum_{i=1}^{m}(y_i-w^Tx_i)^2+λ||w||_{2}^2(λ>0)
	$$

- L1正则和L2正则结合算法：（Elastic  Net）
	$$
	J(w)=\frac{1}{m}\sum_{i=1}^{m}(y_i-w^Tx_i)^2+λ(p||w||_{1}+(1-p)||w||_{2}^2)(λ>0)
	$$
	其中，L1范数正则化和L2范数正则化都有助于降低模型的过拟合的风险。

	L2范数通过对参数向量各元素的平方和求平方根，使得L2范数最小，从而使得采纳数w的各个元素接近于0，但是不等于0。

	**L1范数正则要比L2范数正则更容易获得“稀疏解”**，也就是说L1范数正则化求得的w会有更少的非零分量，所用L1范数可用于特征选择，L2范数在参数规则化时经常用到的。



#### 为什么说L1正则化就更容易获得“稀疏”解呢？



假设x仅有两个属性，w只有两个参数$w_1,w_2$，绘制不带正则项的目标函数-平方误差项等值线，在绘制L1、L2范数的等值线

![img](https://img-blog.csdn.net/20181010195155165?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3B4aGRreQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

如图所示，L1正则化后优化目标的解要在平方误差项和正则化项之间折中，也就是图中等值线相交处采用。L1范数时，交点常常出现在坐标轴上，即$w_1或w_2$为0；而采用L2范数，交点常会出现在某个象限中，也就是说$w_1，w_2$都不为0，当然为零的地方要比不为零的地方要好很多。也就是“稀疏”解



## 岭回归的求解

岭回归不抛弃任何一个特征，缩小了回归系数，它的求解与一般的线性回归一致

**采用梯度下降法**

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190829102520173.png)

迭代公式如下：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190829102623895.png)

## Lasso回归求解

由于$L_1$范数用的是绝对值，导致LASSO的优化目标不是连续可导的，也就是说，最小二乘法，梯度下降法，牛顿法，拟牛顿法都不能用，这里求解的方法是近端梯度下降法（Proximal Gradient Descent，PGD）。

### 优化目标
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190829102834213.png)

若$f(x)$可导，梯度$\nabla f(x)$满足$L-Lipschitz$条件（利普希茨连续条件），即存在常数L> 0，使得：

![1567045827389](C:/Users/admin/AppData/Roaming/Typora/typora-user-images/1567045827389.png)

> $L-Lipschitz$（利普希茨连续条件）定义：
>
> ​	对于函数$f(x)$，若其任意定义域中的$x_1,x_2$都存在$L>0$，使得$|f(x_1)-f(x_2)|≤L|x_1-x_2|$，即对于$f(x)$上每对 点，连接他们的线的斜率的绝对值总是不大于这个实数$L$。
>
> 

### 泰勒展开

将$x_k$处将$f(x)$进行二阶泰勒展开:

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190829103452807.png)

在将代入：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190829103538512.png)

在对其进行化简

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190829103632937.png)其中

![\ varphi \ left（{{x_k}} \ right）{\ rm {=}} f \ left（{{x_k}} \ right） -  \ frac {1} {{2L}} {\ left（{\ nabla f \ left（{{x_k}} \ right）} \ right）^ 2}](https://private.codecogs.com/gif.latex?%5Cvarphi%20%5Cleft%28%20%7B%7Bx_k%7D%7D%20%5Cright%29%7B%5Crm%7B%20%3D%20%7D%7Df%5Cleft%28%20%7B%7Bx_k%7D%7D%20%5Cright%29%20-%20%5Cfrac%7B1%7D%7B%7B2L%7D%7D%7B%5Cleft%28%20%7B%5Cnabla%20f%5Cleft%28%20%7B%7Bx_k%7D%7D%20%5Cright%29%7D%20%5Cright%29%5E2%7D)

是关于x的无关常数，则可以以忽略掉。

