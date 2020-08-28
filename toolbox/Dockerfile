FROM alpine:3.12
# Alpine镜像是musl的libc，tcping属于gnu libc的软件
# gnu libc的软件最好使用其他发行版的linux，如:busybox
# https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
# https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.29-r0/glibc-2.29-r0.apk


COPY tcping /bin/tcping
COPY glibc/sgerrand.rsa.pub /etc/apk/keys/sgerrand.rsa.pub
COPY glibc/glibc-2.29-r0.apk /

RUN packages=' \
    bash \
    drill \
    vim \
    curl \
    bind-tools \
  ' \
  set -x \
  && sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories \
  && apk --update add $packages \
  # install gun libc
  && apk add glibc-2.29-r0.apk \
  && rm -rf /var/cache/apk/* \
  && chmod 755 /bin/tcping

ENTRYPOINT ["/bin/sh"]