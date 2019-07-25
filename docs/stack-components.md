# List Included Components

The OwnCloud Stack ships the components listed below. If you want to know which specific version of each component is bundled in the stack you are installing, check the Image introduction page of marketplace. You can also find more information about each component using the links below.

You can view the version of components from our [OwnCloud Repository](https://github.com/Websoft9/ansible-phpapps/blob/master/roles/owncloud/readme.txt) on Github

<a name="OwnCloud"></a>
## OwnCloud
OwnCloud Directory: _/data/wwwroot/owncloud_<br />OwnCloud configuration :_ /data/wwwroot/owncloud/config/config.php_<br />_
> This config file was saved database configuration in the installation. You can change this file later.


<a name="PHP"></a>
## PHP
PHP Configuration File: _/etc/php.ini_<br />PHP Modules Configuration Directory: _/etc/php.d_

<a name="APACHE"></a>
## APACHE
Apache Vhost Configuration File: _/etc/httpd/conf.d/vhost.conf_<br />Apache Configuration directory: _/etc/httpd/conf.d_<br />Apache Log Files: _/var/log/httpd_

<a name="MYSQL"></a>
## MYSQL
Database install directory: /usr/local/mysql<br />Database data directory: /data/mysql<br />Database Configuration File: /etc/my.cnf<br />MySQL Management URL: _http://Internet IP/phpmyadmin_<br />_
<a name="Redis"></a>
## Redis
Redis configuration file: _/etc/redis.conf_<br />Redis data directory: _/var/lib/redis_

<a name="Port"></a>
## Port
| MySQL | 3306 |
| --- | --- |
| Apache | 80,443 |


