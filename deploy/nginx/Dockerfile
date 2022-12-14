# 
# Dockerfile
# ----------------
# by Griffon Development Co., Ltd
#
# docker環境設定，指定nginx:1.15.0-alpine image 
# 將設定好的nginx設定檔放入docker環境內的指定位置

FROM nginx:1.15.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

#RUN apk update && apk add bash
#RUN bash
#RUN /bin/bash openssl req -x509 -out localhost.crt -keyout localhost.key \
#  -newkey rsa:2048 -nodes -sha256 \
#  -subj '/CN=localhost' -extensions EXT -config <( printf "[dn]\nCN=localhost\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:localhost\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth")
