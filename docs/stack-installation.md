# Initial Installation

If you have completed the Metabase deployment on Cloud Platform, the following steps is for you to start use it quikly

## Preparation

1. Get the **Internet IP** on your Cloud Platform
2. Check you **[Inbound of Security Group Rule](https://support.websoft9.com/docs/faq/tech-instance.html)** of Cloud Console to ensure the TCP:80 is allowed
3. Make a domain resolution on your DNS Console if you want to use domain for Metabase

## Metabase Installation Wizard

1. Using local Chrome or Firefox to visit the URL *http://domain name* or *http://Internet IP*, you will enter the login page(if the page is not a login page, please follow steps 3-7)  
![Metabase login](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-login-websoft9.png)

2. Login it to Metabase console [(Don't know password?)](/stack-accounts.md) 
![Metabase admin](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-dashborad-websoft9.png)

3. Using local Chrome or Firefox to visit the URL *http://domain name* or *http://Internet IP*, you will enter the register interface of Metabase
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-start-websoft9.png)
4. You may wait for 1-3 Minutes for the loading of Metabase
![Start Metabase](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-starty-websoft9.png)

5. Click the **Let's get started** button and set your administrator account, then go to next step
6. Add your data: you can select the type of Database which will be analyzed or  click **I'll add my data later** then Metabase will create a Demo from H2 Database
![Add data to Metabase](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-installdb-websoft9.png)

7. Once you have completed the installation, click the button **Take me to Metabase** to log in Metabase Console
![Metabase installation successful](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-installss-websoft9.png)

8. Take the H2 demo data as an example to start data analysis work.
![Metabase H2](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-dashborad-websoft9.png)

9. Log in Metabase Console, go to **Metabase Admin** page like below
![Metabase Admin](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-admin-websoft9.png)

10. Click **Add a database** to add a new data source for Metabase
![Metabase Data source](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-adddb-websoft9.png)

11. Click **People** tab on the top of Metabase Admin, you can add user and modify password
![Metabase People](https://libs.websoft9.com/Websoft9/DocsPicture/en/metabase/metabase-users-websoft9.png)

> More useful Metabase guide, please refer to [Metabase Documentation](https://metabase.com/docs/latest/)

## Q&A

#### I can't visit the start page of Metabase?

Your TCP:80 of Security Group Rules is not allowed so there no response from Chrome or Firefox

#### Which database does this Metabase use?

MySQL
