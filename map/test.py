# coding=utf-8
import pymysql
from math import radians, cos, sin, asin, sqrt
from geopy.distance import geodesic
import sys

from map import bd09togcj02

reload(sys)
sys.setdefaultencoding('utf8')

my = pymysql.connect(host="127.0.0.1", user='debian-sys-maint', password="PmOL3zdw6WErzZ7a", db='TEST', port=3306,
                     charset='utf8')
mycur = my.cursor()
ins = "INSERT INTO TEST.CUser_GCJ (id, gid, address, baidux, baiduy, activity, payname, fwlsmc, zzyqzl, cname)" \
      " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

sql = ''


def find1(page, num):
    sqlss = "SELECT * FROM TEST.excel_gas order by  id DESC limit " + str(
        page) + " , " + str(num)
    mycur.execute(sqlss)
    res_list = mycur.fetchall()
    return res_list


def find():
    sqlss = "SELECT * FROM CUser  order by  id DESC"
    mycur.execute(sqlss)
    res_list = mycur.fetchall()
    return res_list


if __name__ == '__main__':
    ss = find()
    for s in ss:
        lnglat = bd09togcj02(float(s[3]), float(s[4]))
        params = (s[0], s[1], s[2], lnglat[0], lnglat[1], s[5], s[6], s[7], s[8], s[9])
        mycur.execute(ins, params)
        my.commit()

# 2
sql_2 = "select * from TEST.CUser_GCJ where id not in (select cc from (select c_id cc from TEST.excel_map_baidu_gas group by c_id) a)  "
# 4
sql_4 = "select * from TEST.gas_info where id not in (select cc from (select g_id cc from TEST.excel_map_baidu_gas group by g_id) a) "


def find_sql(sql, page, num, type):
    if type == 1:
        sql += "limit " + str(page) + " , " + str(num)
    mycur.execute(sql)
    res_list = mycur.fetchall()
    return res_list
