# Seaborn

> Seaborn的官方文档:http://seaborn.pydata.org/

#### Seaborn介绍

是对于matplotlib模块的优化，使其能够做出更具有吸引力的图标

> 安装`pip install seaborn`

#### 背景风格的管理

##### 支持的风格有5种：

- **darkgrid**  黑背景-白格 
- **whitegrid** 白背景-白格
- **dark**  黑背景
- **white** 白背景
- **ticks** 

##### 设置风格的方法：

- **set()**
- **set_style(value)**   统一设置
- **axes_style(value)**   单一设置

##### 使用详情

> **注意事项：**  修改样式要在填充数据之前使用。

```python
# set(),默认为darkgrid,单独设置需要加style='asdasd'参数
sns.set(style='dark')
plt.plot(x,y)

# 单一设置 axes_style()
with sns.axes_style('dark'):
	plt.plot(x,y)

# 统一设置样式
sns.set_style('darkgrid')
plt.plot(x,y)
```

#### 移除轴脊柱

​		在风格表中`white`和`ticks`这两个风格能够移除顶部和右侧的不必要的轴脊柱，要想单独实现这样的操作，需要`seaborn`中的`despine()`函数来实现。

```
sns.despine()
```

**注意事项：**移除轴脊柱要在 填充数据之后，在显示图表之前。

#### 图像风格管理

​		可以通过调用重置默认参数*set（）*实现,调整标签的大小、线条、绘图等其他的元素，不影响整体的样式。

- set（）
- set_context（）

图片中文本的相对大小的顺序为`paper→notebook→talk→poster`，`notebook`是默认的大小。

```python
set_context('paper')
# 等价于,但是别忘记set的背景默认样式为darkgrid
set(context='paper')
```

set_context（）中的参数

- font_size`(字体大小)` = x`(x为放大的倍数)`

- rc `(自定义参数)`，举例：

  - ```python
    rc = {'line.linewidth': 5 }  # 线的粗细
    ```

  - 想要找rc中有什么样的参数，有两种方法：
    1. 看官方文档
    2. 找寻源码，`set_context→plotting_context→base_context`

#### 调色板

通过调整颜色，更加凸显显示数据的结果与重要性。

- color_palette()	能传入任何Matplotlib支持的颜色，不写参数则默认为`deep, muted, pastel, bright, dark, colorblind`。
- light_palette() 和   dark_palette()   用法都是一样的，前者是由浅入深，后者为由深入浅。
- set_palette()      设置说有图片的颜色
- xkcd_rgb()     制定使用`RGB`颜色

##### color_palette()

```python
current_palette = sns.color_palette()
sns.palplot(current_palette) # 默认显示为10个色块
sns.palplot(sns.color_palette('hls',8))   # 后面的数字表示几个色块，色度比较亮
plt.show()
```

![](https://note.youdao.com/yws/api/personal/file/WEBc69497b873583d3301d3f8ec9c8a8439?method=download&shareKey=399897c141ecc19d2dff495c92bee6c3)

###### 连续的调色板

```python
sns.palplot(sns.color_palette('Blues'))  # 不加‘_r’，为由浅入深
sns.palplot(sns.color_palette('Greens_r')) #参数里可以输入数字，指定颜色的块数,_r由深到浅
plt.show()
```

![](https://note.youdao.com/yws/api/personal/file/WEB52aa4b9c53bb690a2fc383786188a295?method=download&shareKey=9d802e5dda753e178c706bc91ec788d7)

![](https://note.youdao.com/yws/api/personal/file/WEB15f6e557a3ee10492502cac64c6b684e?method=download&shareKey=9aa4e6600f3d78722562d15d7ea74aca)

##### light/dark

```python
sns.palplot(sns.light_palette('green'))  #  绿色的连续调色板
sns.palplot(sns.dark_palette('purple'))  #  紫色的连续调色板
```

##### xkcd_rgb

在xkcd_rgb中一共有[954种命名颜色](https://xkcd.com/color/rgb/)，可以使用xkcd_rgb在seaborn中引用

```python
plt.plot([0, 1], [0, 1], sns.xkcd_rgb["pale red"], lw=3) # lw 为线的宽度
plt.plot([0, 1], [0, 2], sns.xkcd_rgb["medium green"], lw=3)
plt.plot([0, 1], [0, 3], sns.xkcd_rgb["denim blue"], lw=3)
```



#### 单变量数据绘图

​		分析单变量的数据的图表有三种。

##### **distplot**			直方图

```python
def test17():
    # 生成数据
    data = np.random.normal(size=100)
    # 绘画数据    高斯估计：kde  分组：bins
    # sns.distplot(data,kde=False)
    # sns.distplot(data,kde=False,bins=20) 
    sns.distplot(data,kde=True,bins=20) # kde = True 多了一条正态分布曲线。
    # 显示图表
    plt.show()
```

![distplot](https://img-blog.csdnimg.cn/20190715205443679.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjAxODY3MQ==,size_16,color_FFFFFF,t_70)



##### jointplot		 散点图

```python
import pandas as pd
# joinpoint散点图
def test18():
    # 多元高斯正态分布：一堆正太分布向更多维度的推广，这种分布由其均值和协方差矩阵来确定
    data = np.random.multivariate_normal([0,1],[(1,0.5),(0.5,1)],1000) # 均值， [(1,0.5),(0.5,1)]协方差对称阵
    # 删选数据，对上面的数据进行处理。
    df = pd.DataFrame(data, columns=['x', 'y'])
    #  绘画图表 x:横坐标 y:纵坐标 data：数据来源 kind:散点样式 color:颜色 k 黑白
    sns.jointplot(x='x', y='y', data=df, kind='hex', color='k')
    plt.show()
```

![jointplot](https://img-blog.csdnimg.cn/20190715205704546.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjAxODY3MQ==,size_16,color_FFFFFF,t_70)



##### pairplot		对比关系图

​	会同时绘制数据中心所有特征两两之间的关系图。

```python
# pairplot
def test19():
    # 引入鸢尾花的数据集
    iris = sns.load_dataset('iris')
    sns.pairplot(iris)
    plt.show()
```

![pairplot](https://img-blog.csdnimg.cn/20190715210406586.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjAxODY3MQ==,size_16,color_FFFFFF,t_70)



#### 回归关系分析图

当得到连续性的数据时，可以做一些回归关系的绘制与展示，具体的方法如下：

- sns.regplot() 
- sns.lmplot()

就简单的应用这两个函数的功能几乎完全一样，但lmplot()函数功能多一些，使用也会相对复杂，先学习[regplot()](http://seaborn.pydata.org/generated/seaborn.regplot.html#seaborn.regplot)。

```python
def test20():
    # 获取数据 tips 是内置在seaborn中的数据
    data = sns.load_dataset('tips')
    print(data)
    # 填充数据  x 为total_bill  y 为 tip data=data  数据来源于data
    sns.regplot(x='total_bill',y = 'tip',data = data)
    # 展现图表
    plt.show()

def test21():
    data=sns.load_dataset('tips')
    sns.lmplot(x='total_bill',y = 'tip',data = data)
    plt.show()
```

![回归分析图](https://img-blog.csdnimg.cn/20190715213342286.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjAxODY3MQ==,size_16,color_FFFFFF,t_70)



#### 多变量绘图

​	在数据分析做图中，往往只研究两个变量之间的关系是不够的，那么就要进行多变量分析。加一个变量通过参数添加`hue='要加的东西'`

##### 花装图（分簇散点图）

分簇散点图是在分布散点图的基础上，衍生而来的。直观上的变化就是把数据重合的地方分散开，但总体上还是同一个维度上的。

```python
# 分布散点图
sns.stripplot(x='day', y='total_bill', data=data)
# 分簇散点图
sns.swarmplot(x='day',y = 'total_bill',data =data)
```

![分布和分簇散点图](https://img-blog.csdnimg.cn/20190716094447610.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjAxODY3MQ==,size_16,color_FFFFFF,t_70)

##### 盒图（箱形图）

​		它能显示出一组数据的**最大值**、**最小值**、**中位数**及**上下四分位数**。

```python
sns.boxplot(x='day',y = 'total_bill',hue='time',data =data)
```

###### 箱型图图解（引用）

![https://upload-images.jianshu.io/upload_images/8316927-25c3a1e2467277be?imageMogr2/auto-orient/strip%7CimageView2/2/w/485/format/webp](https://upload-images.jianshu.io/upload_images/8316927-25c3a1e2467277be?imageMogr2/auto-orient/strip|imageView2/2/w/485/format/webp)

##### 小提琴图

​	小提琴图是以基础分布的**核密度估计**为特征的。

```python
sns.violinplot(x='day',y = 'total_bill',hue='sex',data =data,split=True)
```

![小提琴图](https://img-blog.csdnimg.cn/2019071609510485.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjAxODY3MQ==,size_16,color_FFFFFF,t_70)

##### 条形图

```python
sns.barplot(x='sex',y='survived',hue='class',data=titanic)
```

##### 点图

```python
# sns.pointplot(x='sex',y='survived',hue='class',data=titanic)
# markers：点的样式 linestyles：线的样式
sns.pointplot(x='class',y='survived',hue='sex',data=titanic,
                  palette={'male':'g','female':'m'},markers=['^','o'],
                  linestyles=['-','--'])
```

##### 万能图

​		功能最多，同时它的参数也是最多的。

```python
# 万能方法,kind='要啥来啥'  height和aspect代表大小
sns.catplot(x='day',y = 'total_bill',hue = 'smoker',data=tips,kind='bar')
```

> ###### 万能图的参数

> - x,y,hue 数据集变量 变量名
> - date 数据集 数据集名
> - row,col 更多分类变量进行平铺显示 变量名
> - col_wrap 每行的最高平铺数 整数
> - estimator 在每个分类中进行矢量到标量的映射 矢量
> - ci 置信区间 浮点数或None
> - n_boot 计算置信区间时使用的引导迭代次数 整数
> - units 采样单元的标识符，用于执行多级引导和重复测量设计 数据变量或向量数据
> - order, hue_order 对应排序列表 字符串列表
> - row_order, col_order 对应排序列表 字符串列表
> - kind : 可选：point 默认, bar 柱形图, count 频次, box 箱体, violin 提琴, strip 散点，swarm 分散点 size 每个面的高度（英寸） 标量 aspect 纵横比 标量 orient 方向 "v"/"h" color 颜色 matplotlib颜色 palette 调色板 seaborn颜色色板或字典 legend hue的信息面板 True/False legend_out 是否扩展图形，并将信息框绘制在中心右边 True/False share{x,y} 共享轴线 True/False

#### FacetGrid

​	当想把数据中的多个子集展示出来时，可以使用FacetGrid，步骤如下：

```python
g = sns.FacetGrid(tips, col='sex', hue='smoker')   # 绘画区域  (数据源，按照sex分开，观察吸烟与消费的关系)
g.map(plt.scatter, 'total_bill', 'tip')# 使用方法绘画数据 (横轴为total_bill 纵轴为tip)
```

> ​	对于Facetgrid中对图像的操作，是通过参数来实现的：
>
> - height  高
> - size 代表的也是高，但是被height代替
> - aspect  宽
> - palette 色板
> - col    分图属性(列)
> - row   分图属性(行)
> - hue   属性分类
> - margin_titles  外边框
> - row_order     确定显示分图的数据的顺序   使用这个之前要导入 `from pandas import Categorical`对顺序进行加工。
> - hue_kws     显示图标记的形状(散点)

```python
# 绘画区域
g = sns.FacetGrid(tips, col="time")
#----------------- 绘画直方图-----------------
g.map(plt.hist, "tip");

#----------------- 绘画散点图-------------------
g = sns.FacetGrid(tips, col="sex", hue="smoker") # 根据`性别`分类多图， 显示出2部分数据
g.map(plt.scatter, "total_bill", "tip", alpha=.7) # alpha为透明度，横为total_bill
g.add_legend(); #增加图例

#----------------- 绘画散点图-------------------
pal = dict(Lunch="seagreen", Dinner="gray")
g = sns.FacetGrid(tips, hue="time", palette=pal, size=5) # palette修改颜色
g.map(plt.scatter, "total_bill", "tip", s=50, alpha=.7, linewidth=.5, edgecolor="white")
g.add_legend();

#----------------- 绘画散点图-------------------
g = sns.FacetGrid(tips, hue="sex", palette="Set1", size=5, hue_kws={"marker": ["^", "v"]})#  hue_kws确定散点的样式
g.map(plt.scatter, "total_bill", "tip", s=100, linewidth=.5, edgecolor="white")
g.add_legend();


#------------------回归分析图-----------------
g = sns.FacetGrid(tips, row="smoker", col="time", margin_titles=True) # margin_titles 外边距
g.map(sns.regplot, "size", "total_bill", color=".1", fit_reg=False, x_jitter=.1)

#------------------条形图-----------------
g = sns.FacetGrid(tips, col="day", height=4, aspect=.5)
g.map(sns.barplot, "sex", "total_bill");

#------------------盒形图-----------------
from pandas import Categorical # 引入pandas,对顺序进行包装
ordered_days = tips.day.value_counts().index
print (ordered_days)
ordered_days = Categorical(['Thur', 'Fri', 'Sat', 'Sun'])
g = sns.FacetGrid(tips, row="day", row_order=ordered_days,
                  size=1.7, aspect=4,)
g.map(sns.boxplot, "total_bill");




with sns.axes_style("white"):   # axes_style 和with连用设置单一的样式。
    g = sns.FacetGrid(tips, row="sex", col="smoker", margin_titles=True, size=2.5)
g.map(plt.scatter, "total_bill", "tip", color="#334488", edgecolor="white", lw=.5);
g.set_axis_labels("Total bill (US Dollars)", "Tip");
g.set(xticks=[10, 30, 50], yticks=[2, 6, 10]);
g.fig.subplots_adjust(wspace=.02, hspace=.02);
# g.fig.subplots_adjust(left  = 0.125,right = 0.5,bottom = 0.1,top = 0.9, wspace=.02, hspace=.02)
```

#### 热力图

​		热力图可以显示多个数据的走势与规律，并可以快速到到大值的与最小值所在位置，说白了就是一堆颜色块堆积在一起的。

```python
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

def test42():
    '''绘制热力图'''
    # sns.heatmap(data)
    # 绘制0.2~0.5之间的数据
    # sns.heatmap(data,vmin=0.2,vmax=0.5)
    # 设置中间值为0 越接近0则越黑
    sns.heatmap(data,center=0)
    # 显示
    plt.show()
    
def test43():
    # 转化数据   pivot()先画y在画x
    flight = flights.pivot('month','year','passengers')
    print(flight)
    # annot = True 显示响应的数据  ,fmt='d' 转化为十进制 linewidths 格距 cmp 更改颜色（注意其中的颜色有规定） cbar = False 消除旁边的图例
    sns.heatmap(flights,annot=True,fmt='d',linewidths=0.5,cmap='Blues',cbar=False)
    plt.show()

if __name__ == '__main__':
    # data = np.random.rand(3,3)
    # randn 表示能够生成正数和负数  rand()只能生成正数
    data = np.random.randn(3,3)
    # print(data)
    # 航班的信息
    flights = sns.load_dataset('flights')
    # print(flights.head())
    test43()
```



pycharm快捷键

- 复制当前行：ctrl+d
- 同时输入多行文本：按住滚轮滑动