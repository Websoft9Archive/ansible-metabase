# 初始化安装

在云服务器上部署了 Metabase 镜像之后，请参考下面的步骤来使用它。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 如果您打算通过域名访问Metabase软件，请通过域名控制台完全一个域名解析（非必须）

## Metabase 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：http://domain name 或 http://Internet IP, 就进入了软件的引导首页
![Metabase初始化页面](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-start-websoft9.png)

2. 软件的加载速度比较慢，耐心等待1-3分钟，直至出现如下的界面。

3. 接下来，设置登录账号，并连接第一个需要分析的数据库

4. 如果暂时没有需要连接的数据库，系统会默认给 Metabase 增加一个H2演示数据

5. 以H2演示数据为例，开始数据分析工作

6. 需要了解更多Metabase的使用，请参考官方文档：[Metabase Documentation](https://metabase.com/docs/latest/)

## 常见问题

#### 浏览器打开IP地址，无法访问Metabase（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 本部署包采用的哪个数据库来存储 Metabase 数据？

是MySQL，不是默认的H2，H2只能用于测试环境
