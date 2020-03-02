# coding=utf-8
# 第一电动
from math import ceil

import pymysql
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf8')
my = pymysql.connect(host='127.0.0.1', user='debian-sys-maint', password='PmOL3zdw6WErzZ7a', db='TEST', port=3306,
                     charset='utf8')
mycur = my.cursor()


# 72.414032,53.988665        137.761231,53.988665
# 72.414032,18.25638          137.761231,18.25638


def getLngList():
    headers = {
        'accept': '*/*',
        'connection': 'Keep-Alive',
        'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)'}
    res = requests.get(
        'https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=16&city=110000&geoobj=116.47142%7C39.905188%7C116.483241%7C39.91608&keywords=%E5%85%85%E7%94%B5%E6%A1%A9'
        , headers=headers)
    json = res.json()
    print json


if __name__ == '__main__':
    # getLngList()
    s = ceil(float(30) / float(10))
    print s
    print "---------"
    s = s + 1
    print s
    for i in range(2, int(s)):
        print i
