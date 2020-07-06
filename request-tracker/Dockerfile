FROM reg.nexus.wmq.com/tools/request-tracker-base:v4.2.16

LABEL maintainer="https://www.cnblogs.com/weavepub"

ENV RT_VERSION 4.2.16

COPY rt-${RT_VERSION}.tar.gz /usr/local/src/
RUN cd /usr/local/src \
  && tar -zxvf rt-${RT_VERSION}.tar.gz \
  && cd "rt-${RT_VERSION}" \
  && ./configure \
    --disable-gpg --disable-smime --enable-developer --enable-gd --enable-graphviz --with-db-type=SQLite \
  && make install \
  && make initdb \
  && rm -rf /usr/local/src/*

#RT LDAP Auth
RUN cpan -i RT::Authen::ExternalAuth \
  && rm -rf /root/.cpanm

COPY apache.rt.conf /etc/apache2/sites-available/rt.conf
RUN a2dissite 000-default.conf && a2ensite rt.conf

RUN chown -R www-data:www-data /opt/rt4/var/

COPY RT_SiteConfig.pm /opt/rt4/etc/RT_SiteConfig.pm

VOLUME /opt/rt4

COPY docker-entrypoint.sh /usr/local/bin/

ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["apache2-foreground"]
