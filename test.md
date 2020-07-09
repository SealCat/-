##### 1.登录MySQL

​	mysql -h localhost(IP地址) -P 3306(端口) -u root(用户名) -p000000(密码)

##### 2.Python 中文

​	\u4e00 - \u9fff

##### 3.pycharm 中自动补全代码提示前符号 p，m ，c，v, f 是什么

​	p：parameter 参数
​	m：method 方法
​	c：class 类
​	v：variable 变量
​	f：function 函数

##### 4.python pip安装包的三种方式 ： 在线安装，setup.py安装，whl文件安装

###### 	1.在线安装

　	　pip install xx

​	　　如果网络不好可以使用国内镜像， pip install xx -i http://xxx

​	　　国内的几个常用镜像地址：

​				豆瓣 ： https://pypi.douban.com/simple

​				中国科学科技大学 ： https://mirrors.ustc.edu.cn/pypi/web/simple/

​				清华大学 ：https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/

###### 	2.离线安装

​	　　　　1.下载好压缩包 ->解压 -> 在解压目录的当前文件夹下，打开终端

　		　　　  输入 ： python setup.py install

​					2.whl文件安装 ： 当前目录下运行 ：pip install xxx.whl

##### 5.请求

http     -> tcp               -> ip          -> arp      ->网线

应用层 ->  传输控制层 -> 网络层 -> 链路层 -> 物理层



##### 6.(Xpath)如何选择不包含某一个属性的节点?

可以使用例如//tbody/tr[@class]来选择。那么不含某属性的节点如何用xpath取得呢？

这里可以用到not。例如排除一个属性的节点可以使用//tbody/tr[not**(@class)**]来写，排除一个或者两个属性可以使用**//tbody/tr[not(@class or @id)]**来选择。 **(注意用括号括起来）**

##### 7.Linux passwd

- -l 锁定口令，即禁用账号。
- -u 口令解锁。
- -d 使账号无口令。

