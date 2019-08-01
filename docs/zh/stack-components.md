# 组件

Metabase部署包中不仅仅只有Metabase本身，还包含一序列支持Metabase运行所需的其他软件（这里称之为组件），下面列出主要组件名称、安装路径、配置文件地址等重要的信息：

## Metabase

Metabase安装目录: /data/wwwroot/metabase  
Metabase配置文件: /data/wwwroot/metabase/

> Metabase配置文件中包含数据库连接信息，如果您更改了MySQL数据库账号密码，此处也需要对应修改

## Java
PHP Configuration File: _/etc/php.ini_<br />PHP Modules Configuration Directory: _/etc/php.d_

## Tomcat
Apache Vhost Configuration File: _/etc/httpd/conf.d/vhost.conf_<br />Apache Configuration directory: _/etc/httpd/conf.d_<br />Apache Log Files: _/var/log/httpd_


## Nginx
Apache Vhost Configuration File: _/etc/httpd/conf.d/vhost.conf_<br />Apache Configuration directory: _/etc/httpd/conf.d_<br />Apache Log Files: _/var/log/httpd_

## MYSQL
Database install directory: /usr/local/mysql<br />Database data directory: /data/mysql<br />Database Configuration File: /etc/my.cnf<br />MySQL Management URL: _http://Internet IP/phpmyadmin_<br />_

## Redis
Redis configuration file: _/etc/redis.conf_<br />Redis data directory: _/var/lib/redis_

## Port
| MySQL | 3306 |
| --- | --- |
| Apache | 80,443 |


> 组件对应的版本号可以通过云市场商品页面查看，也可以通过[Github项目地址](https://github.com/metabase/metabase)查看。