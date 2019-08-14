### Anaconda

Anaconda是Python的一个免费发行版本，里面集成集成python解释器。它包含很多数据科学计算的软件包与开发工具，非常适合数据科学与机器学习领域开发。

#### 下载与安装

我们可以登录<https://www.anaconda.com/distribution/>下载

安装过程一路next，注意其中一步需要将Anaconda注册到环境变量中

![Image Anaconda安装注意点](Anaconda安装注意点.png)

#### 虚拟环境

* 创建虚拟环境

  conda create -n 虚拟环境名称 python=版本号

* 删除虚拟环境

  conda remove -n 虚拟环境名称 --all

* 激活(进入)虚拟环境

  activate 虚拟环境名称

* 离开虚拟环境

  deactivate 虚拟环境名称

说明：

* 创建虚拟环境后，会在Anaconda安装目录的envs目录下，创建虚拟环境相关文件

* 创建的虚拟环境仅安装一些必须软件包，例如pip等。如果需要安装Anaconda所有库，需要：

  conda create -n 虚拟环境名称 python=版本号 anaconda

#### conda包管理器

conda是一个包管理器，可用来下载(删除)Python软件包(与pip有些类似)

- 安装包

  conda install 包

- 卸载包

  conda remove 包

- 更新包

  activate update 包

* 查看包

  conda list










