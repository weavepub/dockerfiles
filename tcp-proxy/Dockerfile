FROM alpine:3.12.1

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories &&\
    apk add --no-cache bash socat

COPY tcp-proxy.sh /usr/bin/tcp-proxy
RUN chmod +x /usr/bin/tcp-proxy

ENTRYPOINT ["tcp-proxy"]
