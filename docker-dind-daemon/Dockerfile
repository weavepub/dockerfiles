FROM docker:dind
USER root
RUN mkdir /etc/docker && \
    sed -i "2a crond" /usr/local/bin/dockerd-entrypoint.sh && \
    crontab -l > crontab_list && \
    echo '0 3 * * * docker image prune -a -f --filter "until=24h" > /var/log/crontab.log 2>&1' >> crontab_list && \
    crontab crontab_list
ADD daemon.json /etc/docker/daemon.json