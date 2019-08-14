

学习的四种语言都是以前一个语言为基础的，举个栗子：HTML5是人的骨架，CSS是人的血肉+衣服（静态），JavaScript完善它是个人（动态）。

# HTML

## 互联网中的三大基石

### 概念

-   HTML：超文本标记语言

-   HTTP：超文本传输协议

-   URL ：统一资源点位符。

    #### 理解示意图

    ##### 情景模拟

    ​	小明给移动客服打电话

    ##### 需要准备的事情

    -   小明必须知道移动的电话号码（10086）--URL

    -   移动客服的语言必须和小明的语言统一（中文）--HTTP

    -   小明询问之后移动客服必须做出回应--HTML

        

    ![1558078152388](E:\python_document\notes\assets\1558078152388.png)

## HTML入门

### 为什么要学习HTML

#### 需求：

随着技术的发展，信息量的增大网页的数据信息没有办法完美的、漂亮的展现到用户的面前。

#### 作用：

HTML是一种专门对网页信息进行规范化展示的语言，把网页的信息格式化展现的语言。

### 什么是HTML?

-   **HTML**(Hyper Text Markup Language)：超文本标记语言。
-   **超文本**：不仅能够写文本信息，还可以写图片、声音、视频、超链接等信息。
-   **标记**：标记？=标签，格式以及布局效果都是利用标签的展现。

### 学习网站

​	w3cschool在线教程：http://www.w3school.com.cn/

### 简单案例

```html
<html>
	<head>
	<!--head中会书写一些浏览器中国的配置标签-->
	<!--告诉浏览器按照UTF-8的形式解析网页-->
	<meta charset='UTF-8' />
	
	<title>史上最黄色的网站</title>
	
	</head>
	<body>
		<!--body中会书写直接展现到用户面前的信息-->
	别看了，想啥呢？

	</body>
</html>
```

## Head标签的子标签

### meta标签

```html
<!DOCTYPE html>
<!--HTML的文档约束(DTD)
	
	HTML5 的文档约束		<!DOCTYPE html>
	HTML	4.01的文档约束 	<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
													"http://www.w3.org/TR/html4/strict.dtd">
-->
<html>
	<head>
		<meta charset="utf-8" />
		<title>史上最黄色的网站</title>		
		<!--搜索引擎优化-->
    <!--按照作者来检索-->
		<meta name="author" content="朱自清，张三" />
    <!--按照内容检索-->
		<meta name="description" content="东风来了，春天的脚步近了" />
    <!--按照关键字检索-->
		<meta name="keywords" content="东风，春天" />
		
		<!--自动刷新网页-->
		<meta http-equiv="refresh" content="5;http://www.baidu.com" />
		
		<!--禁止网页缓存(了解)-->
		<meta http-equiv="Pragma" content="no-cache" />
		<meta http-equiv="Cache-Control" content="no-cache" />
		<meta http-equiv="expires" content="0" />	
	</head>
	<body>
		别看了，想啥呢？
	</body>
</html>
```

#### 小笔记环节：

##### 	简介

​	元素可提供有关页面的元信息（meta-information），比如针对搜索引擎和更新频度的描述和关键词。

##### 	必须的属性

​	content = “搜索的内容”

##### 	可选的属性

| 属性       | 值                                                           | 描述                            |
| ---------- | ------------------------------------------------------------ | ------------------------------- |
| http-equiv | content-type<br />expires<br />refresh<br />set-cookie       | 把content属性关联到HTTP头部     |
| name       | author<br />description<br />keywords<br />generator<br />revised<br />others | 把content属性关联到一个名称     |
| scheme     | some_text                                                    | 定义用于翻译content属性值的格式 |

## body中的基本标签

​	用于展现到用户面前的信息

### 基本标签

-   **标题标签**：从1-6分为六个标题，自动加粗加黑+自动换行，align="center"表示位置，默认为"left"，"right"表示右。

    -   <!--<h1 align="center">【史上最全黄色网站】</h1>-->

-   **分割线标签**:width="500px"宽度属性,color="red"颜色属性,align="left"位置属性（默认为center），size=垂直方向大小。

    -   ```html
        <hr width="500px" color="red" align="left" size="20px"/>
        ```

-   **段落标签**:br为换行标签，&ndsp;空格效果实现

    -   ```html
        <p>&ndsp;&ndsp;继续往下看啊，<br />哈哈哈哈</p>
        ```

-   **预文本标签**：会按照指定的格式原样输出，但是使用的情况不多

    -   <!--<pre>继续往下看啊，
        		哈哈哈哈</pre>-->

-   **下划线标签**：文本增加下划线

    -   ```
        <u>yellow</u>
        ```

-   **斜体标签**

    -   ```html
        <i>blue</i>
        ```

-   **加粗加黑标签**

    -   ```html
        <b>black</b>
        ```

-   **中划线标签**（删除标签）

    -   ```html
        <del>yellow</del>
        ```

-   **上标标签和下标标签**：基本+标字

    -   ```html
        2<sup>3</sup>
        3<sub>2</sub>
        ```

-   **字体变小、变大标签**

    -   ```html
        <small>yellow</small>
        <big>yellow</big>
        ```

-   **字体标签**：face指定字体的风格

    -   ```html
        <font color="red" size="25px" face="宋体">yellow</font>
        ```

-   **列表标签**：

    -   **[1]有序标签**：（type 排序）

        -   ```html
            <ol type="a">
                    	<li>yellow</li>
                    	<li>black</li>
                    	<li>green</li>
                    <ol>
            ```

    -   **[2]无序标签**

        -   ```html
            <ul type="circle">
                    	<li>yellow</li>
                    	<li>black</li>
                    	<li>green</li>
                    </ul>
            ```

    -   **[3]自定义标签**

        -   ```html
            <dl>
                    	<dt>java</dt>
                    	<dd>yellow</dd>
                    	<dd>black</dd>
                    	<dd>green</dd>
                    </dl>
            ```

    -   **作用**：

        -   树形菜单
        -   导航栏的布局

-   **跑马灯标签**：driection表示文字哪个方向动,scrollamount表示速度

    -   ```html
        <marquee direction="right" scrollamount="40px">yellow</marquee>
        ```

    ### 案例整合：

    ```html
    <!DOCTYPE html>
    <html>
    	<head>
    		<meta charset="utf-8">
    		<title>
    			【史上最全黄色网站】
    		</title>
    	</head>
    	<body>
    		<!--标题标签,从1-6分为六个标题，自动加粗加黑+自动换行
    			align="center"表示位置，默认为"left"，"right"表示右-->
    		<h1 align="center">【史上最全黄色网站】</h1>
    		【史上最全黄色网站】
    		<!--分割线标签，width="500px"宽度属性,color="red"颜色属性,
    		align="left"位置属性（默认为center），size=垂直方向大小-->
    		<hr width="500px" color="red" align="left" size="20px"/>
    		
    		<!--段落标签,<br />:换行标签,&ndsp;空格效果实现-->
    		<p>&ndsp;&ndsp;继续往下看啊，<br />哈哈哈哈</p>
    		
    		<!--预文本标签，会按照指定的格式原样输出，使用的情况不多-->
    		<pre>继续往下看啊，
    		哈哈哈哈</pre>
        
        <!--下划线标签-->
    		<u>yellow</u>
    		<!--斜体标签-->
    		<i>blue</i>
    		<!--加粗加黑标签-->
    		<b>black</b>
    		<!--中划线标签、删除标签-->
    		<del>yellow</del>
    		<!--上标标签和下标标签-->
    		2<sup>3</sup>
    		3<sub>2</sub>
    		<!--字体变小标签-->
    		<small>yellow</small>
    		<!--字体变大标签-->
    		<big>yellow</big>
    		
    		<!--字体标签，face指定字体的风格-->
            <font color="red" size="25px" face="宋体">yellow</font>
            <span>yellow</span>
        
        <hr />
      	<!--列表标签[1]有序标签，[2]无序标签，[3]自定义标签-->
        <!--作用：[1]树形菜单
            		 [2]导航栏的布局-->
        <!--[1]有序标签,type 排序-->
        <ol type="a">
           <li>yellow</li>
           <li>black</li>
           <li>green</li>
        </ol> 
        <!--[2]无序列表-->
        <ul type="circle">
           <li>yellow</li>
           <li>black</li>
           <li>green</li>
         </ul>
         <!--[3]自定义列表-->
         <dl>
           <dt>java</dt>
           <dd>yellow</dd>
           <dd>black</dd>
           <dd>green</dd>
         </dl> 
         <!--跑马灯标签 driection表示文字哪个方向动,scrollamount表示速度-->
         <marquee direction="right" scrollamount="40px">yellow</marquee>
    	</body>
    </html>
    ```

## 图片标签

### 	指令

-   图片引入分为三个路径【相对路径（在img文件夹中）、绝对路径（很详细，但是换一个设备就分辨不出来 ）、网络路径（网络上的图片）】
-   img标签中的小标签们：
    -   src :引入图片位置（相对，绝对，网络）
    -   title:图片的标签
    -   width /height :图片的大小
    -   border： 给图片加一个边框
    -   alt : 当图片无法正常显示的时候，alt显示
    -   align:图片的位置，但是必须要有参考才可以实现
    -   让图片能够点击，则需要让img标签放到</a/ href = “ #”>(去掉两个/)里面。	

## 超链接标签

### 超链接标签的作用（不会自动换行的）

1.  实现不同页面的跳转
    -   href :引入资源的位置
    -   target: 决定是如何打开超链接，_blank是新窗口的意思
2.  实现锚点的功能
    **锚点**其实就是类似于返回顶部、返回底部这样的操作

### 代码的实现

​	只是把主要的内容呈现出来。

```html
<!--超链接的作用1-->
		<!--跳转到本地的资源位置-->
		<a href="boby中常用的标签.html" target="_blank">小便签测试</a>
		<!--跳转到网络的资源位置-->
		<a href="http://www.baidu.com">世界最大脑残集中地</a>
<!--超链接的作用2-->
		<a href="#bottom" name= 'top'>返回底部</a>
		<a href="#top" name= "bottom">返回顶部</a>
```

## 表格标签

### 	table标签

-   行：tr

-   列：td（普通列）th（标题列）

-   指定单元格大小：

    -   规定整体的大小，在table上添加width和height属性
    -   个别大小，在对应的行和列上添加height和width属性

-   内容位置：

    -   让所有的内容变换位置，在每个tr上添加align
    -   注意：在table上添加align只会让表格整体变动位置。

-   快速生成表格：（例：生成3行3列表格）

    -   table>tr*3>td*3+tab

-   小属性：

    -   合并属性：
        -   th colspan="x"合并几列填几，同时合并的后一项要注释掉
        -   th rowspan="x"合并几行填几，同时合并的后一项要注释掉
    -   背景颜色：bgcolor="blue"
    -   cellpadding:指文本的内容和单元格的距离
    -   cellspacing:单元格和单元格之间的距离

    ### 代码实现

    ```html
    <table border="2px" cellpadding="20px" cellspacing="20px"> 
    			<!--一行-->
    			<tr height="100px"	align="center" bgcolor="blue">			<!--一列-->
    				<td width="100px">11</td>
    				<td width="100px">2</td>
    				<td width="100px" rowspan="2">3</td>
    			</tr>
    			<tr height="100px">
    				<td colspan="2">4</td>
    				<!--<td>5</td>-->
    				<!--<td>6</td>-->
    			</tr>
    			<tr height="100px">
    				<td>7</td>
    				<td>8</td>
    				<td>9</td>
    			</tr>
    			<tr height="100px">
    				<th>12</th>
    				<th>12</th>
    				<th>12</th>
    			</tr>
    </table>
    ```

## 表单标签

### 	表单标签（from）

-   action：表单提交的位置

-   method(get/post)：表单提交的方式

    -   get : （1）参数会依附与url地址之后（2）利用get方式提交数据，数据长度有限制，（3）不安全的
    -   post:（1）请求不会依附与地址（2）而且对提交数据的长度无限制（3）post数据提交比较安全
    -   ps：百度使用的提交方式为get

    ### input标签

    ```html
    <form>
    			<!--普通文本框  value:文本框中默认的值-->
    			账号： <input type="text" name="zh" value="123"/>	
    			<br />
    			<!--密码框-->
    			密码：<input type="password" name="pwd" value="123" />
    			<!--单选框 实现单选效果，必须要指定同一个name属性 checked="checked"默认选择-->
    			男：<input type="radio" name="sex" value="1" checked="checked"/>
    			女：<input type="radio" name="sex" value="0"/>
    			<!--多选框 -->
    			抽烟：<input type="checkbox" value="1"/>
    			喝酒：<input type="checkbox" value="2"/>
    			烫头：<input type="checkbox" value="3"/>
    			<!--多行文本框-->
    			个人介绍：
    			<textarea rows="15" cols="20" >
    				
    			</textarea>
    			<!--文件选择-->
    			<input type="file" name="file" />
    			<!--隐藏框-->
    			<input type="hidden" name="sno" value="1321321"/>
    			<br />
    			<br />
    			<!--下拉框 selected="selected"默认选项-->
    			<select name="ch">
    				<option value="1">中国</option>
    				<option value="2" selected="selected">美国</option>
    				<option value="3">德国</option>
    				<option value="4">法国</option>
    			</select>
    			<br />
    			<br />
    			<!--按钮的使用-->
    			<!--提交按钮-->
    			<input type="submit" value="提交" />
    			<!--清除按钮 清空写好的内容回到默认的状态-->
    			<input type="reset"  value="清除" />
    			<!--普通的按钮，无提交功能-->
    			<input type="button"  value="普通" />
    </form>
    ```

## 框架标签

### 	**iframe标签**

​	在当前网页中嵌套一个框架，用于显示页面。

```html
<ul>
			<li><a href="http://www.baidu.com" target="ifm">百度</a></li>
			<li><a href="http://www.taobao.com" target="ifm">淘宝</a></li>
			<li><a href="http://www.jd.com" target="ifm">京东</a></li>
		</ul>
		<!--框架标签 宽度：width 高度：height src:默认路径-->
		<iframe width="1000px" height="550px" name="ifm" src="http://www.baidu.com"></iframe>
```

### 	frameset标签

​	可以把网页分为好几个部分，结合iframe标签让每个部分显示不同的内容。

```html
<!--先横向划分,在纵向划分-->
<!--rows划分别三部分-->
<frameset rows="150px,*,100px">
		<!--顶部,不让它滑动-->
    <frame  src="admin/top.html" noresize="noresize"/>
  
    <!--中间部分,纵向划分-->
    <frameset cols="10%,*">
      
       <!--左侧部分-->
       <frame src="admin/left.html" />
      
       <!--右侧部分-->
       <frame src="admin/right.html" name="rig"/>	
      
    </frameset>
  
    <!--底部部分-->
		<frame src="admin/buttom.html"/>
  
</frameset>
```

## div标签（应用很广）

​	**div标签就是模块化**，本身是无任何意义的，作用是对网页进行模块化的划分。

```html
<!--div是放在body中的，但是规定位置什么的，需要放在style标签内，会用到CSS.-->
<!--样式，规定每个div的大小位置等等等。-->
<style>
			.top{
				height:100px;
			
				width:100%;
				/*背景颜色*/
				background-color: black;
			}
			.tips{
				width: 100%;
				height: 20px;
				background-color: red;
			}
			.mid{
				width: 100%;
				height: 475px;
				background-color: green;
			}
			.but{
				width: 100%;
				height: 150px;
				background-color: palegoldenrod;
			}
			.login{
				width: 350px;
				height: 400px;
				background: #ffffff;
				/*相对定位*/
				position: relative;
				left: 70%;
				top: 5%;
			}	
		</style>
<body>
	<!--头部模块-->
        <div class="top">	 </div>
        <!--中间提示-->
        <div class="tips"></div>
        <!--中间展现-->
        <div class="mid">
        	<div class="login"></div>
        </div>
        <!--底部模块-->
        <div class="but"></div>
</body>
```

## HTML5增强表单标签

​	**一定要在from标签内！！！！**,同时标签要在P中。

### 	增强标签

-   email:可以帮助邮箱完成基本的格式校验

    -   ```html
        <p>
          邮箱：<input type="email" />
        </p>
        ```

-   number:不可以输入英文，但是e是支持的（这里e表示的是科学计数法）

    -   ```html
        <p>
        	年龄：<input type="number" />
        </p>
        ```

-   range:滑动器

    -   ```html
        <p>
          滑动器：<input type="range"
        </p>
        ```

-   search：搜索框

    -   ```html
        搜索框：<input type="search"
        ```

-   date：日期框（年月日）/week：日期框（周）/month：日期框（月）

    -   ```html
        日期：<input type="date" />
        第几周：<input type="week" />
        月：<input type="month" />
        ```

-   color：颜色框（可选颜色变多）

    -   ```html
        颜色：<input type="color" />
        ```

-   url：自动判断网址格式

    -   ```html
        网址：<input type="url" />
        ```

### 	增强属性

-   placeholder：为输入之前的灰色默认值

    -   ```html
        账号：<input type="text" placeholder="手机号/邮箱" />
        ```

-   autofocus：光标自动定位，自动获得焦点

    -   ```html
        账号：<input type="text" placeholder="手机号/邮箱" autofocus />
        ```

-   max/min：最大/最小值数字

    -   ```html
        年龄：<input type="number" max="130" min="0" />
        ```

-   maxlength/minlength:最大长度/最小长度

    -   ```html
        密码：<input type="password" maxlength="15" minlength="6"/>
        ```

## HTML5新增结构标签

### 	结构标签

主要是优化在div标签上，简单的用两个图片就能很明显的看出来。

#### 原始版本↓

![2012052410570957](E:\python_document\notes\assets\2012052410570957.gif)

#### H5版本↓↓

![2012052410554136](E:\python_document\notes\assets\2012052410554136.gif)

咱们可以清晰地看出来这个优化，简直就是不写备注星人的福音啊，简单易懂就能定位页面地方定位在哪个地方。

## H5中音频视频标签

### 	音频标签：audio

```html
<!--引入音频的标签 controls是控制按钮-->
<audio src="img/彪高音.mp3" controls="controls">
  该网页不支持多媒体标签
</audio>
<audio>
	<!--防止不同的浏览器支持的音频格式不同-->
	<source src="img/彪高音.mp3">
	该网页不支持多媒体标签	</source>
</audio>
```

### 	视频标签：video

```html
<!--引入视频标签-->
<video src="img/2.mp4" controls="controls">
</video>
<!--同样防止格式不同-->
<video>
	<source src="XXXX">
	</source>
</video>
```

### 	多媒体标签：embed

```html
<!--多媒体标签 可以规定框框-->
<embed src="img/彪高音.mp3"></embed>
<embed src="img/彪高音.mp3" width="500px" height="500px"></embed>
```

## H5中绘图和其他标签

### 	代码：

```html
<!--和自定义列表很相似-->
<figure>
	<img src="img/a6d85e4bd11373f06dcfd0f0a80f4bfbfaed040d.jpg" />
			
	<figcaption>IT程序猿</figcaption>
			
</figure>
<!--展示文章细节标签-->
<details>
	<summary>请选择</summary>
	<p>China</p>
	<!--mark高亮表示标签-->
	<p><mark>China</mark></p>
	<p>China</p>
			
</details>
		
<!--刻度标签 
		最大max、
		最小min、
		当前value、
		给定正常的范围超出范围变色low/high-->
<meter max="100" min="0" value="90" low="20" high="80"></meter>
		
<!--进度条标签 最大max 当前value-->
<progress max="100" value="50"></progress>
		
<!--画布标签 必须基于javascript，现在知道有这个东西就好啦-->
<canvas id="mycat"></canvas>
<script>
			var ca=document.getElementById("mycat");
			var te = ca.getContext("2d")
			//背景颜色
			te.fillStyle="red"
			//绘制图形的大小
			te.fillRect(0,0,80,100)
</script>
```



# CSS样式

## 	CSS入门

#### 为什么学习CSS？（作用）

​	HTML虽然可以再一定程度上美化页面，但是在页面的整体还是不是很美观的。

​	HTML进行网页的书写重复代码比较多，后期的维护性不好。

#### 什么是CSS（概念）

​	英文全称：Cascading Style Sheets

​	层叠样式表（级联样式表）

### 	CSS的引入方式

​	CSS的引入方式分为四种，而且遵循的是**就近原则**（谁离我近我遵循谁）

1.  **行内样式** ，利用style=“键：值”来定义样式，但是如果目标变多，重复代码量就会增大

    ```html
    <!--这里以字体颜色举栗-->
    <p style="color: red;">我们不一样</p>
    ```

2.  **内嵌式**，在title标签下插入style标签。

    ```html
    <style>
    			/*代表标签的名称*/
    			p{
    				/*字体颜色*/
    				color: red;
    				/*字体大小*/
    				font-size: 25px;
    				/*字体加粗*/
    				font-weight: bold;	
    			}
    </style>
    ```

3.  **外部链接式**，在CSS文件夹中创建一个样式文件，然后引入就OK啦~

    ```css
    /*CSS中代码*/
    p{
    	/*字体的风格*/
    	font-family: 宋体;
    	
    	color: yellow;
    	
    	/*字体的样式，italic斜体*/
    	font-style: italic;
    }
    ```

    ```html
    <!--HTML中代码  rel：引入文件和当前文件的关系   href：引入文件的路径-->
    <link rel="stylesheet" href="css/01样式.css" />
    ```

4.  **引入式**（了解即可）

    ```html
    <style>
    			@import url("css/01样式.css");
    </style>
    ```

这四种方式，首推**外部链接和内嵌**，额外的两种方式都有相应的缺点。

CSS常用的选择器

选择器常见的也就只有四种，分别为通用选择器、元素选择器、ID选择器、类选择器。**这四个选择器的优先级是：ID>类选择器>元素选择器>通用选择器。**

都是在title下加一个style标签，在style标签中编辑的。

#### 通用选择器

​	用一个“*”表示该页面中的所有元素，代码如下↓↓

```css
/*通用选择器"*",表示该页面中的所有元素*/
*{
	/*让字体变为红色*/
	color: red;
}
```

#### 元素选择器

​	用对应的元素来进行选择，也叫标签选择器，代码如下↓↓

```css
div{
	width: 200px;
	height: 200px;
	/*背景颜色*/
	background-color: yellow;
	/*边框的粗细、边框的风格、边框颜色*/
	border: 1px solid red;
}
```

#### ID选择器

​	用处在于把某个标签添加样式，刚开始要用**#+ID名称**，并且也要保持唯一（按理说可以，但是防止出错）

**ID 的命名规范：数字、字母、下划线、中划线组成，不能用数字开头。**

代码如下↓↓

```css
#div1{
				background-color: gray;
			}
```

#### 类选择器

​	注意区分类是可以重复的，id是尽量不要重复的，使用的格式是**“.”+class名称**，代码如下↓↓

```css
.div_1{
				background-color: pink;
			}
```

## 	CSS中的其他选择器（了解）

#### 后代选择器（派生选择器）

​	栗子中，只要是div中的span都会生效。

```css
div span{
				font-size: 27px;
				font-family: 宋体;
			}
```

#### 子选择器

​	栗子中，只有和div有直系子关系的span标签生效

```css
div>span{
				color: red;
			}
```

#### 兄弟选择器（1）

​	只会改变下面相邻的元素对象

```css
#p_1+p{
				color: green;
			}
```

#### 兄弟选择器（2）

​	后面所有的兄弟对象都会发生改变

```css
#p_1~p{
				color: red;
				font-family: 30px;
			}
```

#### 伪类选择器

​	hover：表示鼠标放上的操作

```css
a:hover{
				color: red;
			}
```

## CSS常用属性

1.  ### 框框：

    border: 宽度 样式 颜色

    样式都有啥呢？请看下图↓↓

    ![1558428960984](E:\python_document\notes\assets\1558428960984.png)

    或者这样的~

    ![1558428986265](E:\python_document\notes\assets\1558428986265.png)

2.  ### 字体（font）

    1.  字体颜色：color
    2.  字体大小：font-size
    3.  字体加粗：font-weight:bold
    4.  字体风格：font-family
    5.  字体倾斜：font-style: italic

3.  ### 文本（text）

    1.  去除下划线/下划线展示：text-decoration: none/text-decoration: underline
    2.  文本居中（横）：text-align: center
    3.  文本居中（竖）：行高的高度和div外面的高度一致，这时里面的内容就会垂直居中,line-height

4.  ### 背景（background）

    1.  设置背景图片：background-image

    2.  设置背景图片不重复：background-repeat: no-repeat

    3.  调整背景图片的位置：background-position:X Y

    4.  调整背景图片的大小：background-size: 宽 高

    5.  增加整个背景颜色：background-color：（）

        （）中有四种表达颜色的方式：纯英文（red）、#f0000、rgb(255,0,0)、rgba(255,0,0,.5)[包含了透明度]。

5.  ### 其他样式

    1.  调整透明度的属性：opacity
    2.  超出隐藏：overflow: hidden;
    3.  行内元素转块级元素：display: block;

上面说了行内元素和块元素。

行内元素：多个标签位于同一行（也就是不会自动换行的元素），行内元素的标签有：span /font/小标签/img/a, 等

块元素：标签可以自动换行的元素是块元素,块元素的标签有：div/h1-h6/ul/p,等

## CSS中的定位

### 	绝对定位

​	absolute：定位离开之后释放之前位置，是基于外层父级标签而言的

### 	相对定位

​	relative ：定位离开之后不释放之前位置，并且是基于之前位置而言的

### 	固定定位

​	fixed：始终是基于浏览器的定位，适合用来做广告。

### 	默认定位

​	static：默认的定位方式

### 	代码

```css
/*定位中的绝对定位*/
				position: absolute;
/*固定定位,固定在页面上的位置*/
				position: fixed;
/*相对定位*/
				position: relative;
```

### 	拓展小知识

​	把标签置于底层位置：z-index: -1;

## CSS中的盒模型

​	类似于刚买的一个新手机，会有一个盒子装着，这里的div就是你的手机，外面是有个盒子的，在浏览器中F12或者右键“检查”，然后选中div所在的地方，就会看到下图这样的东西。

![1558442927743](E:\python_document\notes\assets\1558442927743.png)

​	padding是内边距,margin是外边距，简单说说padding的用法。

```css
/*当padding后面是一个参数的时候，说明四周都是这个宽度*/
padding:10px;
/*当padding后面是两个参数的时候，先是上下的距离，再是左右的距离*/
padding:10px 20px;
/*当padding后面是四个参数的时候，顺序是这样的：上 右 下 左*/
padding: 10px 20px 30px 40px;
/*要想指定某一个方向的值，padding-有很多*/
```

margin的用法和padding一模一样，不过它有个用处，就是可以给**盒子定位**，并且要注意的是**上下不重合，左右可以重合。**

## CSS3中的选择器

### 	选择器

​		在W3cshool上扒出来的全部选择器。![1558490482781](E:\python_document\notes\assets\1558490482781.png)

### 选择器的种类

-   **基础选择器**

    ```
    *  id  class 标签
    ```

-   **关系选择器**

    ```
    >  +   ~ 
    ```

-   **伪类选择器**

    hover

-   **伪对象选择器**

    before \after

-   **属性选择器**

    input[type='text']

### 	常用的选择器

不过在编写页面的时候，用的最多的是类选择器，当出现想实现特别麻烦的时候可以考虑使用伪选择器。

#### 		伪元素选择器

1.  获得class名称是div1下面的第某个元素：

    -   第一个元素(:first-child)

        ```CSS
        .div_1>p:first-child{
        				color: red;
        			}
        ```

    -   最后一个元素(:last-child)

        ```css
        .div_1>p:last-child{
        				color: green;
        			}
        ```

    -   具体的第几个元素(:nth-child(2))

        ```css
        /*获得第几个在（）中添加就OK了*/
        .div_1>p:nth-child(2){
        				color: burlywood;
        			}
        ```

    -   单行元素(:nth-child(even))

        ```css
        .div_1>p:nth-child(even){
        				background-color:red;
        			}
        ```

    -   双行元素(:nth-child(odd))

        ```css
        .div_1>p:nth-child(odd){
        				background-color:green ;
        			}
        ```

    -   获得空元素(:nth-child(odd))

        ```css
        /*获得空的元素对象，这里指定了大小，更容易分辨*/
        .div_1>p:nth-child(odd){
        				background-color:green ;
        			}
        ```

2.  **获得焦点执行的样式：**

    -   当获得焦点时，产生变化,执行的样式

        ```css
        input:focus{
        				width: 20px;
        				height: 30px;
        			}
        ```

    -   当被选择的时候，产生变化

        ```css
        input:checked{
        				width: 20px;
        				height: 20px;
        			}
        ```

#### 	伪对象选择器

​	在指定的对象之前（或者之后插入内容）

```css
.div1:before{
				content: "我们是祖国的花朵";
				/*content:;也可以是图片，url(图片地址)*/
			}
```

#### 	属性选择器

```css
/*属性选择器，选择type为text的对象进行样式*/
input[type=text]{
				width: 300px;
				height: 40px;
}
/*属性 ^以fom开头的对象 */
input[name^='fom']{
				width: 300px;
				height: 40px;
}
```

## 利用CSS实现跳动的心

![1558511500010](E:\python_document\notes\assets\1558511500010.png)

### 	代码实现

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
		<style >
			body{
				background-color: #ffa5a5;
				animation: 1s heart infinite;
			}
			.div1{
				width: 200px;
				height: 200px;
				background-color: #D5093C;
				/*添加阴影*/
				box-shadow: 0px 0px 70px #D5093C;
			}
			.r1 {
				border-radius: 50%;
				position: absolute;
				top: 227px;
				left: 227px;
			}
			.r2{
				border-radius: 50%;
				position: absolute;
				top: 227px;
				left: 373px;
			}
			.fk{
				position: absolute;
				/*角度旋转*/
				transform: rotate(45deg);
				top: 300px;
				left: 300px;
			}
			/*添加动画效果*/
			@keyframes heart{
				0%{transform: scale(1);}
				50%{transform: scale(1.1);}
				100%{transform: scale(1);}
			}
		</style>
	</head>
	<body>
		<div class="div1 r1"></div>
		<div class="div1 r2"></div>
		<div class="div1 fk"></div>
	</body>
</html>
```

### 	知识点

1.  #### 倒圆角指令

    border-radius: 50%;（50%就是变成一个圆了）

    当“：”后面为2个值，则先左上右下，后右上左下。

    当“：”后面为4个值，则顺时针旋转，从左上开始

2.  #### transform指令

    1.  旋转角度：transform :rotate(角度)；
    2.  放大缩小：transform:scale(放大缩小的倍数)；
    3.  平移：transform:tranlate(X，Y)；
    4.  2D的旋转：transform :skew(角度，角度)

3.  #### 阴影指令

    box-shadow:水平方向的偏移  垂直方向的偏移  模糊度  阴影的颜色;

4.  动画标签

    ```css
    @keyframes name{
    	from{}
    	to{}
    }
    @keyframes name{
      0%{}
      50%{}
      100%{}
    }
    /*别忘记，规定完了要调用啊！！哪里需要就在哪里加*/
    animation:时间 名字 infinite(一直不停);
    ```

    不用的浏览器支持的动画标签不同，见下图↓↓

    ![1558513136560](E:\python_document\notes\assets\1558513136560.png)

5.  #### 浏览器中调试

    在调整div位置的时候，一直用H5会有些麻烦，那么就可以在浏览器中按F12或者右键检查，选定想要的部分，找到要更改的属性，方向键上下就可以调试了。

    ![倒圆角](E:\python_document\notes\assets\倒圆角.png)



## CSS项目搭建

### 	总述（思维导图）

​	![1558528310877](E:\python_document\notes\assets\1558528310877.png)

先分析页面把，京东购物车的静态页面分成五个部分：**导航**、**搜索框+logo**、**商品栏**、**商品展示详情**、**结算页面**，同时在实际操作之前要对整体的一个样式有要求，比如文本的居中、文本的下划线、字体等等。

```css
body,div,h1,h2,h3,h4,h5,h6,li,ol,ul{
	margin: 0px; padding: 0px;
}
body{
	text-align: center; font-size: 14px;
}
a{text-decoration: none;}
li{
	list-style: none;
}
```

### 	实际效果

![1558529377209](E:\python_document\notes\assets\1558529377209.png)

### 	第一部分：导航

**需求：文本的位置、颜色、鼠标交互实现、小型图标实现。**

#### 	文本位置、颜色

​	利用div盒子+ul+li列表实现，样式CSS文件中需要用到漂浮、字体大小颜色、内边距。

先把文本分为两个div中，（京东首页和配送至）+（右边的一长串文本）。

#### 	鼠标交互

​	用一个伪连接器（：hover）就可以搞定了。

#### 	小型图标实现

​	需要到<https://www.iconfont.cn/>（阿里巴巴矢量图标库）寻找，并且下载代码，结合Unicode代码自动去到咱需要的位置上。

#### 	第一部分代码

**HTML部分：**

```html
<!--导航开始-->
		<div class="nav">
			<div class="warp">
				<ul class="nav_ul1">
					<li><a href=""><i class="iconfont">&#xe6d3</i>京东首页</a></li>
					<li><a href="">配送至：月球</a></li>
				</ul>
				<ul class="nav_ul2">
					<li><a href="">大兄弟</a><span>|</span></li>
					<li><a href="">我的订单</a><span>|</span></li>
					<li><a href="">我的京东</a><span>|</span></li>
					<li><a href="">京东会员</a><span>|</span></li>
					<li><a href="">企业采购</a><span>|</span></li>
					<li><a href="">京东手机</a><span>|</span></li>
					<li><a href="">关注京东</a><span>|</span></li>
					<li><a href="">客户服务</a><span>|</span></li>
					<li><a href="">网站导航</a><span>|</span></li>
				</ul>
			</div>
		</div>
```

**CSS样式部分：**

```css
.nav{
	height: 30px;
	background-color: #f1f1f1;
}
.warp{
	width: 1000px;
	margin: auto;
}
.nav_ul1 , .nav_ul2 li{
	float: left;
}
.nav_ul1 li{
	float: left;
	line-height: 30px;
	margin-right: 20px;
}
.nav_ul1 a , .nav_ul2 a , .nav_ul2 span{
	color: gray;
	font-size: 12px;
	}

.nav_ul2{
	float: right;
}
.nav_ul2 li,.nav_ul2 span{
	float: left;
	line-height: 30px;
	margin-right: 10px;
}
.nav a:hover{
	color: red;
}
```

### 	第二部分：搜索框+logo

**需求：狗头的实现，搜索框的位置**

#### 	狗头的实现

直接导入需要的图片，然后调增位置使得图片出现在右上角，注意：如果浮动的样式和想要的不一样，可以用clear:both；清除之前的所有格式。

#### 	搜索框的位置

大div里套着小div，在加入两个input标签，一个text文本，一个button按钮。

#### 	第二部分代码

**HTML部分代码：**

```html
<div class="search">
			<div class="warp">
				<img src="img/dog.jpg"  />
				<div class="search_div">
					<input type="text" class="search_div_text" />
					<input type="button"  value="搜索"  class="search_div_button" />
				</div>
			</div>
		</div>
```

**CSS部分代码：**

```css
/*搜索框开始*/
.search img{
	/*如果浮动的样式和你想要的不一样的话*/
	/*清除之前的所有的样式*/
	clear: both;
	float: left;
	width: 90px;
}
.search{
	margin-top:20px;
}

.search_div{
	float: right;
	margin-top: 20px;
}
.search_div_text{
	width:265px;
	height: 21px;
	border: 3px solid #c91623;
	position: relative;
	left: 6px;
}
.search_div_button{
	width: 52px;
	height: 29px;
	background-color: #c91623;
	border: 0px;
	color: #FFFFFF;
	position: relative;
	top: 1px;
}
/*搜索框结束*/
```

### 	第三部分商品栏

第三部分细分下来可以分为两个小部分，（全部商品+配送至）①和（全选、商品…）②

**需求：完成①和完成②中相应的要求、位置、样式**

#### ①div

利用标题文字+span+select+CSS完成

#### ②div

利用div+ul+li标签，在CSS中规定样式。

#### 代码实现

**HTML部分：**

```html
<!--标题开始-->
		<div class="title warp">
			<h3>全部商品</h3>
			<div>
				<span>配送至:</span>
				<!--下拉框-->
				<select>
					<option >东城区</option>
					<option >西城区</option>
					<option >海淀区</option>
					<option >朝阳区</option>
					<option >昌平区</option>
				</select>
			</div>
		</div>
		<!--标题结束-->
		<!--显示菜单开始-->
		<div class="tips warp">
			<ul >
				<li>
					<input type="checkbox" name="" id="" value="" />
					全选
				</li>
				<li>商品</li>
				<li>单价</li>
				<li>数量</li>
				<li>小计</li>
				<li>操作</li>
			</ul>
		</div>
		<!--显示菜单结束-->
```

**CSS部分：**

```css
/*标题框开始*/
.title{
	margin-top:130px ;
}
.title h3{
	float: left;
	font-size: 23px;
	color: #c91623;
}
.title div{
	float: right;
	font-size: 14px;
	color:gray;
}

/*标题结束*/
/*显示菜单开始*/
.tips{
	width: 1000px;
	height: 50px;
	background-color: #F1F1F1;
	margin-top: 160px;
	/*也可以用下面的*/
	/*position: relative;
	top: 30px;*/
	border: 1px solid #E9E9E9;
}
.tips li{
	float: left;
	line-height: 50px;
	font-size: 12px;
	color: grey;
}

/*方式一*/
.tips li:nth-child(1){width: 90px;/*上面的红线*/border-top: 3px  solid  #C91623 ;}
.tips li:nth-child(2){margin-left: 80px;}
.tips li:nth-child(3){margin-left: 440px;}
.tips li:nth-child(4){margin-left: 70px;}
.tips li:nth-child(5){margin-left: 109px;}
.tips li:nth-child(6){margin-left: 50px;}
/*显示菜单结束*/
```

### 第四部分：商品详情

**需求：使得相应文字与上标签对齐**

#### 代码实现

**HTML实现**

```html
<!--商品详情开始-->
		<div class="info warp">
			<ul>
				<li class="info_1"><input type="checkbox" /></li>
				<li class="info_2"><img src="img/6a645f3465343536613861353561633331343933393431393133383830_mid.jpg"/></li>
				<li class="info_3"><a>【京东超市】栩栩如生手办猪</a></li>
				<li class="info_4"><a>颜色：粉+红帽</a></li>
				<li class="info_5">￥182.5</li>
				<li class="info_6">
					<button>-</button>
					<input type="text" name="" id="" value="1" />
					<button class="info_6_but2">+</button>
				</li>
				<li class="info_7">￥182.5</li>
				<li >
					<a>删除</a><br />
					<a>一刀我的关注</a>
				</li>
			</ul>
		</div>
<!--有几个商品就复制粘贴几个就OK了-->
```

**CSS代码实现：**

```css
.info{
	width:1000px;
	height: 125px;
	background-color: #fff4e8;
	border: 1px solid grey;
	margin-top:30px ;
	border-top: 3px solid grey;
}
.info li{
	float: left;
	margin-top:15px ;
}
.info a{
	font-size: 12px;
	color: #333333;
}
.info img{
	width:90%;
}
.info_1{
	margin-left: 20px;
}

.info_2{
	margin-left:20px ;
	/*border: 1px solid gray;*/
}
.info_3{
	width: 250px;
	height: 20px;
	font-weight:bold;
}
.info_4{
	margin-left:40px ;
}
.info_5{
	margin-left: 85px;
}
.info_6{
	margin-left:40px;
}
.info_6 input{
	width:40px;
	text-align: center;
	position: relative;
	top: -1px;
	left: -5px;
}
.info_6 button{
	width: 30px;
	height: 22px;
}
.info_6_but2{
	position: relative;
	left: -10px;
}
.info_7{
	margin-left: 31px;
}
```

### 第五部分:结算页面

#### 代码实现：

HTML实现

```html
		<!--结算开始-->
		
	   <div class="balance warp">
	   	
	   	   <ul class="balance_ul1">
	   	   	<li>
	   	   		
	   	   		<input type="checkbox" name="fav" id="" value=""  onclick="checkTest1(this),checkTest2()"/>
	   	   		全选
	   	   	</li>
	   	   	<li><a>删除选中商品</a></li>
	   	   	<li><a>移到我的关注</a></li>
	   	   	<li><a>清除下柜商品</a></li>
	   	   </ul>
	   	   
	   	   <ul class="balance_ul2">
	   	   	
	   	   	 <li>已经选择<span id="snum">0</span>件商品</li>
	   	   	 <li>总价 <span id="zongz">￥0</span></li>
	   	   	 <li>
	   	   	 	<button class="butt">去结算</button>
	   	   	 	
	   	   	 </li>
	   	   	
	   	   </ul>
	   	
	   	
	   </div>
		
		
		<!--结算结束-->
```

**CSS代码实现：**

```css
/*结算模块开始*/

.balance{
	
	width: 1000px;
	
	height: 50px;
	
	border: 1px  solid  gray;
	
	
	margin-top: 30px;
	
}

.balance_ul1,.balance_ul1>li,.balance_ul2>li{
	
	float: left;
	
	line-height: 50px;
	
	margin-left: 14px;
	
	
}
.balance_ul2{
	
	float: right;
}

.butt{
	
	width: 100px;
	
	height: 50px;
	
	background-color: #C91623;
	
	border: 0px;
	
	color: #FFFFFF;
	
	font-size: 20px;
	
	font-weight: bold;
	
}

.balance span{
	
	
	 font-size: 25px;
	 
	 color: #C91623 ;
	
	font-weight: bold;
}

.balance_ul2 li:nth-child(1){width: 120px;}

.balance_ul2 li:nth-child(2){width: 150px;}
```

一个copy彻底结束~静态页面可真费时间啊o(╥﹏╥)o

# JavaScript

![JS思维导图](E:\python_document\notes\assets\JavaScript.png)

## 		JS介绍

### JS的作用

1.  实现网页的动态效果，比如弹窗等等
2.  表单的校验
3.  背景图片的切换
4.  TAB菜单的切换
5.  小游戏的开发，比如贪吃蛇、飞机大战等等

### 概念和定义

​	JS一种直译式脚本语言，是一种动态类型、弱类型（体现在var）、基于原型的语言，内置支持类型。

### JS由什么组成的？

JS由三部分组成，ECMAScript、DOM、BOM。

-   ECMAScript是JS的**核心**。
-   DOM：**文档对象模型**，会把整个页面规划成由节点层级构成的文档。
-   BOM：**浏览器对象模型**，对浏览器窗口进行访问和操作。

    

## 	JS的引入方式

>   **注意**：JS的两种引入方式很相似，但是不能二合一。

### 方式一：直接镶嵌法

​	在title标签下，写个script标签，在script标签内些JS代码。

```html
<script type="text/javascript">
			/*网页中的弹框*/
			alert("js 的学习课程");
</script>
```

### 方式二：引入文件法

​	创建新JS文件，在HTML文件中引用，格式如下↓↓

```html
<script type="text/javascript" src="js/test.js" charset="UTF-8" >
</script>

```

​	对标签内参数的说明：

-   type:引入文件的类型
-   src： 引入文件的路径
-   charset:指定引入的编码（当网页出现乱码的情况，一般设置的都是utf-8）

## 	变量的使用

### 变量的声明

​	在JS中所有的变量都是用var 来声明的

### 变量使用的注意事项

-   JS中的变量的名称和java中标识符的命名保持一致
    （数字、字母、下划线、$    但不能用数字开头）
-   JS中变量名可以重复，但是后者的名称会把前者的名称的值覆盖。
-   JS中末尾即使没有"；"结束也是可以的，但是尽量加上

## 		数据类型

### 基本数据类型

-   **Number**：数字类型（注意在JS中没有浮点数的）。
-   **String**：字符串类型。
-   **Boolean**：布尔类型。
-   **Object**：对象类型，只要是new出来的都是对象类型。

### 特殊数据类型

-   **Underfined**：只是声明，但未定义，也就是没赋值。
-   **NAN**：不是一个数字not a number
-   **Null**：空对象

### 数据类型的相关操作

#### 测试变量的数据类型

```js
alert(typeof a );
```

#### 强行转变变量的数据类型

```js
//这里以number为栗子。
alert(Number(a));
```

## 			运算符

### 算术运算符

```
+		-		*		/		%		++		--
```

### 逻辑运算符

```
&		|		!		&&		||		^		<		>		＜＝		=			!=
```

### 连接符

```
+
```

### 特殊运算符

#### (==)等值符

​	先比较类型 如果类型一致，在比较内容如果类型不一致，这时候会进行强制转换统一转number类型，然后再进行内容的比较

#### (===)等同符

​	先比较类型 如果类型一致，在比较内容如果类型不一致 直接返回false；

## 		控制语句	

### 条件语句

有三种条件语句

​	if()

​	if ()else()

​	if ()else if() else if() ….else()

### 分支语句（选择语句）

```js
switch(){
  case value :
  break;
  default:
  break;
}
```

### 循环语句

也有三种循环语句

while{}

do {}while{}	至少执行一次循环体

for (var i = 0; i<10;i++){}

## JS函数的使用

### 	函数的声明

函数的声明有三种，其中1,2用的最为广泛，3了解即可

>   在方式三中，函数本身也是一个对象，所以可以那么写

#### 方式一

```js
//格式为：
function 函数名 （）{
		函数体
	};
```

#### 方式二

```js
//格式为：
var 函数名= function (){
		函数体
	};
```

#### 方式三

```js
//格式为：
var  函数名=new  Function("函数体");
```

### 	参数的传递

**在JS中实参的个数和形参的个数可以不一致。**

```js
function demo4(a,b){
				//把参数打印到浏览器的工作台上
				console.log(a+'.......'+b)
			}
demo4(1,2);//1.......2
//如果只是传入一个参数，那另一个参数默认为underfined。
demo4(1);//1.......underfined
//若传入的参数比函数规定的参数多了，那会从前往后传递，传完了就完事了，多的就不管了
demo4(1,2,3)//1.......2
```

### 	函数的返回值

```js
function demo5(a){
				console.log("参数值："+a());
				return a ;
			}
//()是函数的执行符，假如a是一个函数。
var a =function (){
				console.log("我是函数a");
			};
			demo5(a)
//如果函数没有return，返回值就是underfined
//控制台结果：我是函数a + 参数值为underfined
```

## 	JS中的对象

全部的对象以及方式见网址：<http://www.w3school.com.cn/jsref/jsref_obj_date.asp>

### 	Date对象

#### 	Date对象方法全家福

| 方法                                                         | 描述                                                   |
| :----------------------------------------------------------- | :----------------------------------------------------- |
| [Date()](http://www.w3school.com.cn/jsref/jsref_Date.asp)    | 返回当日的日期和时间。                                 |
| [getDate()](http://www.w3school.com.cn/jsref/jsref_getDate.asp) | 从 Date 对象返回一个月中的某一天 (1 ~ 31)。            |
| [getDay()](http://www.w3school.com.cn/jsref/jsref_getDay.asp) | 从 Date 对象返回一周中的某一天 (0 ~ 6)。               |
| [getMonth()](http://www.w3school.com.cn/jsref/jsref_getMonth.asp) | 从 Date 对象返回月份 (0 ~ 11)。                        |
| [getFullYear()](http://www.w3school.com.cn/jsref/jsref_getFullYear.asp) | 从 Date 对象以四位数字返回年份。                       |
| [getYear()](http://www.w3school.com.cn/jsref/jsref_getYear.asp) | 请使用 getFullYear() 方法代替。                        |
| [getHours()](http://www.w3school.com.cn/jsref/jsref_getHours.asp) | 返回 Date 对象的小时 (0 ~ 23)。                        |
| [getMinutes()](http://www.w3school.com.cn/jsref/jsref_getMinutes.asp) | 返回 Date 对象的分钟 (0 ~ 59)。                        |
| [getSeconds()](http://www.w3school.com.cn/jsref/jsref_getSeconds.asp) | 返回 Date 对象的秒数 (0 ~ 59)。                        |
| [getMilliseconds()](http://www.w3school.com.cn/jsref/jsref_getMilliseconds.asp) | 返回 Date 对象的毫秒(0 ~ 999)。                        |
| [getTime()](http://www.w3school.com.cn/jsref/jsref_getTime.asp) | 返回 1970 年 1 月 1 日至今的毫秒数。                   |
| [getTimezoneOffset()](http://www.w3school.com.cn/jsref/jsref_getTimezoneOffset.asp) | 返回本地时间与格林威治标准时间 (GMT) 的分钟差。        |
| [getUTCDate()](http://www.w3school.com.cn/jsref/jsref_getUTCDate.asp) | 根据世界时从 Date 对象返回月中的一天 (1 ~ 31)。        |
| [getUTCDay()](http://www.w3school.com.cn/jsref/jsref_getUTCDay.asp) | 根据世界时从 Date 对象返回周中的一天 (0 ~ 6)。         |
| [getUTCMonth()](http://www.w3school.com.cn/jsref/jsref_getUTCMonth.asp) | 根据世界时从 Date 对象返回月份 (0 ~ 11)。              |
| [getUTCFullYear()](http://www.w3school.com.cn/jsref/jsref_getUTCFullYear.asp) | 根据世界时从 Date 对象返回四位数的年份。               |
| [getUTCHours()](http://www.w3school.com.cn/jsref/jsref_getUTCHours.asp) | 根据世界时返回 Date 对象的小时 (0 ~ 23)。              |
| [getUTCMinutes()](http://www.w3school.com.cn/jsref/jsref_getUTCMinutes.asp) | 根据世界时返回 Date 对象的分钟 (0 ~ 59)。              |
| [getUTCSeconds()](http://www.w3school.com.cn/jsref/jsref_getUTCSeconds.asp) | 根据世界时返回 Date 对象的秒钟 (0 ~ 59)。              |
| [getUTCMilliseconds()](http://www.w3school.com.cn/jsref/jsref_getUTCMilliseconds.asp) | 根据世界时返回 Date 对象的毫秒(0 ~ 999)。              |
| [parse()](http://www.w3school.com.cn/jsref/jsref_parse.asp)  | 返回1970年1月1日午夜到指定日期（字符串）的毫秒数。     |
| [setDate()](http://www.w3school.com.cn/jsref/jsref_setDate.asp) | 设置 Date 对象中月的某一天 (1 ~ 31)。                  |
| [setMonth()](http://www.w3school.com.cn/jsref/jsref_setMonth.asp) | 设置 Date 对象中月份 (0 ~ 11)。                        |
| [setFullYear()](http://www.w3school.com.cn/jsref/jsref_setFullYear.asp) | 设置 Date 对象中的年份（四位数字）。                   |
| [setYear()](http://www.w3school.com.cn/jsref/jsref_setYear.asp) | 请使用 setFullYear() 方法代替。                        |
| [setHours()](http://www.w3school.com.cn/jsref/jsref_setHours.asp) | 设置 Date 对象中的小时 (0 ~ 23)。                      |
| [setMinutes()](http://www.w3school.com.cn/jsref/jsref_setMinutes.asp) | 设置 Date 对象中的分钟 (0 ~ 59)。                      |
| [setSeconds()](http://www.w3school.com.cn/jsref/jsref_setSeconds.asp) | 设置 Date 对象中的秒钟 (0 ~ 59)。                      |
| [setMilliseconds()](http://www.w3school.com.cn/jsref/jsref_setMilliseconds.asp) | 设置 Date 对象中的毫秒 (0 ~ 999)。                     |
| [setTime()](http://www.w3school.com.cn/jsref/jsref_setTime.asp) | 以毫秒设置 Date 对象。                                 |
| [setUTCDate()](http://www.w3school.com.cn/jsref/jsref_setUTCDate.asp) | 根据世界时设置 Date 对象中月份的一天 (1 ~ 31)。        |
| [setUTCMonth()](http://www.w3school.com.cn/jsref/jsref_setUTCMonth.asp) | 根据世界时设置 Date 对象中的月份 (0 ~ 11)。            |
| [setUTCFullYear()](http://www.w3school.com.cn/jsref/jsref_setUTCFullYear.asp) | 根据世界时设置 Date 对象中的年份（四位数字）。         |
| [setUTCHours()](http://www.w3school.com.cn/jsref/jsref_setutchours.asp) | 根据世界时设置 Date 对象中的小时 (0 ~ 23)。            |
| [setUTCMinutes()](http://www.w3school.com.cn/jsref/jsref_setUTCMinutes.asp) | 根据世界时设置 Date 对象中的分钟 (0 ~ 59)。            |
| [setUTCSeconds()](http://www.w3school.com.cn/jsref/jsref_setUTCSeconds.asp) | 根据世界时设置 Date 对象中的秒钟 (0 ~ 59)。            |
| [setUTCMilliseconds()](http://www.w3school.com.cn/jsref/jsref_setUTCMilliseconds.asp) | 根据世界时设置 Date 对象中的毫秒 (0 ~ 999)。           |
| [toSource()](http://www.w3school.com.cn/jsref/jsref_tosource_boolean.asp) | 返回该对象的源代码。                                   |
| [toString()](http://www.w3school.com.cn/jsref/jsref_toString_date.asp) | 把 Date 对象转换为字符串。                             |
| [toTimeString()](http://www.w3school.com.cn/jsref/jsref_toTimeString.asp) | 把 Date 对象的时间部分转换为字符串。                   |
| [toDateString()](http://www.w3school.com.cn/jsref/jsref_toDateString.asp) | 把 Date 对象的日期部分转换为字符串。                   |
| [toGMTString()](http://www.w3school.com.cn/jsref/jsref_toGMTString.asp) | 请使用 toUTCString() 方法代替。                        |
| [toUTCString()](http://www.w3school.com.cn/jsref/jsref_toUTCString.asp) | 根据世界时，把 Date 对象转换为字符串。                 |
| [toLocaleString()](http://www.w3school.com.cn/jsref/jsref_toLocaleString.asp) | 根据本地时间格式，把 Date 对象转换为字符串。           |
| [toLocaleTimeString()](http://www.w3school.com.cn/jsref/jsref_toLocaleTimeString.asp) | 根据本地时间格式，把 Date 对象的时间部分转换为字符串。 |
| [toLocaleDateString()](http://www.w3school.com.cn/jsref/jsref_toLocaleDateString.asp) | 根据本地时间格式，把 Date 对象的日期部分转换为字符串。 |
| [UTC()](http://www.w3school.com.cn/jsref/jsref_utc.asp)      | 根据世界时返回 1970 年 1 月 1 日 到指定日期的毫秒数。  |
| [valueOf()](http://www.w3school.com.cn/jsref/jsref_valueOf_date.asp) | 返回 Date 对象的原始值。                               |

#### 	常用方法应用实例

```js
function testDate(){
				var date = new 	Date();
				//本月中的第几天
				document.write(date.getDate()+"<br />");
				//获取今天是星期几
				document.write(date.getDay()+"<br />");
				//获取月份  但是月份在这里面是0-11的
				document.write(date.getMonth()+"<br />");
				//返回的是从1900年到现在的年份差值。
				document.write(date.getYear()+"<br />");
				//返回的全年，就是2019这样的格式
				document.write(date.getFullYear()+"<br/>");
				//返回本地的时间。
				document.write(date.toLocaleDateString()+"<br />");
			};
```

### 	Math对象

#### 	Math对象全家福

| 方法                                                         | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [abs(x)](http://www.w3school.com.cn/jsref/jsref_abs.asp)     | 返回数的绝对值。                                             |
| [acos(x)](http://www.w3school.com.cn/jsref/jsref_acos.asp)   | 返回数的反余弦值。                                           |
| [asin(x)](http://www.w3school.com.cn/jsref/jsref_asin.asp)   | 返回数的反正弦值。                                           |
| [atan(x)](http://www.w3school.com.cn/jsref/jsref_atan.asp)   | 以介于 -PI/2 与 PI/2 弧度之间的数值来返回 x 的反正切值。     |
| [atan2(y,x)](http://www.w3school.com.cn/jsref/jsref_atan2.asp) | 返回从 x 轴到点 (x,y) 的角度（介于 -PI/2 与 PI/2 弧度之间）。 |
| [ceil(x)](http://www.w3school.com.cn/jsref/jsref_ceil.asp)   | 对数进行上舍入。                                             |
| [cos(x)](http://www.w3school.com.cn/jsref/jsref_cos.asp)     | 返回数的余弦。                                               |
| [exp(x)](http://www.w3school.com.cn/jsref/jsref_exp.asp)     | 返回 e 的指数。                                              |
| [floor(x)](http://www.w3school.com.cn/jsref/jsref_floor.asp) | 对数进行下舍入。                                             |
| [log(x)](http://www.w3school.com.cn/jsref/jsref_log.asp)     | 返回数的自然对数（底为e）。                                  |
| [max(x,y)](http://www.w3school.com.cn/jsref/jsref_max.asp)   | 返回 x 和 y 中的最高值。                                     |
| [min(x,y)](http://www.w3school.com.cn/jsref/jsref_min.asp)   | 返回 x 和 y 中的最低值。                                     |
| [pow(x,y)](http://www.w3school.com.cn/jsref/jsref_pow.asp)   | 返回 x 的 y 次幂。                                           |
| [random()](http://www.w3school.com.cn/jsref/jsref_random.asp) | 返回 0 ~ 1 之间的随机数。                                    |
| [round(x)](http://www.w3school.com.cn/jsref/jsref_round.asp) | 把数四舍五入为最接近的整数。                                 |
| [sin(x)](http://www.w3school.com.cn/jsref/jsref_sin.asp)     | 返回数的正弦。                                               |
| [sqrt(x)](http://www.w3school.com.cn/jsref/jsref_sqrt.asp)   | 返回数的平方根。                                             |
| [tan(x)](http://www.w3school.com.cn/jsref/jsref_tan.asp)     | 返回角的正切。                                               |
| [toSource()](http://www.w3school.com.cn/jsref/jsref_tosource_math.asp) | 返回该对象的源代码。                                         |
| [valueOf()](http://www.w3school.com.cn/jsref/jsref_valueof_math.asp) | 返回 Math 对象的原始值。                                     |

#### 	常用方法应用实例

```js
function testMath(){
				//获得随机数
				//random的范围是0-1
				var ran= Math.random()*1000;
				
					console.log(ran);
					
					//向下取整   有小数点就把小数点删掉，只留整数部分
					console.log(Math.floor(ran));
					//向上取整    有小数点就往前进1 
					console.log(Math.ceil(ran));
					//获得四位随机数  -->验证码
					console.log(Math.floor(Math.random()*9000+1000))
				}
```

### 	String对象

#### 	String对象全家福

| 方法                                                         | 描述                                                 |
| :----------------------------------------------------------- | :--------------------------------------------------- |
| [anchor()](http://www.w3school.com.cn/jsref/jsref_anchor.asp) | 创建 HTML 锚。                                       |
| [big()](http://www.w3school.com.cn/jsref/jsref_big.asp)      | 用大号字体显示字符串。                               |
| [blink()](http://www.w3school.com.cn/jsref/jsref_blink.asp)  | 显示闪动字符串。                                     |
| [bold()](http://www.w3school.com.cn/jsref/jsref_bold.asp)    | 使用粗体显示字符串。                                 |
| [charAt()](http://www.w3school.com.cn/jsref/jsref_charAt.asp) | 返回在指定位置的字符。                               |
| [charCodeAt()](http://www.w3school.com.cn/jsref/jsref_charCodeAt.asp) | 返回在指定的位置的字符的 Unicode 编码。              |
| [concat()](http://www.w3school.com.cn/jsref/jsref_concat_string.asp) | 连接字符串。                                         |
| [fixed()](http://www.w3school.com.cn/jsref/jsref_fixed.asp)  | 以打字机文本显示字符串。                             |
| [fontcolor()](http://www.w3school.com.cn/jsref/jsref_fontcolor.asp) | 使用指定的颜色来显示字符串。                         |
| [fontsize()](http://www.w3school.com.cn/jsref/jsref_fontsize.asp) | 使用指定的尺寸来显示字符串。                         |
| [fromCharCode()](http://www.w3school.com.cn/jsref/jsref_fromCharCode.asp) | 从字符编码创建一个字符串。                           |
| [indexOf()](http://www.w3school.com.cn/jsref/jsref_indexOf.asp) | 检索字符串。                                         |
| [italics()](http://www.w3school.com.cn/jsref/jsref_italics.asp) | 使用斜体显示字符串。                                 |
| [lastIndexOf()](http://www.w3school.com.cn/jsref/jsref_lastIndexOf.asp) | 从后向前搜索字符串。                                 |
| [link()](http://www.w3school.com.cn/jsref/jsref_link.asp)    | 将字符串显示为链接。                                 |
| [localeCompare()](http://www.w3school.com.cn/jsref/jsref_localeCompare.asp) | 用本地特定的顺序来比较两个字符串。                   |
| [match()](http://www.w3school.com.cn/jsref/jsref_match.asp)  | 找到一个或多个正则表达式的匹配。                     |
| [replace()](http://www.w3school.com.cn/jsref/jsref_replace.asp) | 替换与正则表达式匹配的子串。                         |
| [search()](http://www.w3school.com.cn/jsref/jsref_search.asp) | 检索与正则表达式相匹配的值。                         |
| [slice()](http://www.w3school.com.cn/jsref/jsref_slice_string.asp) | 提取字符串的片断，并在新的字符串中返回被提取的部分。 |
| [small()](http://www.w3school.com.cn/jsref/jsref_small.asp)  | 使用小字号来显示字符串。                             |
| [split()](http://www.w3school.com.cn/jsref/jsref_split.asp)  | 把字符串分割为字符串数组。                           |
| [strike()](http://www.w3school.com.cn/jsref/jsref_strike.asp) | 使用删除线来显示字符串。                             |
| [sub()](http://www.w3school.com.cn/jsref/jsref_sub.asp)      | 把字符串显示为下标。                                 |
| [substr()](http://www.w3school.com.cn/jsref/jsref_substr.asp) | 从起始索引号提取字符串中指定数目的字符。             |
| [substring()](http://www.w3school.com.cn/jsref/jsref_substring.asp) | 提取字符串中两个指定的索引号之间的字符。             |
| [sup()](http://www.w3school.com.cn/jsref/jsref_sup.asp)      | 把字符串显示为上标。                                 |
| [toLocaleLowerCase()](http://www.w3school.com.cn/jsref/jsref_toLocaleLowerCase.asp) | 把字符串转换为小写。                                 |
| [toLocaleUpperCase()](http://www.w3school.com.cn/jsref/jsref_toLocaleUpperCase.asp) | 把字符串转换为大写。                                 |
| [toLowerCase()](http://www.w3school.com.cn/jsref/jsref_toLowerCase.asp) | 把字符串转换为小写。                                 |
| [toUpperCase()](http://www.w3school.com.cn/jsref/jsref_toUpperCase.asp) | 把字符串转换为大写。                                 |
| toSource()                                                   | 代表对象的源代码。                                   |
| [toString()](http://www.w3school.com.cn/jsref/jsref_toString_string.asp) | 返回字符串。                                         |
| [valueOf()](http://www.w3school.com.cn/jsref/jsref_valueOf_string.asp) | 返回某个字符串对象的原始值。                         |

#### 	常用方法应用实例

```js
function testString(){
				var  a = "z-x-c-v-b-n";
				// 下标为0开始的哦~
				var b = new String('zxcvbn');
				
				//获得下标为2的内容
				document.write(b.charAt(2)+"<br/>");
				
				//2 获得我们的下标
				document.write(b.indexOf("sxt")+"<br />");
				
				//字符串截取   （开始下标 ，截取长度）
				document.write(b.substr(2,3)+"<br/>");
				//截取，从下标1到最后
				document.write(b.substr(1)+"<br />");
				
				//字符串截取。（开始下标，结束下标）
				document.write(b.substring(2,3)+"<br />");
				// 截取的开始下标，效果和substr()（一个参数）的一样
				document.write(b.substring(2)+"<br />");
				
				//字符串截取的方法，按照"-"截取字符串
				document.write(a.split("-"));
			};
```

### 	Global对象（全局对象）

#### 	全家福

| 函数                                                         | 描述                                               |
| :----------------------------------------------------------- | :------------------------------------------------- |
| [decodeURI()](http://www.w3school.com.cn/jsref/jsref_decodeURI.asp) | 解码某个编码的 URI。                               |
| [decodeURIComponent()](http://www.w3school.com.cn/jsref/jsref_decodeURIComponent.asp) | 解码一个编码的 URI 组件。                          |
| [encodeURI()](http://www.w3school.com.cn/jsref/jsref_encodeuri.asp) | 把字符串编码为 URI。                               |
| [encodeURIComponent()](http://www.w3school.com.cn/jsref/jsref_encodeURIComponent.asp) | 把字符串编码为 URI 组件。                          |
| [escape()](http://www.w3school.com.cn/jsref/jsref_escape.asp) | 对字符串进行编码。                                 |
| [eval()](http://www.w3school.com.cn/jsref/jsref_eval.asp)    | 计算 JavaScript 字符串，并把它作为脚本代码来执行。 |
| [getClass()](http://www.w3school.com.cn/jsref/jsref_getClass.asp) | 返回一个 JavaObject 的 JavaClass。                 |
| [isFinite()](http://www.w3school.com.cn/jsref/jsref_isFinite.asp) | 检查某个值是否为有穷大的数。                       |
| [isNaN()](http://www.w3school.com.cn/jsref/jsref_isNaN.asp)  | 检查某个值是否是数字。                             |
| [Number()](http://www.w3school.com.cn/jsref/jsref_number.asp) | 把对象的值转换为数字。                             |
| [parseFloat()](http://www.w3school.com.cn/jsref/jsref_parseFloat.asp) | 解析一个字符串并返回一个浮点数。                   |
| [parseInt()](http://www.w3school.com.cn/jsref/jsref_parseInt.asp) | 解析一个字符串并返回一个整数。                     |
| [String()](http://www.w3school.com.cn/jsref/jsref_string.asp) | 把对象的值转换为字符串。                           |
| [unescape()](http://www.w3school.com.cn/jsref/jsref_unescape.asp) | 对由 escape() 编码的字符串进行解码。               |

#### 	常用方法应用举例

```js
function testGlobal(){
				
				var   a = 1;
				var b = "var c = 1";
				document.write(a+"<br />");
				document.write(b+"<br />");
				
				//把字符串转化为可以执行的代码！！必须记住
				eval(b);
				
				document.write(c);
				
				
				var d = "123a";
				Number(d);
				//判断是否为数字，不是数字就true  是就是flase
				document.write(isNaN(d));
				
			}
```

### 	Array（数组对象）

#### 	Array对象所有的函数

| 方法                                                         | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [concat()](http://www.w3school.com.cn/jsref/jsref_concat_array.asp) | 连接两个或更多的数组，并返回结果。                           |
| [join()](http://www.w3school.com.cn/jsref/jsref_join.asp)    | 把数组的所有元素放入一个字符串。元素通过指定的分隔符进行分隔。 |
| [pop()](http://www.w3school.com.cn/jsref/jsref_pop.asp)      | 删除并返回数组的最后一个元素                                 |
| [push()](http://www.w3school.com.cn/jsref/jsref_push.asp)    | 向数组的末尾添加一个或更多元素，并返回新的长度。             |
| [reverse()](http://www.w3school.com.cn/jsref/jsref_reverse.asp) | 颠倒数组中元素的顺序。                                       |
| [shift()](http://www.w3school.com.cn/jsref/jsref_shift.asp)  | 删除并返回数组的第一个元素                                   |
| [slice()](http://www.w3school.com.cn/jsref/jsref_slice_array.asp) | 从某个已有的数组返回选定的元素                               |
| [sort()](http://www.w3school.com.cn/jsref/jsref_sort.asp)    | 对数组的元素进行排序                                         |
| [splice()](http://www.w3school.com.cn/jsref/jsref_splice.asp) | 删除元素，并向数组添加新元素。                               |
| [toSource()](http://www.w3school.com.cn/jsref/jsref_tosource_array.asp) | 返回该对象的源代码。                                         |
| [toString()](http://www.w3school.com.cn/jsref/jsref_toString_array.asp) | 把数组转换为字符串，并返回结果。                             |
| [toLocaleString()](http://www.w3school.com.cn/jsref/jsref_toLocaleString_array.asp) | 把数组转换为本地数组，并返回结果。                           |
| [unshift()](http://www.w3school.com.cn/jsref/jsref_unshift.asp) | 向数组的开头添加一个或更多元素，并返回新的长度。             |
| [valueOf()](http://www.w3school.com.cn/jsref/jsref_valueof_array.asp) | 返回数组对象的原始值                                         |

#### 	常用函数应用实例

```js
//***************数组的声明方式*************
	
			function demo1(){
				//方式一
				var arr=new Array();
				//方式二，5代表数组的长度
				var  arr2 = new Array(5);
				console.log(arr2);
				
				//方式三  指定了具体的值
				
				var arr3 = new Array("你好",123,new String(),true);
				
				console.log(arr3);
				
				//方式四
				var  arr4 = ['asdadas',123132,new Date(),true];
				console.log(arr4);
			}
			demo1()
			
			function demo2(){
				//*****************数组的使用*************
				var arr = [];
				arr[0] = '李时珍的皮';
				arr[1] = 123;
				arr[2] = new Date();
				
				//在Java中数组的下标必须要连续的，但是在JS中可以不连续，若没有给值就是empty
				
				arr[6] = true;
				console.log(arr);
				
			}
			demo2()
			
			//***********数组的扩容*************
			function demo3(){
				var arr=["你好",123,new String(),true];
				
				console.log(arr.length );
				
				//扩大数组
				arr.length = 10;
				console.log(arr);
				//缩小数组
				arr.length = 2;
				console.log(arr);
				
			}
			demo3()
//************数组的遍历*************
			function demo4(){
				
				var arr=["你好",123,new String(),true];
				//数组遍历方式一
				for (var i = 0;i<arr.length;i++) {
					console.log(arr[i]);
				}
				//数组遍历方式二   i : 是代表数组的下标而不是具体的值
				for (var  i in arr){
					console.log(arr[i]);
				}
			}
			demo4();
			//***********数组中常用方法************
			function demo5(){
				var arr=["你好",123,new String(),true];
				console.log(arr);
				//向数组末尾添加一个或者更多元素，并返回新的长度
//				var le = arr.push("我们");
				//删除并返回数组的最后一个元素
//				var le = arr.pop();
				//删除并返回元素的第一个元素
//				var le = arr .shift()
				//向开头添加一个或者多个元素，并返回新的长度
//				var le  = arr.unshift(789);
				//删除的含义，（开始删除的下标，删除的个数）
//				arr.splice(1,2);
				
				//添加的含义，（添加的下标，0，添加的元素）
				arr.splice(1,0,"你好")
				console.log(arr);
				console.log(arr+"----------"+le);
				
			}
			demo5()
```



## JS中的事件	

​	事件就是能被 JavaScript 侦测到的行为，在网页中任何一个元素都可以触发JS事件。

### 	鼠标事件

单击+双击

```html
<input type="button" id="" value="单机操作" onclick="demo1();demo2()" />
<!--多个事件用“；”隔开-->
<input type="button" name="" id="" value="双击操作" ondblclick="demo2()"/>
```

鼠标放入

```html
<!--鼠标事件  onmouseover 放上事件   onmouseout 移开事件   onmousemove 移动事件-->
<div style="width: 300px; height: 300px; background-color:red ;"  onmousemove="demo4()"></div>
```

### 	键盘事件

```html
<!--键盘事件  onkeyup 键盘弹起    onkeydown键盘按下-->
	<input type="text" onkeyup="demo5()" />
```

### 	焦点事件

```html
<!--焦点事件  onfocus 获得焦点   onblur 失去焦点  onchange内容改变事件（必须失去焦点，放在body标签中）-->
	<input type="text" name="" id="" value="" onfocus="demo6()"/>
```

## BOM对象（Browser Object Model）

![BOM对象](E:\python_document\notes\assets\BOM对象.png)

### 		什么是BOM对象？

​	BOM对象就是一个浏览器的模型，有一系列对象组成，是访问、控制、修改浏览器属性的方法。并且每个浏览器的的标准还不一样，是DOM对象的爸爸，可以**大致等于Windows对象。**

​	为什么说是DOM对象的爸爸？看下图↓↓↓，BOM对象中包含了DOM对象，DOM对象就是BOM对象的众多下级之一。

![1559008662494](E:\python_document\notes\assets\1559008662494.png)

### 	BOM--Window常用方法

#### 三种弹框方式

-   含有确定按钮的弹窗

    ```js
    window.alert('弹框a');
    ```

-   含有确定和取消 按钮的弹窗，并且有一个返回值（true/flause）

    ```js
    var flag = window.confirm('是否删除');
    //查看返回值。
    alert(flag);
    ```

-   含有交互页面的弹窗，可以输入内容，而且也有返回值，输入什么返回什么。		

    ```js
    var va=window.prompt('亲输入昵称');
    alert(va);
    ```

#### 定时器

添加定时器：setTimeout()/setInterval()，清除定时器：clearInterval

```js
//***************定时器****************
			function getTime(){
				var date = new Date();
				//获得时间
				var time =date.toLocaleDateString();
				
				
				//获得id名称是span_1的对象
				var span = document.getElementById("span_1");
				
				span.innerHTML = time;
			}
			
			//定时器，1s之后进行方法的调用，调用一次
      //window.setTimeout("getTime()",1000);
			//没间隔一面就会进行方法的调用。
			 var in1 = window.setInterval('getTime()',1000);

			function demo4(){
				//清除定时器
				window,clearInterval(in1);
			}
//***************定时器（hTML）****************
<span id="span_1"></span>
```

#### 打开/关闭浏览器

```js
//***************打开或者关闭浏览器****************
			
			function demo5(){
				//打开先页面，另起一页
				window.open("http://www.baidu.com")
			}
			
			function demo6(){
				//关闭当前的网页
				window .close()
			}
```

### BOM对象及常用方法属性

#### 	Location

```js
//*************location对象学习*************
			function testLocation(){
				//url地址
				var  href = window.location.href;
				//当前路径的IP地址
				var hostname = window.location.hostname;
				//端口号
				var port = window.location.port;
				//主机：ip地址+端口号
				var  host = window.location.host;
				
//				alert(href+"-------"+hostname+"----------" +port+"********"+host);

			//修改当前的url
//			window.location.href = "http://www.baidu.com"
   			//			重新加载页面
			window.location.reload();
			}
```

#### 	History

```js
function testHistory(){
				//返回浏览器历史列表中的URL数量
//				var len=window.history.length;
				
				//前进\后退都是一个
				//前进的按钮
//				window.history.forward();
				//后退操作
				window.history.back();
				
				//控制我们前进和后退的网页
				//若前进x个，就x写，后退y个，就写-y .如果是0，就是刷新页面
				window.history.go(5);
			}
```

#### 	Screen

```js
function testScreen(){
			//*************screen***********
			//screen中没有方法，只有属性
			
			//获得当前屏幕的分辨率
			var he = window.screen.height;
			
			var wi = window.screen.width;
			
			alert(he+"*******"+wi);
					
			}
```

#### 	Navigator

```js
function testNavigator(){
				
				//返回客户机发送服务器的user-agent 头部的值
				var us = window.navigator.userAgent;
				alert(us)
				
			}
```



## DOM对象（Document Object Model）

![Dom对象](E:\python_document\notes\assets\Dom对象.png)

### 	什么是DOM对象？

DOM对象全称为Document Object Model，就是文件对象模型，适用于XHTML / XML的应用接口。是有一系列对象组成，是访问、检索、修改XHTML文档内容和结构的标准方法，它是跨平台与跨语言的。顶层是BOM中的**Document**。

### DOM结构节点类型

#### 		DOM的节点个数以及介绍

听过内容的不同可以给DOM大致分成三个节点（元素、属性、文本内容），可以用DOM树图来进行表示。

![DOM节点](E:\python_document\notes\assets\DOM节点.png)

​	但是在上图中，可以看到多了个文档节点和注释节点，这是更细化分了，一般来说就是三大节点。

**元素节点**：（element node）特征为

```html
<a href="链接地址">我的链接</a>
```

**属性节点**：（attribute node）由上面的例子，表示的就是href = “链接地址”

**文本节点**：（text node）链接地址、我的链接都代表的是文本节点。

​	**那么各种节点之间又有什么样的关系呢？**

#### 	DOM节点关系

分为两类，父子关系和兄弟关系。比如说，在下图中

父子关系：html就是head和body的父级，head和body就是子级.

兄弟关系： a 和h1就是兄弟关系，而title和h1元素并不是兄弟关系。

![DOM节点之间的关系](E:\python_document\notes\assets\DOM节点之间的关系.png)

注意：兄弟关系是一个爸爸的，不存在表兄弟或者堂兄弟。

### DOM获得元素节点的方式

#### 	直接获得元素的方式

-   直接通过id来获取**单个对象**
    -   方法:getElementById()

        ```js
        var  username=window.document.getElementById("username");
        ```

-   通过标签名称来获取**所有对象**（备注：空白文档也算做一个节点）

    -   方法：getElementsByTagName()

        ```js
        var  inp=document.getElementsByTagName("input");
        ```

-   通过name来获取**指定的对象**

    -   方法：getElementsByName()

        ```js
        var inp=document.getElementsByName("hobby");
        ```

#### 	间接获得元素的方式

-   通过获取父级节点来获取子级节点。

    -   属性：childNodes

        ```js
        //获得父节点
        var  professional=document.getElementById("professional");
        //获得子元素  注意：空白的文档也是一个子节点
        var  child= professional.childNodes;
        ```

-   通过获取子级节点来获取父级节点

    -   属性：parentNode

        ```js
        var  parent= p2.parentNode；
        ```

-   已知一个节点，获取下一个节点

    -   下一个包含空白文档的节点

        -   属性：nextSibling

            ```js
            var next=p2.nextSibling.nextSibling;
            ```

    -   下一个不包含空白文档的节点

        -   属性：nextElementSibling

            ```js
            var  next=p2.nextElementSibling;
            ```

-   已知一个节点，获取上一个节点

    -   上一个包含空白文档（previousSibling）
    -   上一个不包含空白文档（previousElementSibling）

### 操作元素节点对象的属性

#### 	获得节点对象的属性

-   方式一：直接获取

    ```js
    var inp1 = document.getElementById("inp1");
    var ty=inp1.type
    ```

-   方式二：getAttribute方法获取

    ```js
    inp1.getAttribute("type")
    ```

#### 操作对象的属性

-   方式一：直接更改

    ```js
    //把type属性改为button
    inp1.type ="button"
    ```

-   方式二：通过setAttribute()方法更改

    ```js
    //setAttribute(把什么，变为什么)
    inp1.setAttribute("type","button")
    ```

### 操作元素的样式

-   获得节点，通过style属性操作样式

    ```js
    //获得id名称是div1的对象
    var div = document.getElementById("div1");
    				
    //获得CSS样式
    var wi = div.style.width;
    var he = div.style.height;
    //操作元素的CSS样式，注意background-color这样的属性在JS中要使用驼峰命名法
    div.style.width="300px";
    div.style.height = "300px";
    div.style.backgroundColor = "red"
    ```

-   添加class类，来增加CSS样式

    ```js
    //通过增加class类来增加CSS样式
    div.className = "div2"
    //然后在CSS样式style中定义样式。
    <style>
    			.div2{
    				border: 1px solid black;
    			}
    </style>
    ```

### 操作元素的内容

​	不同的标签获取内容的方法不一样。

-   单标签：

    -   简单的通过value就可以查看内容

-   双标签：

    -   获取里面的HTML内容（innerHTML）

        ```js
        var  inn = div.innerHTML;
        ```

    -   获取里面的文本信息（innerText）

        -   和innerHTML的格式一致

-   特殊标签：

    -   要注意的是select（多选框）和texterea是使用value获取内容。

### 操作节点对象

​	分为创建节点、添加节点、移除节点

-   创建节点

    -   createElement(“标签名”)

        ```js
        var  p = document.createElement("p")
        ```

-   添加节点

    -   在之后添加节点（appendChild）

        ```js
        form.appendChild(p)
        ```

    -   在指定元素之前添加节点（insertBefore）

        ```js
        //lastNode是最后一个节点
        form.insertBefore(p,lastNode)
        ```

-   移除节点

    -   移除子节点

        ```
        p.removeChild(inp)
        ```

    -   移除全部（自身），格式同上。

### 案例

#### 案例一

需求：如图所示

![DOM案例1](E:\python_document\notes\assets\DOM案例1.gif)

分析：1、创建初始3*3表格，CSS样式设定，给按钮加鼠标事件。

​	    2、创建方法：获得table节点，创建一个tr和3个td节点，依次添加节点。

​	    3、给每个节点创建是添加相应内容，调用。

代码：

```html
		<style >
			tr{
				height: 70px;
			}
			td,th{
				width: 150px;
				text-align:center;
			}
		</style>
		<script >
			
			function addNode(){
				
				//获得table表格对象
				var  tab=document.getElementById("tab"); 
				//创建tr节点对象
				
				var tr =document.createElement("tr");
				//创建td对象
				
				var  td =document.createElement("td");
				
				td.innerHTML="<input type='text'  size = 10px   onblur='seaveVal(this)'/>"
				
				var  td2 =document.createElement("td");
				td2.innerHTML="<input type='text' size = 10px   onblur='seaveVal(this)'/>"
				
				var  td3 =document.createElement("td");
				td3.innerHTML="<input type='button' value='添加' size = 10px onclick = 'addNode()'/>"+
											"<input type = 'button' value = '取消' size = 10px  onclick = 'removeNode(this)'/>"
				
				tab.appendChild(tr);
				
				tr.appendChild(td);
				
				tr.appendChild(td2);
				
				tr.appendChild(td3);

			}
			
			function seaveVal(thi){
				
				//获得父级节点
				var td = thi.parentNode;
				td .innerText= thi .value;
			}
			
			
			function removeNode(thi){
				
				//获得TR节点
				var tr = thi.parentNode.parentNode;
				tr.remove()
			}
		</script>
	</head>
	<body>
				<table border="1px" align="center" id="tab">
			<tr>
				<th>图书名称</th>
				<th>图书价格</th>
				<th>操作</th>
			</tr>
			<tr>
				<td>javaSE</td>
				<td>19</td>
				<td>
					
					<input type="button" name="" id="" value="添加"  onclick="addNode()"/>
					
					<input type="button" name="" id="" value="删除"  onclick = 'removeNode(this)' />
					
				</td>
			</tr>
			<tr>
				<td>javaEE</td>
				<td>39</td>
				<td>
					
					<input type="button" name="" id="" value="添加" onclick="addNode()"/>
					
					<input type="button" name="" id="" value="删除"  onclick = 'removeNode(this)'/>
					
				</td>
			</tr>
		</table>
	</body>
```



#### 案例二

需求如图：

![DOM案例2](E:\python_document\notes\assets\DOM案例2.gif)

补充说明：1、当鼠标放在“否”时，灰色框换位置。

​		   2、点击右上角更换主题，更换背景图片。

​		   3、鼠标点击“是”，灰色框消失，背景更换。

分析：1、把静态页面构建完成。

​	    2、利用for循环，当点击右上角的按钮更换，随机更换背景图片

​	    3、利用随机数，当鼠标放在“否”上，div随机更换位置。

​	    4、鼠标点击事件onclick，点击“是”消除div并且更换背景图。

代码：

```html
		<style>
			body{
				background-image:url(img/th.jpg) ;
				background-repeat: no-repeat;
				
			}
			
			a{
				font-size: 25px;
				color: whitesmoke;
			}
			div {
				width: 300px;
				height: 200px;
				background-color:gray ;
				text-align: center;
			}
			
			input{
				width: 40px;
				height: 30px;
			}
		</style>
		<script >
			var  i = -1;
			function changbc(){
				
				var arr = ["FreshSalt_ZH-CN12818759319_1920x1080.jpg","4k-wallpaper-alps-clouds-1482927.jpg"];
				
				if(i<arr.length-1){
							i++;
				} else {
					i = 0;
				}
				
				document.body.style.backgroundImage = "url(img/"+arr[i]+")"
			}
			
			function changover(){
				var div = document.getElementById("div_1")
				div .style.marginTop = Math.random()*500+"px"
				div .style.marginLeft = Math.random()*300+"px"
			}
			
			function changclk(){
				document.body.style.backgroundImage="url(img/头像7.jpg)"
				
				document.getElementById("div_1").style.display = "none"
			}
		</script>
	</head>
	<body>
		<a href="javascript:changbc()">点击更换主题</a>
		
		<div class="div1" id="div_1">
			<h3>我是不是你的小可爱</h3>
			
			<input type="button" id="" value="是"  onclick="changclk()" />
			<input type="button"  id="" value="否"  onmouseover="changover()" />
			
		</div>
	</body>
```

## 小知识补充

​	prototype :原型类，作用是关联两个方法。



# JQuery

![JQuery](E:\python_document\notes\assets\JQuery.png)

## JQuery概述

### 什么是JQuery?

​	jQuery（全称为javaScriptQuery）是JavaScript代码库

### 为什么要用JQuery？

-   选择器功能弱
-   DOM操作繁琐之极
-   浏览器兼容性不好
-   动画效果弱

## 认识JQuery中的$

### $(function)

-   相当于window.onload=function(){}
-   功能比window.onload强大
    -   window onload一个页面只能写一个,但是可以写多个() 而不冲突。
    -   执行优先级要大于window onload
-   写法有三种
    -   $(function)
    -   jQuery(function)
    -   $(document).ready(function)

### $(selcet)

>   主要内容都在下一节选择器中

## JQuery中的选择器

### 基本选择器（一）

#### id选择器

```
/*JQ获得元素对象（id选择器）*/
var zh1 = $("#zh");
```

#### 元素选择器

```
/*元素选择器*/
var inp= $("input");
```



#### 类选择器

```
/*类选择器*/
var inp2 = $(".inp");
```



#### 通用选择器

```
/*通用选择器*/
$("*").css("background-color","green");
```

这里是为了明显一些，并加了一个背景为绿色的样式。

#### 分组选择器

```
html代码：
<div>div</div>
<p class="myClass">p class="myClass"</p>
<span>span</span>
<p class="notMyClass">p class="notMyClass"</p>

JQ代码：（获得前三个标签）
$("div,span,p.myClass")
```

### 层级选择器

#### 后代选择器

后代选择器：在给定的祖先元素下匹配所有的后代元素。

```
$("div span").css("background-color","red")
```

#### 父子选择器

//父子选择器，div下面所有的直系子元素

```
$("div>span").css("background-color","green")
```

#### 兄弟选择器

##### 紧挨着的兄弟选择器

```
//紧挨着的span标签，如果是其他标签，就不管用了。
$("#sp1 +span").css("background-color","green");
```

##### 获得指定元素后，同级标签

```
//获得指定元素后面的同级元素，也就是同级的span标签。
$("#sp1~span").css("background-color","green")
```

### 基本选择器（二）

#### 获得第一个（最后一个）元素

```
//获取第一行元素
$("ul li :first").css("background-color","red");
$("ul li ").first().css("background-color","red");
//获取最后一个元素（整体最后一个）
$("ul li :last").css("background-color","red");
$("ul li ").last().css("background-color","red");
```

#### 获得奇数（偶数）元素对象

```
//获得奇数索引的对象  索引是从零开始的
$("ul li :odd").css("background-color","green");
//获得偶数索引的对象
$("ul li :even").css("background-color","darkblue");
```

#### 获得索引为X的对象

```
//获得索引为[3]的对象
$("ul li :eq(3)").css("background-color","darkblue");
```

#### 获得大于（小于）指定索引值的对象

```
//获得大于指定索引下标大小的对象
$("ul li :gt(3)").css("background-color","darkblue");
//获得小于指定索引下标大小的对象
$("ul li :lt(3)").css("background-color","darkblue");
```

### 子选择器

#### 匹配其父元素下的第N个子或奇偶元素

```
//匹配其父元素下的第N个子或奇偶元素
//第一个元素
$("ul li:nth-child(1)").css("background-color","darkblue");
//奇数元素
$("ul li:nth-child(odd)").css("background-color","darkblue");
//隔三个获取一下
$("ul li:nth-child(3n)").css("background-color","darkblue");
```

#### 匹配第一个（最后一个）子元素

```
//匹配第一个（最后一个）子元素
$("ul li:first-child").css("background-color","darkblue");
$("ul li:last-child").css("background-color","darkblue");
```

#### 唯一子元素选择

```
html代码：
<ul>
  <li>John</li>
  <li>Karl</li>
  <li>Brandon</li>
</ul>
<ul>
  <li>Glen</li>
</ul>
JQ代码选择唯一子元素
$("ul li:only-child")
```

### 属性选择器

#### 匹配给定的属性是（不是）某个特定值的元素

```
//获得在input中type为text的全部对象
$("input[type=text]").css("background-color","red")
//获得在input中type不为text的全部对象
$("input[type!=text]").css("background-color","red")
```

#### 匹配给定的属性是以某些值开始的元素

```
//获得在input中name以z开头的全部对象
$("input[name^=z]").css("background-color","red")
```

#### 匹配给定的属性是以某些值结尾的元素

```
//name 属性以d结尾的对象
$("input[name$ = d]").css("background-color","red")
```

#### 匹配给定的属性是以包含某些值的元素

```
//name属性中包含p的对象
$("input[name*=p]").css("background-color","red")
```

#### 同时满足多个条件

```
//选择input中type为text，并且name是以z开头的对象
$("input[type=text][name^=z]").css("background-color","red")
```

### 表单选择器

#### 获取所有表单项

```
//获得from表单中的所有的表单项
$(":input");
//获得标签名称是input的所有标签对象
$("input")；
```

#### 匹配单行文本框、密码框、复选框、单选按钮、提交按钮、图像、重置按钮、所有按钮、文件。

```
//匹配表单中全部的单行文本框
$(":text").css("background-color","red")

//匹配表单中全部的密码框
$(":password").css("background-color","red")

//匹配表单中全部的复选框
$(":checkbox").css("background-color","red")

//匹配表单中全部的单选按钮
$(":radio").css("background-color","red")

//匹配表单中全部的提交按钮
$(":submit").css("background-color","red")

//匹配表单中全部的图像
$(":image").css("background-color","red")

//匹配表单中全部的重置按钮
$(":reset").css("background-color","red")

//匹配表单中全部的所有按钮
$(":button").css("background-color","red")

//匹配表单中全部的文件
$(":file").css("background-color","red")
```

### 表单对象属性选择器



#### 可用（不可用）元素

```
//匹配所有可用属性
$("input:enabled").css("background-color","red")
//匹配所有不可用属性
$("input:disabled").css("background-color","red")
其中input是可以更换的

```

#### 查找所有选中的复选框元素

```
$("input:checked")
```

#### 查找所有选中的选项元素

```
HTML 代码:
<select>
  <option value="1">Flowers</option>
  <option value="2" selected="selected">Gardens</option>
  <option value="3">Trees</option>
</select>
jQuery 代码:
$("select option:selected")
```

## JQuery操作页面的样式

### 修改，添加CSS样式

```
$(function(){
//把click单机事件绑定到bu1上
	$("#bu1").click(function(){
					
	//获得div对象
	var div1 = $("#div1");
	//获得css样式
	var wid = div1.css("width");
	var hei = div1.css("height");
	console.log(wid+"-----"+hei);
					
	//操作元素对象的css
//		div1.css("width","300px")
//		div1.css("height","400px")
//		div1.css("background-color","red")
					
	//以上内容的综合---键值对{key1:value1,key2:value2}----json数据格式
	div1.css({'width':'300px','height':'400px','background-color':'red'})
	})
})
```

### 通过添加类的方法，添加CSS样式

在style中定义一个样式类，需要样式的时候，把已经定义的类，加到目标上就ok了.

```
代码实现：
$("#div1").attr("class","div")
attr():添加可以选择的属性。
$("#div1").addClass("div")
addClass():只能是添加class.
但是修改是有优先级的排序的，id最大。
```

## 操作元素对象

### 操作元素的属性

#### 利用attr(）函数

```
//获得元素的属性----获得属性名为type的值
var te = tex.attr("type");
var cl = tex.attr("class");
//获得元素固有的属性值
var val = tex.attr("value");
					
//获得文本框实时输入的值
var val2 = tex.val();
//修改属性的值
tex,attr("type","button")
//也可以用json数据格式，{}键值对形式
tex.attr({"type":"button","value":"测试按钮"});
```

#### prop()函数

```
//用途体现在多选框，转化为布尔类型。

var flag= $("#fav").prop("checked","true");
```

### 操纵元素的内容和值

#### 获得元素对象的内容

##### 利用val（）函数获得单标签的值

```
var val = $("#inp1").val();

```

##### 获得多标签的值

###### 带有html代码

```
var ht = div.html();
```

###### 不带有html代码

```
var ht1 = div .text();
```

#### 操作元素对象的内容

##### 单标签（直接赋值）

先选择，直接使用val（“  ”）更改

##### 多标签

用html和text直接赋值，叠加则需要如下操作    div.text(div.text()+"操作内容")；

## 操作页面元素

### 添加节点

#### 添加子元素

##### 之前添加

```
//添加到现有元素之前
//方式一:
$("#div1").prepend(p);
//方式二：
p.prependTo("#div1");
```

##### 之后添加

```
//增加子元素---现有元素之后

//方式一：

$("#div1").append(p);

//方式二：

p.appendTo("#div1");
```

#### 添加兄弟标签

##### 现有元素之前添加

```
//	平级添加元素，现有元素之前
//方式一：
p.insertBefore("#div1")
//方式二：
$("#div1").before(p);
```

##### 现有元素之后添加

```
//	平级添加元素，现有元素之后
//方式一：
p.insertAfter("#div1")
//方式二：
$("#div1").after(p);
```

### 替换节点

```
$("div p:nth-child(1)").replaceWith(p);

p.replaceAll("div p:nth-child(5)")
```

### 删除节点

#### 删除指定的元素

```
$("div p:nth-child(3)").remove();
```

#### 清空内容， 里面的内容清空了，但是外面的div还存在。

```
$("#div1").empty()
```

## 事件处理

### 页面加载（ready）

### 绑定事件

#### 基础绑定

```
$("#bu1").click(function(){
			alert("单机事件")
})
```

#### bind事件绑定（一般和json类型连用）

```
$("#bu2").bind('click',function(){
		alert('单机事件')
})
```

#### one一次事件绑定

```
$("#bu3").one('click',function(){
				alert('一次事件')
})
```

#### trigger事件的绑定

```
$("#bu4").click(function(){
				
				$("#bu1").trigger('dblclick');
				
				$("#bu3").trigger('click')
		
})
```

### 事件的解绑

```
//事件的解绑--------默认为指定对象所有事件
/$("#bu1").unbind();
//指定事件
$("#bu1").unbind('click')

```

## 动画功能

动画插件网站：https://www.jq22.com/

### 显示+隐藏

```
显示

div1.show(3000)

隐藏

div1.hide(3000)

自动检测显示隐藏

$("div").toggle(3000)

提示（）中的为毫秒。
```

### 滑动

```
//滑动下
div1.slideDown(3000)

//滑动向上
div1.slideUp(3000)

//滑动上--滑动下    滑动下---滑动上
div1.slideToggle(3000)
```



### 淡入淡出

```
//淡出
div1.fadeIn(3000)

//淡入
div.fadeOut(3000)
```



## 小方法

### 通过JQ获得内容的操作

```
//JQ中获取其中的某个值。
alert(inp2.eq(0).val());
//JS中获取其中的某个值。
alert(inp2[0].value)
```



### JQ对象和JS对象的互换

```
//JS--->JQ
var zhh = $(zh);
//JQ（通过下标）--->JS对象
alert(zh1[0]);
```





​			

​			

​			



