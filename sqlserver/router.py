# 
# router.py
# ----------------
# by Griffon Development Co., Ltd
#
# Specify the settings for DBs when there are multiple databases. 
# https://docs.djangoproject.com/en/3.2/topics/db/multi-db/#automatic-database-routing

class SqlServerRouter:
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to sqlserver_db.
        """
        if model._meta.app_label == 'sqlserver':
            return 'mssql_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to sqlserver_db.
        """
        if model._meta.app_label == 'sqlserver':
            return 'mssql_db'
        return None