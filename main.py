from threading import Thread
import pymysql
import json


def init_database():
    """
    初始化数据库，如果存在，不做改动

    :return:
    """
    try:
        db = pymysql.connect(host='localhost',
                             user=db_user,
                             password=db_pwd,
                             database='njg_plan')
    except pymysql.err.OperationalError:
        print('数据库不存在，创建数据库和表单')
        db = pymysql.connect(host='localhost',
                             user=db_user,
                             password=db_pwd)
        cursor = db.cursor()
        cursor.execute('create database njg_plan')
        cursor.execute('use njg_plan')
        cursor.execute(f'CREATE TABLE yhdm (\
                        showid varchar(10) NOT NULL,\
                        name varchar(50) NOT NULL,\
                        current_episode int(11) NOT NULL,\
                        date date DEFAULT NULL,\
                        user_email varchar(3000) DEFAULT "{owner_mail}",\
                        PRIMARY KEY (showid,name)\
                        ) ENGINE=InnoDB DEFAULT CHARSET=utf8')
        cursor.execute(f'CREATE TABLE yhdmp (\
                                showpid varchar(10) NOT NULL,\
                                name varchar(50) NOT NULL,\
                                current_episode int(11) NOT NULL,\
                                date date DEFAULT NULL,\
                                user_email varchar(3000) DEFAULT "{owner_mail}",\
                                PRIMARY KEY (showpid,name)\
                                ) ENGINE=InnoDB DEFAULT CHARSET=utf8')
        db.commit()
        db.close()


def init():
    """
    开始所有任务\n
    包括创建或检测数据库及表单、启动死循环定时检测番剧更新

    :return:
    """
    init_database()
    pass


def check_YH():
    """
    检测樱花动漫

    :return:
    """
    pass


def check_BR():
    """
    检测哔哩哔哩

    :return:
    """
    pass


if __name__ == '__main__':
    f = open('./resource/config.json', 'r', encoding='utf-8')
    config_data = json.loads(f.read())
    f.close()
    owner_mail = config_data['owner_mail']
    smtp_host = config_data['smtp_host']
    smtp_user = config_data['smtp_user']
    smtp_pass = config_data['smtp_pass']
    db_user = config_data['db_user']
    db_pwd = config_data['db_pwd']
    # init()
    pass
