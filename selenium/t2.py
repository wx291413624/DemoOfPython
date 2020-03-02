# coding=utf-8
import time

from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys

reload(sys)
sys.setdefaultencoding('utf8')
browser = webdriver.Firefox()

url = "https://www.baidu.com"
browser.get(url)

js = 'window.open("https://www.amap.com/detail/B0FFKBQY8P?citycode=110000'
thiswid = browser.current_window_handle
ss = browser.execute_script(js + '");')
all_h = browser.window_handles
browser.switch_to_window(all_h[1])
time.sleep(1)

print browser.find_element_by_xpath('/html/body').text
print browser.page_source
# browser.close()
# browser.switch_to_window(thiswid)
# browser.page_source
