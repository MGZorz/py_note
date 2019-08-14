## Matplotlib

#### 一、Matplotlib的基本使用

##### 常用的函数及注释

- [ ] **plt.title()** 设置图表的名称
- [ ] **plt.xlabel()** 设置x轴名称
- [ ] **plt.ylabel()** 设置y轴名称
- [ ] **plt.xticks(x,ticks,rotation)** 设置x轴的刻度，tick：表示标签的刻度，srotation:坐标轴旋转角度
- [ ] **plt.yticks()** 设置y轴的刻度              
- [x] **plt.plot()**  绘制线性图表，参数label:结合图例使用，参数linwidth:线的粗细，参数c:颜色（也可以自定义RGB颜色）
  - [ ] 特点：能够显示数据的变化走势，反映事物的**变化**情况
- [x] **plt.scatter()** 绘制散点图
  - [ ] 特点：判断变量之间是否存在在数量关联走势，展示**离群点**分布规律
- [x] **plt.bar()** 绘制条状图
  - [ ] 特点：绘制连**离散**的数据，能够一眼看出各个数据的大小，可以快速**统计**数据之间的差别
- [ ] **plt.show()** 显示图表
- [ ] **plt.legend()** 显示图例
- [ ] **plt.text(x,y,text)** 显示每条数据的值  x,y值的位置
- [ ] **plt.figure(name,figsize=(w,h),dpi=n)** 设置图片大小

###### 修改坐标轴刻度+中文字体（y轴坐标同理使用yticks()）

```python
def text1():
    # 插入数据
    info = [10, 20, 30, 40, 50, 20, 37, 20, 90]
    x = range(0, len(info))

    # 让刻度分化更细致
    x_ticks = ['{}月'.format(i) for i in x]

    # 插入字体方法1：
    font1 = matplotlib.font_manager.FontProperties(fname = 'SimHei.ttf')
		# 设置字体方法2:
    	# 查看系统全部的字体
    	# a = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
      # 设置字体
    plt.rcParams['font.family']=['SimHei']
   
    # 绘制数据
    # 规定坐标轴的刻度，以及文字体
    plt.xticks(x,x_ticks,fontproperties = font1)

    # 展现数据
    plt.show()
```

###### 修改标题名以及坐标轴名字（title()+xlabel()+ylabel()）

>   要在展现数据和设置字体中间，完成操作才ok

```python
# 设置表名
plt.title('我的天啊')
# 设置X\Y轴说明
plt.xlabel('月份')
plt.ylabel('台')
```

###### 多条数据作图

>   类似于单条数据，在增加一个plt.plot()函数就ok。

```python
# 填充数据
plt.plot(x, max_temperature,label = '最高温')
plt.plot(x, min_temperature,label = '最低温')
# 显示图例,(loc属性里面)
plt.legend(loc='upper right')
```

>   图例中的loc属性详情见：<https://matplotlib.org/api/legend_api.html>

###### 小小细节问题

```python
# 设置y坐标轴的标尺  从10~35，每2个一个标尺
y_ticks= range(10,35,2)
plt.yticks(y_ticks)
# 设置表格标尺(Flase就是没有标尺的意思)
plt.tick_params(top = False,right=False,left =False,bottom = False)
# 设置网格(alpha = [0~1],透明度)
plt.grid(alpha=0.2)
```

>   整理：
>
>   -   设置坐标轴的刻度可以使用range
>   -   设置表格的标尺，分为四个方向True/Flase
>   -   设置网格的，grid()，参数alpha(0~1)为透明度

#### 二、条状图使用详情

##### 常用函数以及注释

- plt.bar(x,y,color,width) 绘制条状图（正常），【color：颜色，width：宽度】
- plt.barh() 绘制条状图（横向）【相对于正常的，只是把横坐标变为纵坐标了】

##### 多条条状图绘制

> 是通过不同的横坐标来实现的。

```python
def test9():
	# 三条数据的名字	
    real_names = ['大侦探皮卡丘', '复仇者联盟4：终局之战', '何以为家']
	# 分别三天的票房数
    real_num1 = [8414, 4024, 2088]
    real_num2 = [11526, 5605, 2490]
    real_num3 = [7675, 2863, 1311]
    # print(real_names, real_num1, real_num2, real_num3)
    # 设置中文
    plt.rcParams['font.family'] = ['SimHei']

    plt.title('电影票房前三排名统计（3天）')
    plt.xlabel('天数')
    plt.ylabel('票房数')

    # 设置x轴位置（这里用三个横坐标分别表示响应的数据）
    x1_pos = list(range(3))
    x2_pos = [i + 0.3 for i in x1_pos]
    x3_pos = [i + 2 * 0.3 for i in x1_pos]

    print(x1_pos, x2_pos, x3_pos)
    # 设置x轴标签（规定第XX天放在那条数据下面，最好是居中）
    x_ticks = ['第{}天'.format(i) for i in range(1, 4)]
    plt.xticks(x2_pos, x_ticks)
    
    # 设置条状图宽度
    width = 0.3
    
    # 填充数据
    plt.bar(x1_pos, real_num3, width=width,label='大侦探皮卡丘')
    plt.bar(x2_pos, real_num2, width=width,label='复仇者联盟4：终局之战')
    plt.bar(x3_pos, real_num1, width=width,label='何以为家')
    # 显示图例
    plt.legend()
    # 显示图标
    plt.show()
```

#### 三、直方图的使用

> 直方图的特点：绘制连续性的数据，展示一组或者多组数据的分布状态并且**统计**，主要是用来统计的，不是直接拿统计好的数据。

##### 常用的函数以及注释

- plt.hist(data,bins,normed) 绘制直方图
  - data：所有的数据
  - bins ：组数，分为几组
  - normed ：y轴时候显示百分比，一般不用这个。

##### 代码实现

```python
# 绘制直方图  hist(data,bins,normed)
def test10():
    # 获取数据
    data = [45, 49, 42, 42, 36, 37, 31, 38, 35, 39, 43, 33, 34, 36, 35, 36, 34, 32, 36, 32, 37, 33, 32, 38, 35]
    # 制定组距
    data_width = 2
    # 制定组数
    data_count = int((max(data) - min(data)) / data_width)
    print(data_count)
    # 设置X轴坐标
    x = range(data_width)
    x_tickes = range(31, 50, 2)
    plt.xticks(x_tickes)
    # 设置中文
    plt.rcParams['font.family'] = ['SimHei']
    # 绘制图表
    plt.hist(data, data_count)
    # 展现图表
    plt.show()
```

四、Matportlib中的子图的使用（subplots()）

> - plt.subplots(x,y,figsize=(x,x))
>   - x,y ：通过索引的方式确定有几个子图
>   - figsize=(x,x)：确定每个子图的大小为x*x的。

##### 代码简单实现

```python
from matplotlib import pyplot as plt
# 随机生成数字
import numpy as np

def test11():
    # 获取数据
    data = np.random.randn(2, 100)
    # 构建子图的数量 subplots（前两个数字，表示有几行几列的意思，确定了子图的数量,figsize 表示子图的大小）
    fig, axs = plt.subplots(2, 2, figsize=(7, 7))
    # 直方图
    axs[0, 0].hist(data[0])
    # 散点图
    axs[1, 0].scatter(data[0], data[1])
    # 折线图
    axs[0, 1].plot(data[1])
    axs[1, 1].hist(data[1])

    plt.show()
```

