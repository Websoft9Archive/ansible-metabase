# Metabase Notes

组件名称：Metabase
安装文档：https://www.metabase.com/start/jar.html
配置文档：
支持平台： Debian家族 | RHEL家族 | Windows | macOS |Docker|  Kubernetes | 

责任人：zxc

## 概要

Metabase是一个数据可视化工具,可以帮助你把数据库中的数据更好的呈现给更多人。

## 环境要求

* 程序语言：
* 应用服务器：java
* 数据库：自行连接
* 依赖组件：jdk
* 其他：

## 安装说明

采用官方其他通用的安装方法,直接在官网下载metabase.jar包,配置好java环境后直接运行即可。

下面基于不同的安装平台，分别进行安装说明。

### CentOS

```shell
#下载meitabase.jar
sudo wget https://downloads.metabase.com/v0.35.2/metabase.jar

# 安装jdk(需jjdk 1.8及以上版本,openjdk或ocacle均可)
列出jdk版本:rpm -qa |grep jdk         
安装 jdk     : rpm -ivh 版本号

#配置java环境
vi /etc/profile 
在文件最末尾写上:
export JAVA_HOME=/usr/java/jdk1.8.0_151
export JRE_HOME=$JAVA_HOME/jre
export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
export PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH
重新加载该配置文件
source /etc/profile

#运行jar
java -jar metabase.jar

访问时应在防火墙上增设3000端口
firewall-cmd --permanent --add-port=3000/tcp
firewall-cmd --reload
```

## 路径

* 程序路径：
* 日志路径：
* 配置文件路径：
* 其他...

## 配置

安装完成后，完成如下配置

```shell
安装完成后，完成如下配置

```shell
#创建 metabase用户和配置metabase所需文件
   sudo groupadd -r metabase
   sudo useradd -r -s /bin/false -g metabase metabase
   sudo chown -R metabase:metabase </your/path/to/metabase/directory>
   sudo touch /var/log/metabase.log
   sudo chown metabase:metabase /var/log/metabase.log
   sudo touch /etc/default/metabase
   sudo chmod 640 /etc/default/metabase

#配置metabase日志文件  
sudo touch /etc/rsyslog.d/metabase.conf
if $programname == 'metabase' then /var/log/metabase.log
& stop

#环境变量配置  /etc/default/metabase
MB_PASSWORD_COMPLEXITY=<weak|normal|strong>
MB_PASSWORD_LENGTH=<10>
MB_JETTY_HOST=<0.0.0.0>
MB_JETTY_PORT=<12345>
MB_DB_TYPE=<postgres|mysql|h2>
MB_DB_DBNAME=<your_metabase_db_name>
MB_DB_PORT=<5432>
MB_DB_USER=<your_metabase_db_user>
MB_DB_PASS=<ssshhhh>
MB_DB_HOST=<localhost>
MB_EMOJI_IN_LOGS=<true|false>
# any other env vars you want available to Metabase


```

## 服务

本项目安装后无服务

## 环境变量
JAVA_HOME   JRE_HOME  CLASSPATH     PATH


## 版本号

通过如下的命令获取主要组件的版本号: 

```
# Check Metabase version

```

## 常见问题

#### 有没有管理控制台？

*http://your host/setup* 即可访问控制台,按照提示创建user,password,email

#### 本项目需要开启哪些端口？

| item      | port  |
| --------- | ----- |
|  java      | 3000 |


#### 有没有CLI工具？

无

## 日志

* 2020-04-17完成CentOS安装研究
