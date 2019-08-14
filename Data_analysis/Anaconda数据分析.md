# Anaconda

#### 介绍

Anaconda是python免费发行的一个版本，集成了python解释器以及很多科学计算的软件与开发工具。

#### 虚拟环境

利用Anaconda对虚拟环境进行操作。

- conda create -n 名字 python=版本号
- conda info –envs （显示已存在虚拟环境）
- conda remove -n 名字 --all
- activate 名字    （激活虚拟环境）
- deactivate 名字 （关闭虚拟环境）

> ###### 说明
>
> - 创建虚拟环境后，会在Anaconda安装目录的envs目录下，创建虚拟环境相关文件。
> - 刚创建的虚拟环境只有pip，要想添加Anaconda所有库，需要：`conda create -n 名字 python=版本号 anconda`
>
> ###### conda包管理器 （类似于pip）
>
> - conda install  包
> - conda remove 包
> - activate update 包   （更新）
> - conda list （查看）