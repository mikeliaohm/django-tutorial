# 
# connector.txt
# ----------------
# by Griffon Development Co., Ltd
#
# Establish MSSQL DB connection through the [sqlalchemy](https://www.sqlalchemy.org/) package

import urllib

from django.conf import settings

from sqlalchemy import create_engine

def sqlalchemy_connector_engine():
    
    db_setting = settings.DATABASES['mssql_db']
    server = db_setting['HOST']
    database = db_setting['NAME']
    username = db_setting['USER']
    password = db_setting['PASSWORD']

    params = params = urllib.parse.quote_plus('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

    return engine

def GET_EMPLOYEE_DATA():

    engine = sqlalchemy_connector_engine()
    connection = engine.connect()
    result = connection.execute('''SELECT * FROM EMPLOYEE''')

    print(result.fetchall())

    connection.close()
