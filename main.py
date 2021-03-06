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
                                                            ?????????NJG user ?????????
                                                        </h1>
                                                        <p>
                                                            ?????????????????????""" + name + """????????????
                                                        </p>
                                                        <div id="cta">
                                                            <a href=""
                                                                style="-webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%;">??????????????????</a>
                                                        </div>
                                                        <p>
                                                            ????????????????????????????????????<a href=""
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

                            <p>?????????????????????????????????????????????????????????????????????????????????</p>
                            <p>?????????????????????????????????????????????????????????????????????????????????</p>
                            <p>?????????????????????????????????????????????????????????????????????????????????</p>
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
    ????????????????????????????????????????????????

    """
    # try:
    #     db = pymysql.connect(host='localhost',
    #                          user=db_user,
    #                          password=db_pwd,
    #                          database='njg_plan')
    #     db.close()
    # except pymysql.err.OperationalError:
    #     print('?????????????????????????????????????????????')
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

    # ???????????????????????????
    print('?????????????????????')
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
        print('????????????yhdm??????')
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
        print('????????????yhhdmp??????')
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
        print('????????????blbl??????')
    db.commit()
    db.close()
    print('?????????????????????')


def init():
    """
    ??????????????????????????????????????????

    """

    init_database()
    t = Thread(target=time_task())
    t.start()


def time_task():
    """
    ????????????????????????????????????????????????

    """
    print('????????????????????????')
    while True:
        try:
            check_YH()
            check_BR()
            check_YHP()
        except (TypeError, TimeoutError, NameError, KeyError, IndexError) as err:
            sendmail('????????????', f'?????????????????????{err}', [owner_mail], smtp_host, smtp_user, smtp_pass)
        print('???????????????????????????????????????5??????')
        time.sleep(300)
        print('??????5??????????????????????????????????????????')


def check_YH():
    """
    ?????????????????? http://www.yinghuacd.com/

    """
    db = sqlite3.connect('./resource/NJG.db')
    cursor = db.cursor()
    # ???????????????????????????
    sql = 'select * from yhdm'
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print('????????????????????????:', row)
            showid = row[0]
            name = row[1]
            current_episode = row[2]
            # update_date = row[3]
            user_emails = row[4]
            result = get_YH_data(showid)
            if result['current_episode'] > current_episode:
                print('????????????????????????????????????')
                # ????????????????????????
                sendmail(f'?????????{name}???????????????', get_msg(name, result['url']), user_emails.split(","), smtp_host, smtp_user,
                         smtp_pass)
                # ????????????
                update_sql = f'update yhdm set current_episode = {result["current_episode"]},date = date("now") where showid = {showid}'
                # ????????????
                cursor.execute(update_sql)
            else:
                print('?????????')
            # ??????
            db.commit()
    except Exception as err:
        print(err)
        db.rollback()
    db.close()


def check_BR():
    """
    ??????????????????

    """
    db = sqlite3.connect('./resource/NJG.db')
    cursor = db.cursor()
    # ???????????????????????????
    sql = 'select * from blbl'
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print('????????????????????????:', row)
            mid: str = row[0]
            name: str = row[1]
            current_episode: int = row[2]
            # update_date = row[3]
            user_emails: str = row[4]
            result = get_BLBL_data(mid)
            if int(result['current_episode']) > current_episode:
                info = get_info(result['season_id'])
                print('????????????????????????????????????')
                # ????????????????????????
                sendmail(f'?????????{name}???????????????', get_msg(name, result['url'], info['title']), user_emails.split(","),
                         smtp_host, smtp_user,
                         smtp_pass, pic=info['cover'])
                # ????????????
                update_sql = f'update blbl set current_episode = {int(result["current_episode"])},date = date("now") where mid = {mid}'
                # ????????????
                cursor.execute(update_sql)
            else:
                print('?????????')
            # ??????
            db.commit()
    except Exception as err:
        print(err)
        db.rollback()
    db.close()
    pass


def check_YHP():
    """
    ??????????????????P https://www.yhdmp.cc/

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
    init()
    pass
