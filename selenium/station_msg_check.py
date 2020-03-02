import json

import pymysql

my = pymysql.connect(host="127.0.0.1", user='debian-sys-maint', password="PmOL3zdw6WErzZ7a",
                     db='gd_map_charging_station', port=3306, charset='utf8mb4')
mycur = my.cursor()

sql = """ select msg,ids,location from charging_station where brand_desc is null order by  ids desc """
inst = """UPDATE charging_station SET brand_desc = %s  WHERE ids = %s;"""


def select_sql():
    mycur.execute(sql)
    res_list = mycur.fetchall()
    return res_list


if __name__ == '__main__':
    lis = select_sql()
    for ls in lis:
        json_str_msg = ls[0]
        msg = json.loads(json_str_msg)
        if '"status":"1"' in ls[0] and 'brand_desc' in ls[0]:
            brand_desc = msg.get('data').get('charging').get('brand_desc')
            if brand_desc is not None:
                print brand_desc
                params = (brand_desc, ls[1])
                mycur.execute(inst, params)
                my.commit()
