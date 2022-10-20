import os

class Config():
    Root=os.path.dirname(os.path.abspath(__file__))
    LOG_NAME=os.path.join(Root, 'logs', 'pity.log')
    JSON_AS_ASCII=False

    MYSQL_HOST="127.0.0.1"
    MYSQL_PORT=3306
    MYSQL_USER="root"
    MYSQL_PASSWD="123456"
    MYSQL_DBNAME="pity"

    SQLALCHEMY_DATABASE_URI='mysql+pymysql://{}:{}@{}:{}/{}'.format(
        MYSQL_USER,MYSQL_PASSWD,MYSQL_HOST,MYSQL_PORT,MYSQL_DBNAME)

    SQLALCHEMY_TRACK_MODIFICATIONS=False

