FROM atlassian/jira-software:8.13.3
# ubuntu20
RUN echo "deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse" > /etc/apt/sources.list &&\
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse" >> /etc/apt/sources.list &&\
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse" >> /etc/apt/sources.list &&\
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse" >> /etc/apt/sources.list

RUN set -ex &&\
    apt-get update &&\
    apt-get install -y vim net-tools wget
    
# 上传代理破解包，mysql5.7驱动
COPY atlassian-agent.jar /opt/atlassian/jira/
COPY mysql-connector-java-5.1.49.jar /opt/atlassian/jira/lib

# 启动时加载代理包
RUN echo 'export CATALINA_OPTS="-javaagent:/opt/atlassian/jira/atlassian-agent.jar ${CATALINA_OPTS}"' >> /opt/atlassian/jira/bin/setenv.sh