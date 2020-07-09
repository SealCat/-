### Hadoop



#### HDFS命令

> 1. 创建一个文件夹   hdfs dfs -mkdir /myTask
> 2. 创建多个文件夹   hdfs dfs -mkdir -p /myTask1/input1
> 3. 上传文件 hdfs dfs -put /opt/wordcount.txt /myTask/input
> 4. 查看总目录下的文件和文件夹 hdfs dfs -ls /
> 5. 查看myTask下的文件和文件夹 hdfs dfs -ls /myTask
> 6. 查看myTask下的wordcount.txt的内容 hdfs dfs -cat /myTask/wordcount.txt
> 7. 删除总目录下的myTask2文件夹以及里面的文件和文件夹 hdfs dfs -rmr /myTask2
> 8. 删除myTask下的wordcount.txt hdfs dfs -rmr /myTask/wordcount.txt
> 9. 下载hdfs中myTask/input/wordcount.txt到本地opt文件夹中 hdfs dfs -get /myTask/input/wordcount.txt /opt



#### 配置文件

| 配置文件        | 功能描述                                             |
| --------------- | ---------------------------------------------------- |
| hadoop-env.sh   | 配置 Hadoop 运行所需的环境变量                       |
| yarn-env.sh     | 配置 YARN 运行所需的环境变量                         |
| core-site.xml   | Hadoop核心全局配置文件，可在其它配置文件中引用该文件 |
| hdfs-site.xml   | HDFS 配置文件，继承 core-site.xml 配置文件           |
| mapred-site.xml | MapReduce 配置文件，继承 core-site.xml 配置文件      |
| yarn-site.xml   | YARN 配置文件，继承 core-site.xml 配置文件           |
| slaves          | Hadoop 集群所有从节点（DataNode 和 NodeManager）列表 |

**全部在 hadoop-2.7.7/etc/hadoop/ 目录下**

#### slaves: 节点

```shell
node02
node03
```

#### hadoop-env.sh & yarn-env.sh

**hadoop-env.sh在第25行**

**yarn-env.sh 在第23行**

![img](mdPic/27.jpg)

#### core-site.xml

```xml
<!-- HDFS集群中NameNode的URI（包括协议、主机名称、端口号），默认为 file:/// --> 
<property>  
    <name>fs.defaultFS</name>  
    <!-- 用于指定NameNode的地址 --> 
    <value>hdfs://localhost:9000</value>  
</property>  
<!-- Hadoop运行时产生文件的临时存储目录 --> 
<property>  
    <name>hadoop.tmp.dir</name>  
    <value>/root/hadoopData/temp</value>  
</property>


HDFS 垃圾回收机制配置：
<property>
    <name>fs.trash.interval</name>
    <value>1440</value>
</property>
<property>
    <name>fs.trash.checkpoint.interval</name>
    <value>0</value>
</property>

```

#### hdfs-site.xml

```xml
<!-- NameNode在本地文件系统中持久存储命名空间和事务日志的路径 --> 
<property>  
    <name>dfs.namenode.name.dir</name>  
    <value>/root/hadoopData/name</value> 
</property>  
<!-- DataNode在本地文件系统中存放块的路径 --> 
<property>  
    <name>dfs.datanode.data.dir</name>  
    <value>/root/hadoopData/data</value>  
</property>  
<!-- 数据块副本的数量，默认为3 --> 
<property>  
    <name>dfs.replication</name>  
    <value>3</value>  
</property> 


心跳机制配置：
<property>
    <name>dfs.namenode.heartbeat.recheck-interval</name>
    <value>15000</value> 
</property> 
<property> 
    <name>dfs.heartbeat.interval</name> 
    <value>3</value> 
</property> 

```

#### mapred-site.xml

```shell
# 将mapred-site.xml模板复制一份
cp mapred-site.xml.template mapred-site.xml
```

```xml
<!-- 指定使用 YARN 运行 MapReduce 程序，默认为 local --> 
<property>  
    <name>mapreduce.framework.name</name>  
    <value>yarn</value>  
</property>
```

#### yarn-site.xml

```xml
<!-- NodeManager上运行的附属服务，也可以理解为 reduce 获取数据的方式 --> 
<property>  
    <name>yarn.nodemanager.aux-services</name>  
    <value>mapreduce_shuffle</value>  
</property>
```

####  格式化文件系统(只有主节点)

```shell
hdfs namenode -format
```

### SentOS7 配置

#### 	脚本

```shell
#!/bin/bash
echo 'IP:'
read ip
echo 'HOSTNAME:'
read hn
arr=(${ip//./ })
gw="${arr[0] }.${arr[1] }.${arr[2] }.2"

echo "TYPE='Ethernet'
BOOTPROTO='static'
NAME='ens33'
DEVICE='ens33'
ONBOOT='yes'
IPADDR='$ip'
GATEWAY='$gw'
NETMASK='255.255.255.0'
DNS1='223.5.5.5'
DNS2='8.8.8.8'" > /etc/sysconfig/network-scripts/ifcfg-ens33

echo "NETWORKING=yes" > /etc/sysconfig/network

echo "$hn" > /etc/hostname

rm -r /etc/udev/rules.d/70-persistent-net.rules

systemctl stop firewalld
systemctl disable firewalld

echo "$ip $hn" >> /etc/hosts
sleep 5
reboot
```

#### profile

```shell
# HADOOP_HOME
export HADOOP_HOME=/root/software/hadoop-2.7.7
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

# JAVA_HOME
export JAVA_HOME=/root/software/jdk1.8.0_221
export PATH=$PATH:$JAVA_HOME/bin

# ZOOKEEPER_HOME
export ZOOKEEPER_HOME=/root/software/zookeeper-3.4.10
export PATH=$PATH:$ZOOKEEPER/bin

# HIVE_HOME
export HIVE_HOME=/root/software/apache-hive-2.3.4-bin
export PATH=$PATH:$HIVE_HOME/bin
```

#### 时钟同步

```shell
yum -y install ntp
设置开启自启动  
systemctl enable ntpd
启动服务
systemctl start ntpd
```

##### 	服务端

```shell
# /etc/ntp.conf 加入
server 127.127.1.0
fudge 127.127.1.0 stratum 10

systemctl restart ntpdate
```

##### 	客户端

```shell
crontab -e 
* * * * * ntpdate 服务端


crontab [-u username]　　　//省略用户表表示操作当前用户的crontab
    -e      (编辑工作表)
    -l      (列出工作表里的命令)
    -r      (删除工作作)
    
我们用crontab -e进入当前用户的工作表编辑，是常见的vim界面。每行是一条命令。
crontab的命令构成为 时间+动作，其时间有分、时、日、月、周五种，操作符有

* 取值范围内的所有数字
/ 每过多少个数字
- 从X到Z
，散列数字

```

### Zookeeper

```shell
# /conf

cp zoo_sample.cfg zoo.cfg

dataDir=/root/tmp/zookeeper # 第12行

# 在 zoo.cgf 追加
server.1=192.168.25.101:2888:3888
server.2=192.168.25.102:2888:3888
server.3=192.168.25.103:2888:3888

mkdir -p /root/tmp/zookeeper  # dataDir
vi /root/tmp/zookeeper/myid   # 在 myid 输入编号
```
