import urllib
import uuid

imgurl = "https://www.gamersky.com/showimage/id_gamersky.shtml?https://img1.gamersky.com/image2019/07/20190713_ljt_red_220_7/gamersky_068origin_135_201971316493E6.jpg"
u = uuid.uuid1()
if __name__ == '__main__':
    urllib.urlretrieve(imgurl, str(u).replace("-", "") + "s.jpg")
