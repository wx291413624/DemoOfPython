import pymysql
import requests

my = pymysql.connect(host="127.0.0.1", user='debian-sys-maint', password="PmOL3zdw6WErzZ7a",
                     db='gd_map_charging_station', port=3306, charset='utf8')
mycur = my.cursor()
sql = """INSERT INTO gd_map_charging_station.num_of_city (num,city_name,adcode,city_code) VALUES (%s, %s,%s, %s);"""

if __name__ == '__main__':
    res = requests.get(
        'https://restapi.amap.com/v3/place/text?parameters?keywords=%E5%85%85%E7%94%B5%E6%A1%A9&key=e6d08db6376e80527dc47e5ec2d2a0e9&types=011100')
    json = res.json()
    suggestion = json.get('suggestion')
    cities = suggestion['cities']
    for cit in cities:
        params = (cit['num'], cit['name'], cit['adcode'], cit['citycode'])
        mycur.execute(sql, params)
        my.commit()
