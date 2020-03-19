Ansible Role: docker_phpmyadmin 
=========

本 Role 用于在CentOS或者Ubuntu服务器上安装和配置 Docker 版 phpMyAdmin。

## Requirements

运行本 Role，请确认符合如下的必要条件：

| **Items**      | **Details** |
| ------------------| ------------------|
| Operating system | CentOS7.x Ubuntu18.04 AmazonLinux|
| Python 版本 | Python2  |
| Python 组件 |    |
| Runtime |  |


## Related roles

本 Role 在语法上不依赖其他 role 的变量，但程序运行时需要确保已经运行：docker。下面以 MySQL 为例：

```
  roles:
   - {role: role_common, tags: "role_common"}   
   - {role: role_cloud, tags: "role_cloud"}
   - {role: role_mysql, tags: "role_mysql"}
   - {role: role_docker, tags: "role_docker"}
   - {role: role_docker_phpmyadmin, tags: "role_docker_phpmyadmin"}
```


## Variables

暂无

## Example

```
- name: OnlyOffice
  hosts: all
  become: yes
  become_method: sudo 
  vars_files:
    - vars/main.yml 

  roles:
   - {role: role_common, tags: "role_common"}   
   - {role: role_cloud, tags: "role_cloud"}
   - {role: role_mysql, tags: "role_mysql"}
   - {role: role_docker, tags: "role_docker"}
   - {role: role_docker_phpmyadmin, tags: "role_docker_phpmyadmin"}
```

## FAQ
