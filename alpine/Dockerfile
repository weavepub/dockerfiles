FROM alpine:3.12
COPY scripts/mkimage-alpine.bash scripts/apk-install /
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories &&\
    apk add --no-cache bash tzdata xz &&\
    chmod 755 mkimage-alpine.bash
ENTRYPOINT ["/mkimage-alpine.bash"]
