# 服务启停

使用由Websoft9提供的Metabase部署方案，可能需要用到的服务如下：

### Metabase

```shell
sudo docker start metabase
sudo docker stop metabase
sudo docker restart metabase
sudo docker status metabase
```

### Nginx

```shell
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl status nginx
```

### MySQL

```shell
sudo docker start metabase-mysql
sudo docker stop metabase-mysql
sudo docker restart metabase-mysql
sudo docker status metabase-mysql
```

### Docker
```shell
sudo systemctl star docker
sudo systemctl stop docker
sudo systemctl restart docker
sudo systemctl status docker
```