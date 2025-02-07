# 一、python虚拟环境介绍

​	虚拟环境（virtual environment），它是一个虚拟化，从电脑独立开辟出来的环境。通俗的来讲，虚拟环境就是借助虚拟机来把一部分内容独立出来，我们把这部分独立出来的东西称作“容器”，在这个容器中，我们可以只安装我们需要的依赖包，各个容器之间互相隔离，互不影响。 



## 二、为什么要使用虚拟环境

1. 项目部署时，直接导出项目对应的环境中的库就可以了；
2. 同时开发多个项目，各自项目使用的python版本不同，譬如一个是python2，另一个是python3，那么需要来回的切换python版本；
3. 当你同时开发多个项目时，特别是多个项目使用同一个库，譬如：django，但是各自项目使用的django的版本不一致时，那么你在开发这些项目时，需要来回的卸载和安装不同的版本，因为同一个python环境中，同名的库只能有一个版本。



PS：实际项目开发时，建议每个项目使用独立的虚拟环境，但是在进行学习时，我们只使用一个虚拟环境就够了，避免频繁的创建虚拟环境，安装第三方库，浪费时间。



# 三、虚拟环境的安装

1. 安装好python环境

   

2. 安装虚拟环境库，在cmd中输入：

   ```
   pip install virtualenv 
   ```

   

3. 创建虚拟环境，在cmd中切换到需要创建虚拟环境的目录下，执行：

   ```
   virtualenv env_name 
   ```

   

4. 激活虚拟环境，在cmd中进入到 第三步创建的 env_name/Scripts 目录下，执行：

   ```
   activate
   ```

   执行成功后，在cmd中，当前输入行前面会有 (env_name) 的前缀

   在当前状态下，使用 pip 就是在虚拟环境中安装第三方库了

   

5. 退出虚拟环境，cmd中输入：

   ```
   deactivate
   ```



# 四、虚拟环境优化

​	在使用过程中，会发现上述第三步的使用，会有不少局限，譬如必须切换到指定目录才能操作等。通过安装 virtualenvwrapper-win 可以更加简便的使用虚拟环境（需要先安装virtualenv）

1. pip安装

   ```
   pip install virtualenvwrapper-win
   ```

   

2. 在环境变量中，配置虚拟环境的指定安装目录

   1. 打开系统环境变量配置

   2. 新建系统变量名：WORKON_HOME 

   3. 变量值配置为你的系统中一个指定目录，譬如：F:\python3_env

   4. 创建第3步中的文件夹

   5. 保存配置

      

3. 在cmd中运行 workon或者lsvirtualenv 即可查看当前的虚拟环境配置情况

   

4. 新建虚拟环境，cmd中输入：

   ```
   mkvirtualenv env_name
   ```

   PS：可以在cmd命令窗口的任意目录下新建，最终虚拟环境文件夹都会创建在 第 2 步中的 WORKON_HOME 指定的文件夹中

   

5. 激活虚拟环境，cmd中输入：

   ```
   workon env_name
   ```

   

6. 退出虚拟环境，cmd中输入：

   ```
   deactivate
   ```

   

7. 删除虚拟环境，cmd中输入：

   ```
   rmvirtualenv env_name
   ```

   