FROM alpine:3.12

RUN packages=' \
    bash \
    drill \
    bind-tools \
  ' \
  set -x \
  && sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories \
  && apk --update add $packages \
  && rm -rf /var/cache/apk/*

ENTRYPOINT ["/bin/sh"]
