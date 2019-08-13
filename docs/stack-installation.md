# Getting Started

If you have completed the Metabase image deployment on Cloud Platform, the following steps is for you to start use it quikly:

## Preparation

1. Get the **Internet IP address** of Cloud Server from your Cloud Platform Console
2. Check you **inbound of Security Group Rule** of Cloud Console to ensure the **TCP:80** is allowed
3. Make a domain resolution if you want to use domain for this application

## Metabase Installation Wizard

1. Using local Chrome or Firefox to visit the URL http://domain name or http://Internet IP, you will enter the configuration interface of Metabase

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-start-websoft9.png)

2.You need some time to wait for Starting Metabase...

3.Then, start to intialize it. Set adminitrator account,then set the Storage&database, suggest select the MySQL/MariaDB for your data base engine

4.You can use it now

   > Refers to the [Metabase Documentation](https://metabase.com/docs/latest/) to know more

## FAQ

#### I can't visit the start page of Metabase?

Your TCP:80 of Security Group Rules is not allowed so there no response from Chrome or Firefox

#### Which database does this image use?

MySQL
