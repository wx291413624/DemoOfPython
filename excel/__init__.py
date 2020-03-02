# coding=utf-8
import pymysql
import xlrd
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


def getMysql():
    my = pymysql.connect(host="127.0.0.1", user='debian-sys-maint', password="PmOL3zdw6WErzZ7a", db='TEST', port=3306,
                         charset='utf8')
    return my


def read_excel():
    workbook = xlrd.open_workbook(r'./123.xlsx')
    sheet2 = workbook.sheet_by_index(1)
    return sheet2


def sqk(da):
    mys = getMysql()
    mycur = mys.cursor()
    sql = "INSERT INTO TEST.excel_gas ( " \
          "b, cc, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, " \
          "aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, ass, att, au, av, aw, ax, ay, az," \
          " ba, bb, bc, bd, be, bf, bg, bh, bi, bj, bk, bl, bm, bn, bo) " \
          "VALUES (" \
          "%s , %s, %s, %s, %s, %s, %s, %s, %s, %s," \
          " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
          " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
          "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
          "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
          "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
          "%s, %s, %s, %s, %s, %s);"
    params = (
        str(da[1]), str(da[2]), str(da[3]), str(da[4]), str(da[5]), str(da[6]), str(da[7]), str(da[8]), str(da[9]),
        str(da[10]), str(da[11]), str(da[12]), str(da[13]), str(da[14]), str(da[15]), str(da[16]), str(da[17]),
        str(da[18]), str(da[19]), str(da[20]), str(da[21]), str(da[22]), str(da[23]), str(da[24]), str(da[25]),
        str(da[26]), str(da[27]), str(da[28]), str(da[29]), str(da[30]), str(da[31]), str(da[32]), str(da[33]),
        str(da[34]), str(da[35]), str(da[36]), str(da[37]), str(da[38]), str(da[39]), str(da[40]), str(da[41]),
        str(da[42]), str(da[43]), str(da[44]), str(da[45]), str(da[46]), str(da[47]), str(da[48]), str(da[49]),
        str(da[50]), str(da[51]),
        str(da[52]), str(da[53]), str(da[54]), str(da[55]), str(da[56]), str(da[57]), str(da[58]), str(da[59]),
        str(da[60]), str(da[61]), str(da[62]), str(da[63]), str(da[64]), str(da[65]), str(da[66])
    )
    mycur.execute(sql, params)
    mys.commit()


if __name__ == '__main__':
    excel = read_excel()
    print (excel.ncols)
    print(excel.nrows)
    for ex in range(99200, excel.nrows):
        print ex
        sqk(excel.row_values(ex))
