# coding=utf-8
import time

import pymysql
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

reload(sys)
sys.setdefaultencoding('utf8')
# browser = webdriver.Firefox()

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = Chrome(options=option)

url = "https://www.amap.com/search "
browser.get(url)
browser.find_element_by_xpath('//*[@id="searchipt"]').send_keys(unicode("充电桩", 'utf-8'))
browser.find_element_by_xpath('//*[@id="searchbtn"]').click()

print browser.title
my = pymysql.connect(host="127.0.0.1", user='debian-sys-maint', password="PmOL3zdw6WErzZ7a",
                     db='gd_map_charging_station', port=3306, charset='utf8mb4')
mycur = my.cursor()

sql = """ select  ids from charging_station where msg is null group by ids """
update_sql = """ UPDATE gd_map_charging_station.charging_station SET msg = %s where ids = %s """


def select_sql():
    mycur.execute(sql)
    res_list = mycur.fetchall()
    return res_list


def updateS(msg, ids):
    params = (msg, ids)
    mycur.execute(update_sql, params)
    my.commit()


def find_ms():
    list = select_sql()
    thiswid = browser.current_window_handle
    for lss in list:
        id = lss[0]
        url = 'https://www.amap.com/detail/get/detail?id=' + id
        js = 'window.open("' + url + '");'
        browser.execute_script(js)
        time.sleep(1)

        all_h = browser.window_handles
        browser.switch_to_window(all_h[1])
        text = browser.find_element_by_xpath('/html/body').text
        if 'rgv587_flag' in text:
            print '-----flag=---'
            time.sleep(5)
            browser.close()
            browser.switch_to_window(thiswid)
            continue
        if 'status":"6","data":"too fast' in text:
            print '-----too fast=---'
            time.sleep(5)
            browser.close()
            browser.switch_to_window(thiswid)
            continue
        print browser.page_source
        text2 = browser.find_element_by_xpath('/html/body/pre').text
        updateS(text2, id)
        browser.close()
        browser.switch_to_window(thiswid)


find_ms()
