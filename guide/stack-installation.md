# Getting Started with OwnCloud

It is recommended to complete OwnCloud installation wizard according to the following steps :

<a name="jUJ4p"></a>
## Preparation

1. Get the _Internet IP address_ of Cloud Server from Cloud Platform Console
1. Check you** inbound of Security Group Rule** to ensure the **TCP:80** is allowed
1. Complete domain resolution if you want to use domain for this application

<a name="zs3Ct"></a>
## Owncloud Installation Wizard<br /><br />

1. Using local Chrome or Firefox to visit **_http://Domain_** or **_http://Internet IP_**, you will enter the configuration interface of Owncloud installation

1. Set adminitrator account,then set the Storage&database, suggest select the MySQL/MariaDB for your database engine

3. Fill in your database configuration.It's very important and easy to make mistakes on this step

-Database user: `root` or `set by yourself`<br />-Database password: get it from file _/credentials/password.txt_ on your Cloud Server<br />-Database name: `owncloud` (MySQL on this Image has a created this database)

[![](https://cdn.nlark.com/yuque/0/2019/png/152462/1552201392332-71ddbf0a-4cde-4b44-92bf-ea0950c5c562.png#align=left&display=inline&height=644&originHeight=858&originWidth=960&size=0&status=done&width=720)](http://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-install-websoft9.png)

3. Once filish the setup,log in to OwnCloud<br />[![](https://cdn.nlark.com/yuque/0/2019/png/152462/1552201821717-2b638c9f-8248-491d-bd0d-f7631b4c16f2.png#align=left&display=inline&height=314&originHeight=418&originWidth=960&size=0&status=done&width=720)](http://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-login-websoft9.png)

3. OK, it has been installed successfully.<br />[![](https://cdn.nlark.com/yuque/0/2019/png/152462/1552201846779-34f2932d-302b-41bf-af1d-f81a20caf2d2.png#align=left&display=inline&height=288&originHeight=546&originWidth=1366&size=0&status=done&width=720)](http://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/oc04.png)<br />

> Refers to the [OwnCloud Documentation](https://doc.owncloud.org/server/index.html) to get start your OwnCloud tutorial

<br />
<a name="hiaI0"></a>
## FAQ

- **I can't enter the Owncloud installation wizard? **<br />Your TCP:80 of Security Group Rules is not allowed or incorrect setting

- **Can I  use another database connection that is not belong to this image? **<br />Yes, you can use any database that was supported and can be connected for OwnCloud
