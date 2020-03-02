# coding=utf-8
# 第一电动
import pymysql
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf8')
my = pymysql.connect(host="127.0.0.1", user='debian-sys-maint', password="PmOL3zdw6WErzZ7a", db='TEST', port=3306,
                     charset='utf8')
mycur = my.cursor()
# 72.414032,53.988665        137.761231,53.988665
# 72.414032,18.25638          137.761231,18.25638
sql = 'INSERT INTO TEST.poi_map (poi_id, poi_jing, poi_wei) VALUES (%s, %s, %s);'


def getLngList():
    res = requests.get(
        "https://cdz.evcharge.cc/zhannew/basic/web/index.php/tengshi/index?minLng=72.414032&minLat=18.25638&maxLng=137.761231&maxLat=53.988665&eletype=&payway=&supplier=")
    # rtnCode rtnMsg
    # id: "10005111129225"
    # poi_jing: "117.9534123779890000"
    # poi_wei: "41.7964895799870000"
    json = res.json()
    rtnMsg = json.get('rtnMsg')
    for msg in rtnMsg:
        id = msg['id']
        poi_wei = msg['poi_wei']
        poi_jing = msg['poi_jing']
        params = (id, poi_jing, poi_wei)
        print params
        mycur.execute(sql, params)
        my.commit()


msgsql = """INSERT INTO TEST.poi_map_msg (acNum, acableNum, belong_attribute, charge_cost, charge_cost_way2, 
                                                               dcNum, dcableNum, fast_num, fen_info, id, 
                                                               park_location, poi_jing, poi_wei, remarks, serve_cost, 
                                                               slow_num, start_level, stop_cost, supplier, telephone, 
                                                               work_close, work_open, zhan_address, zhan_id, zhan_name, json_text)VALUES (
 %s, %s, %s, %s, %s,
 %s, %s, %s, %s, %s, 
 %s, %s, %s, %s, %s, 
 %s, %s, %s, %s, %s, 
 %s, %s, %s, %s, %s, %s);"""


def get_msg(id):
    print id
    res = requests.get('https://cdz.evcharge.cc/zhannew/basic/web/index.php/tengshi/zhan-detail?zhan_id=' + id)
    json = res.json()
    info = json.get('info')
    if info:
        params = (
            str(info['acNum'] or ''), str(info['acableNum']), str(info['belong_attribute']), str(info['charge_cost']),
            str(info['charge_cost_way2']),
            str(info['dcNum']), str(info['dcableNum']), str(info['fast_num']), str(info['fen_info']), str(info['id']),
            str(info['park_location']), str(info['poi_jing']), str(info['poi_wei']), str(info['remarks']),
            str(info['serve_cost']),
            str(info['slow_num']), str(info['start_level']), str(info['stop_cost']), str(info['supplier']),
            str(info['telephone']),
            str(info['work_close']), str(info['work_open']), str(info['zhan_address']), str(info['zhan_id']),
            str(info['zhan_name']), str(json))
        mycur.execute(msgsql, params)
        my.commit()


def sel_all():
    sql = 'select * from poi_map where poi_id not in (select id from poi_map_msg) limit 0,1000'
    mycur.execute(sql)
    res_list = mycur.fetchall()
    return res_list


if __name__ == '__main__':
    res_list = sel_all()
    for re in res_list:
        get_msg(re[1])
