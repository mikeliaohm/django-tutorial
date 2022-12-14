# 
# Dockerfile
# ----------------
# by Griffon Development Co., Ltd
# 
# Specify the steps in the building and running of the DB container for the
# django tutorial project, there is a backup database djangoproject.bak located
# in the same folder as this file for which the script written below will 
# restore. The default username is SA and default password is Aa1234567.

FROM mcr.microsoft.com/mssql/server:2017-latest

ARG SA_PASSWORD
ARG ACCEPT_EULA

ENV SA_PASSWORD=$SA_PASSWORD
ENV ACCEPT_EULA=$ACCEPT_EULA

COPY ./deploy/db/djangoproject.bak /var/opt/mssql/backup/djangoproject.bak
RUN ( /opt/mssql/bin/sqlservr & ) | grep -q "Service Broker manager has started" \
    && /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P $SA_PASSWORD -Q "RESTORE DATABASE [djangoproject] FROM DISK = N'/var/opt/mssql/backup/djangoproject.bak' WITH  FILE = 7,  MOVE N'djangoproject' TO N'/var/opt/mssql/data/djangoproject.mdf',  MOVE N'djangoproject_log' TO N'/var/opt/mssql/data/djangoproject_log.ldf',  NOUNLOAD,  STATS = 5 " \
    && pkill sqlservr
