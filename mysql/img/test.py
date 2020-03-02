import pymysql
import requests

my1 = pymysql.connect(host="47.95.235.183", user='root', password="Kiretyo1521",
                      db='gd_map_charging_station', port=3306, charset='utf8mb4')
mycur1 = my1.cursor()


def downloadImageFile(local_filename, imgUrl):
    print "Download Image File=", local_filename
    local_filename = local_filename + '.ico'
    r = requests.get(imgUrl, stream=True)  # here we need to set stream = True parameter
    with open("./" + local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
        f.close()
    return local_filename


if __name__ == '__main__':
    name = 'Evcard'
    file_name = downloadImageFile(name, 'http://www.evcardchina.com/Public/images/icon.ico')
    print file_name
    f = open("./" + file_name, "rb")
    b = f.read()
    f.close()
    mycur1.execute(
        "UPDATE gd_map_charging_station.brand_type SET  content = %s WHERE id = 2;",
        (pymysql.Binary(b)))
    my1.commit()
