# django-tutorial

This project uses python 3.9，using other python version may cause some problems

&nbsp;

## Install package

&nbsp;

install package by `pip`

```shell
pip install -r requirements/base.txt
```

&nbsp;

if working for production, need to install production.txt

```shell
pip install -r requirements/production.txt
```

&nbsp;

---

&nbsp;

## Install Microsoft ODBC driver

&nbsp;

To connect sql server, we need to install microsoft ODBC driver
This project uses `ODBC Driver 13 for SQL Server`

### For windows

[download](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16) windows installer and install

&nbsp;

### For Ubuntu

please follow steps from [microsoft official web](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16)

&nbsp;

---

&nbsp;

## Database settings

&nbsp;

create `.sql` in root path, `MSSQL_HOST` and `TEST_MSSQL_HOST` can't be the same

&nbsp;

`.sql`

```sql
MSSQL_HOST=<host>
MSSQL_NAME=djangoproject
MSSQL_USERNAME=<username>
MSSQL_PASSWORD=<password>
USE_MSSQL_FAKE_DATA=True

TEST_MSSQL_HOST=<host>
TEST_MSSQL_NAME=djangoproject
TEST_MSSQL_USERNAME=<username>
TEST_MSSQL_PASSWORD=<password>
USE_MSSQL_FAKE_DATA=True
```

&nbsp;

---

&nbsp;

## Django command

&nbsp;

### **Check if everything was correct**

&nbsp;

```shell
python manage.py check
```

&nbsp;

### **Migrate**

&nbsp;

django has some default migrations that we need to migrate, so run command below

&nbsp;

migrate to database

```shell
python manage.py migrate
```

&nbsp;

(optional)
if we create some apps, we need to create migrations for apps

&nbsp;

create migrations

```shell
python manage.py makemigrations
```

&nbsp;

migrate for specify app

```shell
python manage.py migrate app_name
```

&nbsp;

migrate for specify app migrations number

```shell
python manage.py migrate app_name 0001
```

&nbsp;

revert migrate

```shell
python manage.py migrate app_name zero
```

&nbsp;

### **Shell**

```shell
python manage.py shell
```

&nbsp;

### Create superuser
The sample views in `sqlserver/views.py` has a decorator of `login_required`, meaning you will need to login to see the page. Therefore, you will need to create an user. Yod could run `python manage.py createsuperuser` and follow the instructions to create a superuser to test the functionality of the app.

### **Run server**

```shell
python manage.py runserver
```

&nbsp;

run server for specify settings file

```shell
python manage.py runserver --settings=django_tutorial.settings_test
```

&nbsp;

run server for specify settings ip and port

```shell
python manage.py runserver 0.0.0.0:8001
```

&nbsp;

### **Testing**

&nbsp;

when testing, we need to specify settings file for testing

```shell
python manage.py test --settings=django_tutorial.settings_test
```
