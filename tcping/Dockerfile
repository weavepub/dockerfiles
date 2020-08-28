FROM busybox:1.28-glibc

COPY tcping /bin
RUN chmod 755 /bin/tcping
ENTRYPOINT ["/bin/sh"]
