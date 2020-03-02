# coding=utf-8
import json

import pymysql
import sys

reload(sys)
sys.setdefaultencoding('utf8')
my = pymysql.connect(host="127.0.0.1", user='debian-sys-maint', password="PmOL3zdw6WErzZ7a",
                     db='gd_map_charging_station', port=3306, charset='utf8mb4')
mycur = my.cursor()

sql = """ select id,name from all_brand where tts=1 order by id """
update = """UPDATE all_brand SET name = %s  WHERE id = %s;"""
insert = """INSERT INTO gd_map_charging_station.all_brand (num, name, tts) VALUES (%s, %s, 1);"""


def select_sql():
    mycur.execute(sql)
    res_list = mycur.fetchall()
    return res_list


if __name__ == '__main__':
    lis = select_sql()
    for ls in lis:
        id = ls[0]
        name = str(ls[1])
        if '、' in name:
            nna = name.split('、')
            print nna
            # name = name.replace('微信小程序', '')
            # print name
            # params = (name, id)
            # mycur.execute(update, params)
            # my.commit()
