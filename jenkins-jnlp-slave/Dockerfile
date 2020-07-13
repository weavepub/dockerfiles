FROM jenkins/jnlp-slave:3.35-4
ENV KUBECTL_VERSION=v1.18.5
USER root
RUN echo "deb http://mirrors.tuna.tsinghua.edu.cn/debian/ stretch main contrib non-free" > /etc/apt/sources.list && \
    echo "deb http://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-updates main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.tuna.tsinghua.edu.cn/debian/ stretch-backports main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.tuna.tsinghua.edu.cn/debian-security stretch/updates main contrib non-free" >> /etc/apt/sources.list
RUN apt-get update && \
    apt-get -y install apt-transport-https ca-certificates curl software-properties-common && \
	curl -L https://docs.rancher.cn/download/kubernetes/linux-amd64-${KUBECTL_VERSION}-kubectl -o /usr/local/bin/kubectl && \
	chmod +x /usr/local/bin/kubectl && \
    curl -fsSL http://mirrors.aliyun.com/docker-ce/linux/debian/gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/debian $(lsb_release -cs) stable" && \
    apt-get -y update && \
    apt-get -y install docker-ce