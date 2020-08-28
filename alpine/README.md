# Alpine 镜像

使用方法示例：

1、Dockerfile

```
FROM wmht/alpine:3.12
RUN apk add --no-cache mysql-client
ENTRYPOINT ["mysql"]
```

2、build

```
docker build -t mysql-client .
```

3、use

```
docker run -it --rm mysql-client -uroot -p -h172.16.10.2 -P3306
```