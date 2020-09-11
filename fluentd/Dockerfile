FROM fluent/fluentd:v1.9-debian-1
USER root
RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-document", "--version", "4.1.3"]
RUN sed -i 's/999/0/g' /etc/passwd
USER fluent