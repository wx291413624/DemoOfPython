# coding=utf-8
from mysql import find, find1, geodistance, mycur, my, inst

if __name__ == '__main__':
    # print(geodesic((30.28708, 120.12802999999997), (28.7427, 115.86572000000001)).m)  # 计算两个坐标直线距离
    # print(geodesic((30.28708, 120.12802999999997), (28.7427, 115.86572000000001)).km)  # 计算两个坐标直线距离
    sc = find(1, 10000)
    ex = find1()
    for s in sc:
        for e in ex:
            ddd = geodistance(s[0], s[1], e[0], e[1])
            if ddd < 41:
                print ddd
                if ddd < 41:
                    if ddd <= 10:
                        params = (10, s[2], e[2], ddd)
                        print params
                        mycur.execute(inst, params)
                        my.commit()
                    if ddd <= 20:
                        params = (20, s[2], e[2], ddd)
                        print params
                        mycur.execute(inst, params)
                        my.commit()
                    if ddd <= 30:
                        params = (30, s[2], e[2], ddd)
                        print params
                        mycur.execute(inst, params)
                        my.commit()
                    if ddd <= 40:
                        params = (40, s[2], e[2], ddd)
                        print params
                        mycur.execute(inst, params)
                        my.commit()
