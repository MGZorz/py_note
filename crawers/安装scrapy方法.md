### 装scrapy

#### 前提环境
1. twisted
    1. 方法1：copy 文件夹 copy到$python_home/lib/site-packages
        1. Twisted-17.9.0-py3.6.egg-info
        1. twisted
    2. 方法2：通过安装文件whl
        1.  将文件copy到$python_home/Scripts
        2.  pip install Twisted-17.9.0-cp35-cp35m-win_amd64.whl
    3. 方法3： 直接安装包(比较慢)
        1. visualcppbuildtools_full.exe
2. pypiwin32|pywin32
    1. `pip install pywin32`
3. pip install scrapy
4. 在shell|Terminal中执行scrapy
    如果没有提示不能识别此命令，就说明安装成功了