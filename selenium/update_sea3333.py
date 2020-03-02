import json

import pymysql

my = pymysql.connect(host="47.95.235.183", user='root', password="Kiretyo1521",
                     db='gd_map_charging_station', port=3306, charset='utf8mb4')
mycur = my.cursor()

sql = """ select ids,name from charging_station order by ids desc limit 22000,2000"""
inst = """UPDATE sea_localtion SET station_name = %s  WHERE ids = %s;"""


def select_sql():
    mycur.execute(sql)
    res_list = mycur.fetchall()
    return res_list


if __name__ == '__main__':
    lis = select_sql()
    for ls in lis:
        ids = ls[0]
        name = ls[1]
        if name is None:
            continue
        params = (name, ids)
        mycur.execute(inst, params)
        my.commit()
