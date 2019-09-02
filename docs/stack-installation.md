# Initial Installation

If you have completed the Metabase deployment on Cloud Platform, the following steps is for you to start use it quikly

## Preparation

1. Get the **Internet IP** on your Cloud Platform
2. Check you **[Inbound of Security Group Rule](https://support.websoft9.com/docs/faq/tech-instance.html)** of Cloud Console to ensure the TCP:80 is allowed
3. Make a domain resolution on your DNS Console if you want to use domain for Metabase

## Metabase Installation Wizard

1. Using local Chrome or Firefox to visit the URL *http://domain name* or *http://Internet IP*, you will enter the register interface of Metabase
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-start-websoft9.png)
2. You may wait for 1-3 Minutes for the loading of Metabase
![开始安装Metabase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-starty-websoft9.png)

3. 点击“让我们开始吧”，接下来首先设置登录账号，完成后进入下一步
4. 添加你的数据：可以选择使用的数据类型来连接一个需要分析的外部数据库，如果没有也可以点击“我之后再添加”，这样系统会默认给 Metabase 增加一个H2演示数据
![配置Metabase](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-installdb-websoft9.png)

5. 安装成功后的界面，点击“带我去Metabase”登录后台
![Metabase安装成功](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-installss-websoft9.png)

6. 以H2演示数据为例，开始数据分析工作
![Metabase后台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-dashborad-websoft9.png)

7. Metabase有强大的系统管理能力：后台->设置->管理员，进入系统管理界面
![Metabase后台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-admin-websoft9.png)

8. 通过“添加一个数据库”来增加一个数据分析源
![Metabase后台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-adddb-websoft9.png)

9. 通过点击“人员管理”标签，管理使用Metabase用户，包括增加用户、修改密码等
![Metabase后台](https://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-users-websoft9.png)

> More useful Metabase guide, please refer to [Metabase Documentation](https://metabase.com/docs/latest/)

## Q&A

#### I can't visit the start page of Metabase?

Your TCP:80 of Security Group Rules is not allowed so there no response from Chrome or Firefox

#### Which database does this Metabase use?

MySQL
