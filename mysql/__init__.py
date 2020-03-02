# coding=utf-8
import pymysql
from math import radians, cos, sin, asin, sqrt
from geopy.distance import geodesic
import sys

reload(sys)
sys.setdefaultencoding('utf8')

my = pymysql.connect(host="127.0.0.1", user='debian-sys-maint', password="PmOL3zdw6WErzZ7a", db='TEST', port=3306,
                     charset='utf8')
mycur = my.cursor()
inst = """INSERT INTO TEST.excel_map_gas (dis, c_id, g_id, distance) VALUES (%s, %s, %s, %s);"""


def find(page, num):
    sqlss = "SELECT baidux,baiduy,id FROM CUser  order by  id DESC  limit  " + str(
        page) + " , " + str(num)
    mycur.execute(sqlss)
    res_list = mycur.fetchall()
    return res_list


def find1():
    sqlss = "SELECT n,o,id FROM TEST.excel_gas order by  id DESC "
    mycur.execute(sqlss)
    res_list = mycur.fetchall()
    return res_list


def dista(lat, lng, lat1, lng1):
    dist = geodesic((lat, lng), (lat1, lng1)).m
    return dist


def geodistance(lng1, lat1, lng2, lat2):
    # lng1,lat1,lng2,lat2 = (120.12802999999997,30.28708,115.86572000000001,28.7427)
    lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)])  # 经纬度转换成弧度
    dlon = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    distance = 2 * asin(sqrt(a)) * 6371 * 1000  # 地球平均半径，6371km
    distance = round(distance / 1000, 3)
    return distance * 1000

#
# if __name__ == '__main__':
#     lng1, lat1, lng2, lat2 = (120.12802999999997, 30.28708, 115.86572000000001, 28.7427)
#     ss = geodistance(120.12802999999997, 30.28708, 115.86572000000001, 28.7427) * 1000
#     print ss
#     dist = geodesic((30.28708, 120.12802999999997), (28.7427, 115.86572000000001)).m
#     print dist
