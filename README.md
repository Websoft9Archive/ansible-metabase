# Metabase自动化安装与部署

## 操作系统

目前仅支持Ubuntu16.x以上

## 如何保证最新版本？

Metabase通过下载地址安装，此变量存在 `/roles/metabase/tasks/main.yml`文件中。

```
- name: Download metabase
  get_url:
    dest: /data/wwwroot/metabase
    url: http://downloads.metabase.com/v0.32.9/metabase.jar
```

## 组件

请阅读[参数表](/docs/zh/stack-components.md)

## 安装指南

支持root用户、普通用户（+su权限提升）等两种账号模式，也支持密码和秘钥对登录方式。

## 使用指南

[中文](https://support.websoft9.com/docs/metabase/zh) | [English](https://support.websoft9.com/docs/metabase)
