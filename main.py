from threading import Thread
import json
from mail import sendmail
from YH_HIDERUA import get_YH_data
import time
import sqlite3
from BLBL import get_BLBL_data
from BLBL import get_info


def get_msg(name, url, title=""):
    return r"""
    <div>
    <includetail>
        <style>
            body,
            table,
            td,
            a {
                -webkit-text-size-adjust: 100%;
                -ms-text-size-adjust: 100%;
            }

            table,
            td {
                mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
            }

            img {
                -ms-interpolation-mode: bicubic;
            }

            .hidden {
                display: none !important;
                visibility: hidden !important;
            }

            /* iOS BLUE LINKS */
            a[x-apple-data-detectors] {
                color: inherit !important;
                text-decoration: none !important;
                font-size: inherit !important;
                font-family: inherit !important;
                font-weight: inherit !important;
                line-height: inherit !important;
            }

            /* ANDROID MARGIN HACK */
            body {
                margin: 0 !important;
            }

            div[style*="margin: 16px 0"] {
                margin: 0 !important;
            }

            @media only screen and (max-width: 639px) {

                body,
                #body {
                    min-width: 320px !important;
                }

                table.wrapper {
                    width: 100% !important;
                    min-width: 320px !important;
                }
            }
        </style>
        <style>
            body {
                -webkit-text-size-adjust: 100%;
                -ms-text-size-adjust: 100%;
            }

            img {
                -ms-interpolation-mode: bicubic;
            }

            body {
                margin: 0 !important;
            }
        </style>


        <table border="0" cellpadding="0" cellspacing="0" id="body"
            style="text-align: center; min-width: 640px; width: 100%; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; mso-table-lspace: 0pt; mso-table-rspace: 0pt; margin: 0; padding: 0;"
            bgcolor="#fafafa">
            <tbody>
                <tr class="line">
                    <td style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; height: 4px; font-size: 4px; line-height: 4px; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                        bgcolor="#6b4fbb">&nbsp;
                    </td>
                </tr>
                <tr class="header">
                    <td
                        style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; font-size: 13px; line-height: 1.6; color: #5c5c5c; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; mso-table-lspace: 0pt; mso-table-rspace: 0pt; padding: 25px 0;">
                        <img src="cid:image1"
                            height="200"  style="-ms-interpolation-mode: bicubic;">
                    </td>
                </tr>
                <tr>
                    <td>
                    """ + \
           title + """
                    </td>
                </tr>
                <tr>
                    <td
                        style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                        <table border="0" cellpadding="0" cellspacing="0" class="wrapper"
                            style="width: 640px; border-collapse: separate; border-spacing: 0; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; mso-table-lspace: 0pt; mso-table-rspace: 0pt; margin: 0 auto;">
                            <tbody>
                                <tr>
                                    <td style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; border-radius: 3px; overflow: hidden; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; mso-table-lspace: 0pt; mso-table-rspace: 0pt; padding: 18px 25px; border: 1px solid #ededed;"
                                        align="left" bgcolor="#ffffff">
                                        <table border="0" cellpadding="0" cellspacing="0" class="content"
                                            style="width: 100%; border-collapse: separate; border-spacing: 0; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                                            <tbody>
                                                <tr>
                                                    <td style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; color: #333333; font-size: 15px; font-weight: 400; line-height: 1.4; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; mso-table-lspace: 0pt; mso-table-rspace: 0pt; padding: 15px 5px;"
                                                        align="center">
                                                        <h1 style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; color: #333333; font-size: 18px; font-weight: 400; line-height: 1.4; margin: 0; padding: 0;"
                                                            align="center">
                                                            尊敬的NJG user 您好！
                                                        </h1>
                                                        <p>
                                                            您订阅的番剧《""" + name + """》更新了
                                                        </p>
                                                        <div id="cta">
                                                            <a href=""
                                                                style="-webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%;">点击此处直达</a>
                                                        </div>
                                                        <p>
                                                            或复制此链接在浏览器打开<a href=""
                                                                style="-webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%;">""" + url + """</a>
                                                        </p>

                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
                <tr class="footer">
                    <td
                        style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; font-size: 13px; line-height: 1.6; color: #5c5c5c; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; mso-table-lspace: 0pt; mso-table-rspace: 0pt; padding: 25px 0;">
                        <div style="color: red;">

                            <p>请确认这封邮件没有问题后再点击链接，或自己在浏览器搜索</p>
                            <p>请确认这封邮件没有问题后再点击链接，或自己在浏览器搜索</p>
                            <p>请确认这封邮件没有问题后再点击链接，或自己在浏览器搜索</p>
                        </div>
                    </td>
                </tr>

            </tbody>
        </table>
    </includetail>
</div>
    """


def init_database():
    """
    初始化数据库，如果存在，不做改动

    """
    # try:
    #     db = pymysql.connect(host='localhost',
    #                          user=db_user,
    #                          password=db_pwd,
    #                          database='njg_plan')
    #     db.close()
    # except pymysql.err.OperationalError:
    #     print('数据库不存在，创建数据库和表单')
    #     db = pymysql.connect(host='localhost',
    #                          user=db_user,
    #                          password=db_pwd)
    #     cursor = db.cursor()
    #     cursor.execute('create database njg_plan')
    #     cursor.execute('use njg_plan')
    #     cursor.execute(f'CREATE TABLE yhdm (\
    #                     showid varchar(10) NOT NULL,\
    #                     name varchar(50) NOT NULL,\
    #                     current_episode int(11) NOT NULL,\
    #                     date date DEFAULT NULL,\
    #                     user_email varchar(3000) DEFAULT "{owner_mail}",\
    #                     PRIMARY KEY (showid,name)\
    #                     ) ENGINE=InnoDB DEFAULT CHARSET=utf8')
    #     cursor.execute(f'CREATE TABLE yhdmp (\
    #                             showpid varchar(10) NOT NULL,\
    #                             name varchar(50) NOT NULL,\
    #                             current_episode int(11) NOT NULL,\
    #                             date date DEFAULT NULL,\
    #                             user_email varchar(3000) DEFAULT "{owner_mail}",\
    #                             PRIMARY KEY (showpid,name)\
    #                             ) ENGINE=InnoDB DEFAULT CHARSET=utf8')
    #
    #     db.commit()
    #     db.close()

    # 初始化数据库及表单
    print('开始检测数据库')
    db = sqlite3.connect('./resource/NJG.db')
    try:
        db.execute('select * from yhdm')
    except sqlite3.OperationalError:
        cursor = db.cursor()
        cursor.execute(f'CREATE TABLE yhdm (\
                             showid varchar(10) NOT NULL,\
                             name varchar(50) NOT NULL,\
                             current_episode int(5) NOT NULL,\
                             date date DEFAULT NULL,\
                             user_email varchar(3000) DEFAULT "{owner_mail}",\
                             PRIMARY KEY (showid,name)\
                             )')
        print('创建表单yhdm成功')
    try:
        db.execute('select * from yhdmp')
    except sqlite3.OperationalError:
        cursor = db.cursor()
        cursor.execute(f'CREATE TABLE yhdmp (\
                                     showpid varchar(10) NOT NULL,\
                                     name varchar(50) NOT NULL,\
                                     current_episode int(5) NOT NULL,\
                                     date date DEFAULT NULL,\
                                     user_email varchar(3000) DEFAULT "{owner_mail}",\
                                     PRIMARY KEY (showpid,name)\
                                     )')
        print('创建表单yhhdmp成功')
    try:
        db.execute('select * from blbl')
    except sqlite3.OperationalError:
        cursor = db.cursor()
        cursor.execute(f'CREATE TABLE blbl (\
                                     mid varchar(20) NOT NULL,\
                                     name varchar(50) NOT NULL,\
                                     current_episode int(5) NOT NULL,\
                                     date date DEFAULT NULL,\
                                     user_email varchar(3000) DEFAULT "{owner_mail}",\
                                     PRIMARY KEY (mid,name)\
                                     )')
        print('创建表单blbl成功')
    db.commit()
    db.close()
    print('数据库检测完成')


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
    print('开始执行定时任务')
    while True:
        try:
            check_YH()
            check_BR()
            check_YHP()
        except (TypeError, TimeoutError, NameError, KeyError, IndexError) as err:
            sendmail('错误通知', f'发送了一个错误{err}', [owner_mail], smtp_host, smtp_user, smtp_pass)
        print('本轮任务执行完毕，开始休眠5分钟')
        time.sleep(300)
        print('休眠5分钟结束，即将开始下一轮任务')


def check_YH():
    """
    检测樱花动漫 http://www.yinghuacd.com/

    """
    db = sqlite3.connect('./resource/NJG.db')
    curosr = db.cursor()
    # 获取所有在表的数据
    sql = 'select * from yhdm'
    try:
        curosr.execute(sql)
        results = curosr.fetchall()
        for row in results:
            print('开始检测樱花动漫:', row)
            showid = row[0]
            name = row[1]
            current_episode = row[2]
            # update_date = row[3]
            user_emails = row[4]
            result = get_YH_data(showid)
            if result['current_episode'] > current_episode:
                print('检测到更新，开始发送邮件')
                # 有更新，发送请求
                sendmail(f'番剧《{name}》更新提醒', get_msg(name, result['url']), user_emails.split(","), smtp_host, smtp_user,
                         smtp_pass)
                # 更新表单
                update_sql = f'update yhdm set current_episode = {result["current_episode"]},date = date("now") where showid = {showid}'
                # 执行命令
                curosr.execute(update_sql)
            else:
                print('无更新')
            # 提交
            db.commit()
    except Exception as err:
        print(err)
        db.rollback()
    db.close()


def check_BR():
    """
    检测哔哩哔哩

    """
    db = sqlite3.connect('./resource/NJG.db')
    curosr = db.cursor()
    # 获取所有在表的数据
    sql = 'select * from blbl'
    try:
        curosr.execute(sql)
        results = curosr.fetchall()
        for row in results:
            print('开始检测哔哩哔哩:', row)
            mid: str = row[0]
            name: str = row[1]
            current_episode: int = row[2]
            # update_date = row[3]
            user_emails: str = row[4]
            result = get_BLBL_data(mid)
            if int(result['current_episode']) > current_episode:
                info = get_info(result['season_id'])
                print('检测到更新，开始发送邮件')
                # 有更新，发送请求
                sendmail(f'番剧《{name}》更新提醒', get_msg(name, result['url'], info['title']), user_emails.split(","),
                         smtp_host, smtp_user,
                         smtp_pass, pic=info['cover'])
                # 更新表单
                update_sql = f'update blbl set current_episode = {int(result["current_episode"])},date = date("now") where mid = {mid}'
                # 执行命令
                curosr.execute(update_sql)
            else:
                print('无更新')
            # 提交
            db.commit()
    except Exception as err:
        print(err)
        db.rollback()
    db.close()
    pass


def check_YHP():
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
    init()
    pass
