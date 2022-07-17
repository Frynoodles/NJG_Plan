from threading import Thread
import pymysql
import json
from MAIL_HIDERUA import send_mail
from YH_HIDERUA import get_YH_data
import time


def init_database():
    """
    初始化数据库，如果存在，不做改动

    """
    try:
        db = pymysql.connect(host='localhost',
                             user=db_user,
                             password=db_pwd,
                             database='njg_plan')
        db.close()
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
    初始化数据库，并开启定时任务

    """
    init_database()
    t = Thread(target=time_task())
    t.start()


def time_task():
    """
    定时任务，死循环执行几个定时任务

    """
    while True:
        try:
            db = pymysql.connect(host='localhost',
                                 user=db_user,
                                 password=db_pwd,
                                 database='njg_plan')
            check_YH(db)
            check_BR(db)
            check_YHP(db)
            db.close()
        except (TypeError, TimeoutError, NameError, KeyError, IndexError) as err:
            send_mail('错误通知', f'发送了一个错误{err}', [owner_mail], smtp_host, smtp_user, smtp_pass)
        time.sleep(300)


def check_YH(db: pymysql.connect):
    """
    检测樱花动漫 http://www.yinghuacd.com/

    :param db: 数据库连接
    """
    curosr = db.cursor()
    # 获取所有在表的数据
    sql = 'select * from yhdm'
    try:
        curosr.execute(sql)
        results = curosr.fetchall()
        for row in results:
            showid: str = row[0]
            name: str = row[1]
            current_episode: int = row[2]
            update_date = row[3]
            user_emails: str = row[4]
            result = get_YH_data(showid)
            if result['current_episode'] > current_episode:
                # 有更新，发送请求
                send_mail(f'番剧更新提醒《{name}》',
                          f'<div>\
                            <div><span>您订阅的番剧《{name}》更新了</span></div>\
                            <div><a href=\"{result["url"]}\">直达链接{result["url"]}</a></div>\
                            <div>请确认链接无误后再点击，或者费事点自己去搜</div>\
                            <div>请确认链接无误后再点击，或者费事点自己去搜</div>\
                        </div>',
                          user_emails.split(","), smtp_host, smtp_user, smtp_pass)
                # 更新表单
                update_sql = f'update yhdm set current_episode = {current_episode + 1} where showid = {showid}'
                # 执行命令
                curosr.execute(update_sql)
            # 提交
            db.commit()
    except:
        print("Error: unable to fetch data")
        db.rollback()


def check_BR(db: pymysql.connect):
    """
    检测哔哩哔哩

    """
    pass


def check_YHP(db: pymysql.connect):
    """
    检测樱花动漫P https://www.yhdmp.cc/

    """
    pass


if __name__ == '__main__':
    f = open('./resource/config.json', 'r', encoding='utf-8')
    config_data = json.loads(f.read())
    f.close()
    owner_mail: str = config_data['owner_mail']
    smtp_host: str = config_data['smtp_host']
    smtp_user: str = config_data['smtp_user']
    smtp_pass: str = config_data['smtp_pass']
    db_user: str = config_data['db_user']
    db_pwd: str = config_data['db_pwd']
    # init()
    pass
