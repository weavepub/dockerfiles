FROM ubuntu:18.10
LABEL maintainer tupingping

WORKDIR /opt
RUN echo "deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ cosmic main restricted universe multiverse" > /etc/apt/sources.list && \
    echo "deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ cosmic-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ cosmic-backports main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ cosmic-security main restricted universe multiverse" >> /etc/apt/sources.list

RUN apt-get update -y && \
    apt-get install -y libmysqlclient-dev redis-server python3 python3-pip python3-dev git supervisor nginx npm net-tools vim curl wget libldap2-dev libsasl2-dev && \
    sed -i 's/bind 127.0.0.1 ::1/bind 127.0.0.1/g' /etc/redis/redis.conf && \
    npm install npm@latest -g && \
    pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U && \
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    mkdir -p /var/log/workflow && \
    mkdir /opt/workflow

# clone loonflow code
WORKDIR /opt/workflow
RUN git clone https://github.com/blackholll/loonflow.git
WORKDIR /opt/workflow/loonflow
RUN git checkout r0.3.20 && \
    echo "requests" >> requirements/common.txt && \
    pip install -r requirements/dev.txt

# clone shutongFlow code
WORKDIR /opt/workflow
RUN git clone https://github.com/youshutong2080/shutongFlow.git
WORKDIR /opt/workflow/shutongFlow/apps
RUN echo "python-ldap" >> requirements.txt && \
    echo "django_auth_ldap" >> requirements.txt && \
    pip install -r requirements.txt
WORKDIR /opt/workflow/shutongFlow/fronted
RUN npm --registry https://nexus.wmq.com/repository/npm-proxy/ install .

ADD loonflow/common.py /opt/workflow/loonflow/settings/common.py
ADD loonflow/dev.py /opt/workflow/loonflow/settings/dev.py
ADD shutongFlow/index.js /opt/workflow/shutongFlow/fronted/config/index.js
ADD shutongFlow/settings.py /opt/workflow/shutongFlow/apps/apps/settings.py
ADD shutongFlow/routers.js /opt/workflow/shutongFlow/fronted/src/router/routers.js
ADD workflow.conf /etc/nginx/conf.d/workflow.conf
ADD supervisord.conf /etc/supervisor/supervisord.conf
ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
EXPOSE 80
CMD ["/docker-entrypoint.sh", "start"]
