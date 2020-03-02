# coding=utf-8
import MySQLdb


class BlobDataTestor:
    def __init__(self):
        self.conn = MySQLdb.connect(host='47.95.235.183', user='root', passwd='Kiretyo1521',
                                    db='gd_map_charging_station')

    def __del__(self):
        try:
            self.conn.close()
        except:
            pass

    def closedb(self):
        self.conn.close()

    def testRWBlobData(self):
        # 读取源图片数据
        f = open("./img/test.jpg", "rb")
        b = f.read()
        f.close()

        # 将图片数据写入表
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Dem_Picture (PicData) VALUES (%s)", (MySQLdb.Binary(b)))
        # self.conn.commit()

        # 读取表内图片数据，并写入硬盘文件
        cursor.execute("SELECT PicData FROM Dem_Picture ORDER BY ID DESC limit 1")
        d = cursor.fetchone()[0]
        cursor.close()

        f = open("C:\\22.jpg", "wb")
        f.write(d)
        f.close()

    # 下面一句的作用是：运行本程序文件时执行什么操作


if __name__ == "__main__":
    test = BlobDataTestor()
    try:
        test.testRWBlobData()
    finally:
        test.closedb()
