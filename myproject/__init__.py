import pymysql

# Patch pymysql to work with Django's version check
pymysql.install_as_MySQLdb()
pymysql.version_info = (2, 2, 1, "final", 0)
pymysql.__version__ = "2.2.1"