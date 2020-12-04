

实现：代理`数据库的3306端口`，访问 docker 主机的 ip+port 即可。

使用方法：

```bash
docker run -it --rm -p 1234:3306 wmht/tcp-proxy db.junyue.com 3306
```



> 也可以设置环境变量 `LISTEN_PORT`，重置监控端口，默认监听端口和需要被代理的端口相同。