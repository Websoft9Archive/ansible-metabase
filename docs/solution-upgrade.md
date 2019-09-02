# Update & Upgrade

Updates and upgrades are one of the maintenance tasks for sytem. Programs that are not upgraded for a long time, like buildings that are not maintained for a long time, will accelerate aging and gradually lose functionality until they are unavailable.

You should know the differences between the terms **Update** and **Upgrade**([Extended reading](https://support.websoft9.com/docs/faq/tech-upgrade.html#update-vs-upgrade))
- Operating system patching is **Update**, Ubuntu16.04 to Ubuntu18.04 is **Upgrade**
- MySQL5.6.25 to MySQL5.6.30 is **Update**, MySQL5.6 to MySQL5.7 is **Upgrade**

For Metabase maintenance, focus on the following two Update & Upgrade jobs

- Sytem update(Operating System and Running Environment) 
- Metabase upgrade 

## System Update

Run an update command to complete the system update:

``` shell
#For Ubuntu
apt update && apt upgrade -y

#For Centos&Redhat
yum update -y
```
> This deployment package is preconfigured with a scheduled task for automatic updates. If you want to remove the automatic update, please delete the corresponding Cron

## Metabase Upgrade

Metabase有升级包的时候，后台会及时给出提示。参考下面的步骤完成升级：

1. Metabase后台->设置->升级，如果有新的升级包，系统会给与提示
![Metabase升级提示](http://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-updatereminder-websoft9.png)

2. 点击“更新”按钮后，系统会跳转到Metabase官方的安装页面。
3. 我们提供的部署包采用的是jar包安装模式，因此在安装页面我们选择“Custom install”模式，
![Metabase升级提示](http://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-updatedl-websoft9.png)

3. 下载Metabase.jar包后，上传到服务器 `/data/wwwroot/metabase`, 覆盖已有的同名文件
![Metabase升级提示](http://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-updatereplace-websoft9.png)

4. 重新加载Metabase，升级成功