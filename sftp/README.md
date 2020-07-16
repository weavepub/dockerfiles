# sftp 服务

参考：[atmoz/sftp](https://hub.docker.com/r/atmoz/sftp)

说明：根据user.conf文件，启动时候自动创建用户；每次更新该文件不会自动创建，需重启服务才能创建；并该文件用挂载形式实现更新。



#### 1 docker 上部署

**1）指定账号密码运行**

/opt/users.conf

```
foo:123:1001:100:data
bar:abc:1002:100:data
baz:xyz:1003:100:data
```

> 语法: user:pass:uid:gid:dir

运行

```shell
docker run -itd \
    -v /opt/users.conf:/etc/sftp/users.conf:ro \
    -v mySftpVolume:/home \
    -p 32101:22 wmht/sftp-key
```

**2）指定密钥运行**

/host/users.conf

```
foo::1001:100:PH003
bar::1002:100:PH003
baz:123:1003:100:PH003
```

运行

```
docker run -it \
    -v /host/users.conf:/etc/sftp/users.conf:ro \
    -v /opt/sftp/sshkey/ssh_host_rsa_key.pub:/home/foo/.ssh/keys/id_rsa.pub:ro \
    -v /opt/sftp/sshkey/ssh_host_rsa_key.pub:/home/bar/.ssh/keys/id_rsa.pub:ro \
    -v /host/data:/home \
    -p 2222:22 -d wmht/sftp-key
```

> 说明：foo、bar用户采用密钥登陆，baz用户采用密码登陆。



#### 2 rancher 部署注意事项

rancher部署参考：[Setting up a FTP-server in Kubernetes](https://cloudlets.io/en/kubernetes-blog/setting-up-ftp-server-in-kubernetes/)

1）账号配置文件，同docker部署的配置文件

2）挂载卷：配置文件容器路径为 /etc/sftp，权限400；数据卷容器路径为 /home

3）rancher中挂载users.conf配置映射卷时为容器路径，非文件



#### 3 连接方式

账号密码连接

```shell
sftp -P 32101 foo@172.16.6.116
```

密钥连接

```bash
sftp -i ssh_host_rsa_key -P 32106 foo@172.16.6.116
```

