# 
# Dockerfile
# ----------------
# by Griffon Development Co., Ltd
#
# docker環境設定，指定ubuntu:18.04 image 
# 安裝microsoft odbc、python3.9、project requirements

FROM ubuntu:18.04

 # install microsoft odbc
 RUN apt-get update -y && apt-get install sudo -y
 RUN apt-get update && apt-get install -y gnupg2
 RUN apt-get install curl -y
 RUN sudo su
 RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
 RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
 RUN exit
 RUN sudo apt-get update
 RUN sudo apt-get install libcurl3 -y
 RUN sudo ACCEPT_EULA=Y apt-get install msodbcsql -y
 # optional: for bcp and sqlcmd
 RUN sudo ACCEPT_EULA=Y apt-get install mssql-tools -y
 RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
 RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
 RUN /bin/bash -c "source ~/.bashrc"
 # optional: for unixODBC development headers
 RUN sudo apt-get install unixodbc-dev -y

 # install python 3.9
 RUN sudo apt-get update
 RUN sudo apt-get install software-properties-common -y
 RUN sudo add-apt-repository ppa:deadsnakes/ppa
 RUN sudo apt-get install python3.9 -y
 RUN sudo apt-get install python3.9-distutils -y
 RUN sudo ln -sf /usr/bin/python3.9 /usr/bin/python3

# install requirements
 RUN sudo apt install python3-pip -y
 RUN apt-get clean && apt-get update && apt-get install -y locales
 RUN locale-gen en_US.utf8 && update-locale
 RUN mkdir -p /app/requirements
 ADD ./requirements /app/requirements
 RUN pip3 install --upgrade setuptools
 RUN pip3 install --upgrade pip
 RUN pip3 install --upgrade distlib
 RUN pip3 install -r /app/requirements/base.txt
 RUN sudo apt-get update
 RUN sudo apt-get install libpq-dev -y && pip3 install -r /app/requirements/production.txt;
 RUN mkdir /src

 RUN apt-get update && \
     DEBIAN_FRONTEND=noninteractive apt-get -qq install tzdata

 RUN ln -fs /usr/share/zoneinfo/Asia/Taipei /etc/localtime
 RUN dpkg-reconfigure --frontend noninteractive tzdata

 WORKDIR /src
