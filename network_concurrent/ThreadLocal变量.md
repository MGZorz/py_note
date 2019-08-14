每一个线程都可以使用所属进程的全局变量。

每个线程都有自己独立的数据。



1、全局变量threadLocal就是一个ThreadLocal对象，每个Thread对threadLocal变量都可以读写student属性，但互不影响。

2、 一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。

3、 ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题，真正做到了线程之间的数据隔离。

4、 你可以把threadLocal看成全局变量，但每个属性如threadLocal.student都是线程的局部变量，可以任意读写而互不干扰，也不用考虑锁的问题，ThreadLocal内部会处理。

5、 按课程步骤，你也可以理解全局变量threadLocal是一个dict，不但可以用threadLocal.student，还可以绑定其他变量，如threadLocal.teacher等等。

6、ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。