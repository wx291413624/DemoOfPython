# coding=utf-8
from map import gcj02tobd09
from map.test import mycur, my, find1, find, sql, sql_4, sql_2, find_sql
from mysql import geodistance

inst = """INSERT INTO TEST.excel_map_baidu_gas (dis, c_id, g_id, distance) VALUES (%s, %s, %s, %s);"""

if __name__ == '__main__':
    ss2 = find_sql(sql_2, 0, 0, 0)  # 爬
    ss = find_sql(sql_4, 0, 10000, 1)  # gaode
    for s in ss:
        vs = s[4].split(',')
        for s2 in ss2:
            ddd = geodistance(vs[0], vs[1], s2[4], s2[5])
            print ddd
            if ddd <= 500:
                print '------insert'
                params = (500, s2[0], s[0], ddd)
                print params
                mycur.execute(inst, params)
                my.commit()
