# Bookstrap的使用

## CSS概述
### 移动设备优先
为了绘制的页面对移动设备友好，确保适当的绘制和触屏缩放，需要在网页的 head 之中添加 viewport meta 标签
也就是`meta`标签

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
```

- width ：控制设备的宽度，参数`device_width`可以确保正确呈现在不同的设备上。
- initial-scale = 1.0 ： 表示确保页面加载的时候，是1:1进行加载的，不会有缩放的情况
- 在移动设备上，还可以添加参数`user-scalable=no` 禁用缩放（zooming）功能。
- 当maximum-scale=1.0 与 user-scalable=no 一起使用时，用户体验感极佳，但是并不所有网站都适合使用。

### 响应式图像

```html
<img src="..." class="img-responsive" alt="响应式图像">
```
```css
.img-responsive {
  display: block;
  height: auto;
  max-width: 100%;
}
```
可以按比例缩放，不会超过父元素的尺寸，图像的呈现为block,以块级元素呈现。
【注意】：这里如果想让`.img-responsive `类的图片水平居中，请使用`.center-block`类。

### 全局显示、排版和链接
#### 基本的全局显示
bookstrap中对body也进行了相应的设置：
```css
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 14px;
  line-height: 1.428571429;
  color: #333333;
  background-color: #ffffff;
}
```

- body 的默认字体样式为 "Helvetica Neue", Helvetica, Arial, sans-serif。
- 文本的默认字体大小为 14 像素。
- 默认的行高度为 1.428571429。
- 默认的文本颜色为 #333333。
- 默认的背景颜色为白色。

#### 排版

使用 @font-family-base、 @font-size-base 和 @line-height-base 属性作为排版样式。

#### 链接样式
属性 @link-color 设置全局链接的颜色
默认的样式：
```css
a:hover,
a:focus {
  color: #2a6496;
  text-decoration: underline;
}

a:focus {
  outline: thin dotted #333;
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
```
- 当鼠标悬停在链接上，或者点击过的链接，颜色会被设置为 #2a6496。同时，会呈现一条下划线.
- 点击过的链接，会呈现一个颜色码为 #333 的细的虚线轮廓
- 设置轮廓为 5 像素宽，且对于基于 webkit 浏览器有一个 -webkit-focus-ring-color 的浏览器扩展。轮廓偏移设置为 -2 像素。

### 容器（Container）
用来包裹页面上的全部信息，那么就来看看这个`<div class="container"></div>`.
```css
.container {
   padding-right: 15px;
   padding-left: 15px;
   margin-right: auto;
   margin-left: auto;
}
```
- container 的左右外边距（margin-right、margin-left）交由浏览器决定
- 内边距（padding）是固定宽度，默认情况下容器是不可嵌套的。

```css
.container:before,
.container:after {
  display: table;
  content: " ";
}
```
- 会产生伪元素。设置 display 为 table，会创建一个匿名的 table-cell 和一个新的块格式化上下文。
- :before 伪元素防止上边距崩塌
- :after 伪元素清除浮动。

如果conteneditable 属性出现在 HTML 中，可以通过使用 content: " " 来修复
```css
.container:after {
  clear: both;
}
```


## 网格系统
随着屏幕或视口（viewport）尺寸的增加，系统会自动分为最多12列。

什么是网格：简而言之，网页设计中的网格用于组织内容，让网站易于浏览，并降低用户端的负载。

什么是Bookstrap网格系统：简而言之，随着屏幕或者视口（viewport）尺寸的增加，系统会自动把屏幕分为12列。

### 工作原理
- 行必须放置在 .container class 内，以便获得适当的对齐（alignment）和内边距（padding）
- 使用行来创建列的水平组。
- 内容应该放置在列内，且唯有列可以是行的直接子元素。
- 预定义的网格类，比如 .row 和 .col-xs-4（第4级别的 ），可用于快速创建网格布局。
- 列通过内边距（padding）来创建列内容之间的间隙。该内边距是通过 .rows 上的外边距（margin）取负，表示第一列和最后一列的行偏移。
- 网格系统是通过指定您想要横跨的十二个可用的列来创建的。例如，要创建三个相等的列，则使用三个 .col-xs-4。

### 媒体查询
说白了就是对设备大小分类的一个CSS规则，分为四个类型：
```css
/* 超小设备（手机，小于 768px） */
/* Bootstrap 中默认情况下没有媒体查询 */

/* 小型设备（平板电脑，768px 起） */
@media (min-width: @screen-sm-min) { ... }

/* 中型设备（台式电脑，992px 起） */
@media (min-width: @screen-md-min) { ... }

/* 大型设备（大台式电脑，1200px 起） */
@media (min-width: @screen-lg-min) { ... }
```
有时候也可以让媒体查询代码中包含max-width,从而限制在更小的屏幕中。
比如：@media (min-width: @screen-sm-min) and (max-width: @screen-sm-max) { ... }

媒体查询是有两个部分的，先是一个设备规范，然后是一个大小规则。也就是下列的代码
```css
@media (min-width: @screen-sm-min) and (max-width: @screen-sm-max) { ... }
```

||超小设备手机（<768px）|小型设备平板电脑（≥768px）|	中型设备台式电脑（≥992px）	|大型设备台式电脑（≥1200px）|
|----|----|----|----|---|
网格行为|	一直是水平的|	以折叠开始，断点以上是水平的|	以折叠开始，断点以上是水平的|	以折叠开始，断点以上是水平的|
最大容器宽度|	None (auto)|	750px|	970px|	1170px|
Class 前缀|	.col-xs-|	.col-sm-	|.col-md-|	.col-lg-|
列数量和|	12	|12	|12	|12|
最大列宽	|Auto	|60px	|78px|	95px|
间隙宽度|	30px（一个列的每边分别 15px）|	30px（一个列的每边分别 15px）|	30px（一个列的每边分别 15px）|	30px（一个列的每边分别 15px）|
可嵌套|	Yes|	Yes|	Yes	|Yes|
偏移量|	Yes|	Yes|	Yes	|Yes|
列排序|	Yes|	Yes|	Yes	|Yes|


### 基本的网格结构
```html
<div class="container">
   <div class="row">
      <div class="col-*-*"></div>
      <div class="col-*-*"></div>      
   </div>
   <div class="row">...</div>
</div>
<div class="container">....
```

#### 简单实例 -- 