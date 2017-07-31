#!/usr/bin/env python
#coding:utf8

import pickle
import sys
import time
import re
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from PIL import ImageFilter
import pytesseract
import json
import datetime
reload(sys)     
sys.setdefaultencoding('utf8')


class SogouStockSpider:
    
    def __init__(self):
        """init"""

        self.url_prefix = "http://zhishu.sogou.com/index/searchHeat?kwdNamesStr="
        self.url_afterfix = "&timePeriodType=YEAR&dataType=SEARCH_ALL&queryType=INPUT"
        self.stock_code_path = "data/stock_code.in"

    def getIndex(self, stock_code, ttype = 0):
        """getIndex"""

        time.sleep(2)
        self.url = self.url_prefix + stock_code + self.url_afterfix

        js = 'window.open("'+self.url+'");'
        self.browser.execute_script(js)
        handles = self.browser.window_handles
        self.browser.switch_to_window(handles[-1])
        time.sleep(5)

        out_ret = {'code':stock_code, 'data':[]}

        if ttype:
            xoyelement = self.browser.find_elements_by_css_selector(".listwRA a")[1]
            xoyelement.click()
            time.sleep(2)

        xoyelement = self.browser.find_elements_by_css_selector("#linePart canvas")[0]
        x_0 = 30
        y_0 = xoyelement.size['height'] / 2

        #tmp = []
        while True:
            # 储存数字的数组
            try:
                ActionChains(self.browser).move_to_element_with_offset(xoyelement, x_0, y_0).perform()
                #time.sleep(2)

                print "11"
                data_element = self.browser.find_elements_by_css_selector("#linePart div")[1]
                data = data_element.text.strip().split("\n")
                print "22", data
                date = data[0].strip().replace(".", "-")
                print "33"
                index = data[1].split(":")[1].strip()
                
                index = re.sub("\D", "", index)
                index = 0
                if index:
                    index = int(index)
                print "44"

                out_ret['data'].append({'date':date, 'whole_index':index})
                print date, index
                print datetime.datetime.now()
                x_0 += 2
            except Exception as err:
                if len(out_ret["data"]) < 1:
                    x_0 += 2
                    continue
                print "sogou_partioal_error:", err
                break

        #out_ret['data'].extend(tmp)

        return out_ret

    def process(self):
        """process"""
        self.browser = webdriver.Chrome()
        self.browser.quit()

if __name__ == "__main__":
    url = "http://pinyin.sogou.com/dict/cate/index/167"
    #url = "http://download.pinyin.sogou.com/dict/download_cell.php?id=807&name=%E5%85%A8%E5%9B%BD%E7%9C%81%E5%B8%82%E5%8C%BA%E5%8E%BF%E5%9C%B0%E5%90%8D"
    browser = webdriver.Chrome()
    js = 'window.open("'+url+'");'
    browser.execute_script(js)
    handles = browser.window_handles
    browser.switch_to_window(handles[-1])
    for i in range(0,12):
        xoyelement = browser.find_elements_by_css_selector("#dict_nav_list a")
        co = 0
        while co < 3:
            try:
                xoyelement[i].click()
                time.sleep(2)
                break
            except Exception as e:
                print "not nav:", i
                time.sleep(2)
                co += 1
        ee = browser.find_elements_by_css_selector("#dict_page_list a")[-1]
        text = ee.text
        print "row:", i
        k = 0
        while ee.text.find("下一") != -1:
            k += 1
            j = 0
            kk = browser.find_elements_by_css_selector(".dict_dl_btn a")
            for v in kk:
                durl = v.get_attribute("href")
                j += 1
                print "col:", j
                co = 0
                while co < 3:
                    try:
                        #v.click()
                        js = 'window.open("'+durl+'");'
                        browser.execute_script(js)
                        time.sleep(1)
                        break
                    except Exception as e:
                        print "not crawl:", i, j, e
                        time.sleep(1)
                        co += 1
            co = 0
            while co < 3:
                try:
                    ee.click()
                    time.sleep(2)
                    break
                except Exception as e:
                    print "not xiayiye:", i, k, e
                    time.sleep(2)
                    co += 1
            ee = browser.find_elements_by_css_selector("#dict_page_list a")[-1]
            text = ee.text
    browser.quit()
