FROM openresty/openresty:buster-fat

COPY ./nginx/nginxReloader.sh /usr/local/openresty/bin/nginxReloader.sh
COPY ./nginx/docker-entrypoint.sh /usr/local/openresty/bin/docker-entrypoint.sh

RUN chmod +x /usr/local/openresty/bin/nginxReloader.sh
RUN chmod +x /usr/local/openresty/bin/docker-entrypoint.sh

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install inotify-tools -y
EXPOSE 80
ENTRYPOINT [ "/usr/local/openresty/bin/docker-entrypoint.sh" ]
CMD ["/usr/local/openresty/bin/openresty", "-g", "daemon off;"]