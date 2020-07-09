# 【Linux】卸载Linux自带python2

**Linux卸载自带python:**

1.强制删除已安装python及其关联 \##xargs，允许你对输出执行其他某些命令

rpm -qa|grep python|xargs rpm -ev --allmatches --nodeps

2.删除残余文件

whereis python|xargs rm -frv

 

**Liunx安装python3:**

```shell
yum install -y gcc patch libffi-devel python-devel  zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
```

先进入或者创建一个文件夹，比如 cd /home

1.下载python3

wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz

2.解压安装包

tar zxvf Python-3.7.0.tgz

3.解压好后转到该安装包目录下

cd Python-3.7.0

4.对安装进行配置，并指定安装路径

./configure --prefix=/usr/local/python37

5.make 编译

6.make install 安装