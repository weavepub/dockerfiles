## canal-server

#### 自定义配置：

conf/canal.properties

```properties
canal.serverMode = rabbitMQ
rabbitmq.host =
rabbitmq.virtual.host =
rabbitmq.exchange = 
rabbitmq.username =
rabbitmq.password =
```



conf/instance.properties

```properties
canal.instance.connectionCharset = UTF-8
canal.instance.gtidon = false
canal.instance.master.address = 127.0.0.1:3306
canal.instance.dbUsername = canal
canal.instance.dbPassword = ****
canal.instance.mysql.slaveId = 4354  
canal.instance.filter.regex = ku.biao1,ku.biao2
canal.mq.topic =
```



#### 注意事项：

canal.instance.mysql.slaveId：不同环境需要指定不同id

canal.instance.filter.regex：指定需要监控的表，不同环境需修改



#### 日志目录：

/home/admin/canal-server/logs/example