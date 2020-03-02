import pymysql

czbmy = pymysql.connect(host="127.0.0.1", user='debian-sys-maint', password="PmOL3zdw6WErzZ7a", db='TEST', port=3306,
                        charset='utf8')
czbmycur = czbmy.cursor()

my = pymysql.connect(host="127.0.0.1", user='debian-sys-maint', password="PmOL3zdw6WErzZ7a", db='TEST', port=3306,
                     charset='utf8')
mycur = my.cursor()

czb_sql = """
select gas_id,
       gas_name,
       gas_address,
       concat(gas_address_longitude, ',', gas_address_latitude) location,
       gas_phone,
       province_name,
       city_name,
       county_name,
       CASE
         WHEN gas_type = 1 THEN '中国石化'
         WHEN gas_type = 2 THEN '中国石油'
         WHEN gas_type = 3 THEN '壳牌'
         ELSE '其他' END as                                       gas_type,
       (select  GROUP_CONCAT(oil_no) from yfq_fw_oil_price  where gas_id = b.gas_id and status = 1) as oil

from yfq_fw_gas_info b
where gas_name not like '%内测%'
  and gas_status = 1

"""

gao_de_sql = """select * from gaode_gas_info """


def find(sql):
    mycur.execute(sql)
    res_list = mycur.fetchall()
    return res_list


if __name__ == '__main__':
    czb = find(czb_sql)
    gaode = find(gao_de_sql)
