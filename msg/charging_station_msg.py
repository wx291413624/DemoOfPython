# coding=utf-8
from math import ceil

import pymysql
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf8')
my = pymysql.connect(host="127.0.0.1", user='debian-sys-maint', password="PmOL3zdw6WErzZ7a",
                     db='gd_map_charging_station', port=3306, charset='utf8')
mycur = my.cursor()
selet_sql = """ select adcode,id from adcode where city_code in (select city_code from num_of_city) and adcode not in (select adcode from num_of_city) and city_name not like '%市辖区%' and   tty is null """
sql = """INSERT INTO gd_map_charging_station.kuaiyun_charging_station 
(ids, parent, childtype, name, type,
 typecode, biz_type, address, location, tel,
  distance, biz_ext, pname, cityname, adname, 
  importance, shopid, shopinfo, poiweight, photos) 
VALUES
 (%s, %s, %s, %s, %s, 
 %s, %s, %s, %s, %s, 
 %s, %s, %s, %s, %s, 
 %s, %s, %s, %s, %s);
"""
update_sql = """UPDATE gd_map_charging_station.adcode SET tty = 32 ,pois_len=%s WHERE id = %s;"""


def insertS(sjon):
    for json in sjon:
        print json
        params = (str(json['id']), str(json['parent']), str(json['childtype']), str(json['name']), str(json['type']),
                  str(json['typecode']), str(json['biz_type']), str(json['address']), str(json['location']),
                  str(json['tel']),
                  str(json['distance']), str(json['biz_ext']), str(json['pname']), str(json['cityname']),
                  str(json['adname']),
                  str(json['importance']), str(json['shopid']), str(json['shopinfo']), str(json['poiweight']),
                  str(json['photos']))
        mycur.execute(sql, params)
        my.commit()


def updateS(id, num_of_sum):
    params = (num_of_sum, id)
    mycur.execute(update_sql, params)
    my.commit()


def find():
    mycur.execute(selet_sql)
    res_list = mycur.fetchall()
    return res_list


def get_url(city, page):
    url = """https://restapi.amap.com/v3/place/text?keywords=%e5%bf%ab%e8%bf%90&key=d6911a255e50c5196b7f8f271eefaded&city=""" + str(
        city) + """&offset=1000&citylimit=true&page=""" + str(page)
    res = requests.get(url)
    json = res.json()
    return json


if __name__ == '__main__':
    relis = find()
    for ss in relis:
        id = ss[1]
        city = ss[0]
        print city
        json = get_url(city, 1)
        # num 1  insert sql
        count = json['count']
        pois = json['pois']
        insertS(pois)
        pois_len = len(pois)
        if pois_len == 0:
            continue
        s = ceil(float(count) / float(pois_len))
        s = s + 1
        num_of_sum = pois_len
        for i in range(2, int(s)):
            json = get_url(city, i)
            count = json['count']
            pois = json['pois']
            pois_len = len(pois)
            num_of_sum += pois_len
            # num 2  insert sql
            insertS(pois)
        updateS(id, num_of_sum)
