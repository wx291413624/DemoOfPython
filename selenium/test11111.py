import json

import pymysql

my = pymysql.connect(host="127.0.0.1", user='debian-sys-maint', password="PmOL3zdw6WErzZ7a",
                     db='gd_map_charging_station', port=3306, charset='utf8mb4')
mycur = my.cursor()

my1 = pymysql.connect(host="47.95.235.183", user='root', password="Kiretyo1521",
                      db='gd_map_charging_station', port=3306, charset='utf8mb4')
mycur1 = my1.cursor()

sql = """ select ids,brand_desc from charging_station order by ids desc limit 18000,2000 """
inst = """UPDATE sea_localtion SET brand_desc = %s  WHERE ids = %s;"""


def select_sql():
    mycur.execute(sql)
    res_list = mycur.fetchall()
    return res_list


if __name__ == '__main__':
    lis = select_sql()
    for ls in lis:
        ids = ls[0]
        brand_desc = ls[1]
        if brand_desc is None:
            continue
        params = (brand_desc, ids)
        mycur1.execute(inst, params)
        my1.commit()
