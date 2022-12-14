# Docker Instructions

### Env file

create `.docker` file in the root directory and add the following environment variables for building the docker images. These variables will be fed into the docker compose yml files when these containers are run. `<passowrd>` is the placeholder for the password of your choice. 

```shell
MSSQL_HOST=mssqldb
MSSQL_NAME=djangoproject
MSSQL_USERNAME=SA
MSSQL_PASSWORD=<password>
USE_MSSQL_FAKE_DATA=False

TEST_MSSQL_HOST=mssqldbtest
TEST_MSSQL_NAME=djangoproject
TEST_MSSQL_USERNAME=SA
TEST_MSSQL_PASSWORD=<password>
USE_MSSQL_FAKE_DATA=False

POSTGRES_DB=django_tutorial
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

READ_DOT_ENV_FILE=False
DATABASE_URL=postgres://postgres:postgres@db/django_tutorial
```

### **Docker DB container**

There are two docker-compose files, one to set up the databases (PostgreSQL and MSSQL server), one to set up nginx, and one to set up the production server to run the django app. The following instructions are to create these containers separately. You could pick and choose the ones you need in your project. For instance, if there are PostgreSQL and MSSQL servers in a remote machine, you might just skip those parts.

The PostgreSQL container has ports "5433:5432", so if you need to connect to this image with a django app running locally (not through another container as `docker-compose.yml` will set up), you should amend the connection string to `DATABASE_URL=postgres://postgres:postgres@localhost:5433/django_tutorial` to connect to the container DB with a proper port. The 5433 port setup is to avoid conflict of existing usage of 5432. You could adjust the docker-compose file as you see fit. 

```shell
# create db image
docker-compose -f ./deploy/docker-compose.db.yml --env-file ./.docker build

# run db container
docker-compose -f ./deploy/docker-compose.db.yml --env-file ./.docker up -d

# check db container status
docker-compose -f ./deploy/docker-compose.db.yml --env-file ./.docker ps
```

```shell
# stop db container
docker-compose -f ./deploy/docker-compose.db.yml --env-file ./.docker stop

# delete db container
docker-compose -f ./deploy/docker-compose.db.yml --env-file ./.docker down
```
---

### **Docker django container**

The docker-compose for the django container has a dependency of db. Therefore, if you want to run the compose file as is, you will need to first run the `docker-compose.db.yml` before running this compose file.

```shell
# create django image
docker-compose -f ./deploy/docker-compose.yml -f ./deploy/docker-compose.db.yml --env-file ./.docker build

# run django container
docker-compose -f ./deploy/docker-compose.yml -f ./deploy/docker-compose.db.yml --env-file ./.docker up -d

# create super user in django
docker exec -it django_tutorial-django python3 manage.py createsuperuser
```


You can refer to the following commands to check status, stop, delete
```shell
docker-compose -f ./deploy/docker-compose.yml -f ./deploy/docker-compose.db.yml --env-file ./.docker ps
docker-compose -f ./deploy/docker-compose.yml -f ./deploy/docker-compose.db.yml --env-file ./.docker stop
docker-compose -f ./deploy/docker-compose.yml -f ./deploy/docker-compose.db.yml --env-file ./.docker delete
```
---

### **Docker nginx container**

The nginx container depends on the django app container so you must run `docker-compose.yml` before running this compose file.

Create nginx image

`powershell`
```shell
docker-compose `
    -f ./deploy/docker-compose.yml `
    -f ./deploy/docker-compose.db.yml `
    -f ./deploy/docker-compose.nginx.yml --env-file ./.docker build
```

```shell
docker-compose \
    -f ./deploy/docker-compose.yml \
    -f ./deploy/docker-compose.db.yml \
    -f ./deploy/docker-compose.nginx.yml --env-file ./.docker up -d
```

Check if the app runs successfully by going to <http://localhost:8005>