from map.test import mycur, my

sq3 = 'select c_id from gaode_gas_info where c_id is not null and tel is  null '


def find_sssql(sql, page, num):
    sql += "limit " + str(page) + " , " + str(num)
    mycur.execute(sql)
    res_list = mycur.fetchall()
    return res_list


def find_sql(sql):
    mycur.execute(sql)
    res_list = mycur.fetchall()
    return res_list


if __name__ == '__main__':
    list = find_sssql(sq3, 0, 10000)
    a = 1
    for ls in list:
        print a
        id = ls[0]
        sq1 = 'select g_id from excel_map_baidu_gas where c_id=' + str(id) + ' order by distance;'
        list = find_sql(sq1)
        sq2 = 'select tel,pname,cityname,adname,gas_type from gas_info where id=' + str(list[0][0]) + ';'
        list = find_sql(sq2)
        sql4 = 'UPDATE TEST.gaode_gas_info SET ' \
               'tel = %s, pname = %s, cityname =%s, adname = %s, gas_type = %s WHERE c_id = ' + str(id) + ';'
        params = (list[0][0], list[0][1], list[0][2], list[0][3], list[0][4])
        mycur.execute(sql4, params)
        my.commit()
        a += 1
