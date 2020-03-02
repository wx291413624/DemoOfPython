# coding=utf-8
import pymysql
import xlrd
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

mys = pymysql.connect(host="127.0.0.1", user='debian-sys-maint', password="PmOL3zdw6WErzZ7a",
                      db='gd_map_charging_station', port=3306,
                      charset='utf8')
sql = """INSERT INTO gd_map_charging_station.excel_charging_station (
city_name,provider_name,station_name,station_address,partners_name,
cooperation,cooperation_price,business_progress)
   VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""


def inser(params):
    mycur = mys.cursor()
    mycur.execute(sql, params)
    mys.commit()


def read_excel():
    workbook = xlrd.open_workbook(r'./12.xlsx')
    shee = workbook.sheet_names()
    for sh in shee:
        if sh == '信息统计表' or sh == '勿删':
            continue
        table = workbook.sheet_by_name(sh)
        for ex in range(3, table.nrows):
            print sh, str(table.row_values(ex)[1]), str(table.row_values(ex)[2]), str(table.row_values(ex)[3])
            print str(table.row_values(ex)[4]), str(table.row_values(ex)[5]), str(table.row_values(ex)[6])
            params = (sh,
                      str(table.row_values(ex)[1]), str(table.row_values(ex)[2]), str(table.row_values(ex)[3]),
                      str(table.row_values(ex)[4]), str(table.row_values(ex)[5]), str(table.row_values(ex)[6]),
                      str(table.row_values(ex)[7])
                      )
            print params
            inser(params)


if __name__ == '__main__':
    read_excel()
