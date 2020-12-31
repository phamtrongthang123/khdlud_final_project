from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from cssselector import *
from config import *
import os
import re
import requests
import time


class Crawler:
    def __init__(self, url):
        self.driver = webdriver.Edge(PATH)
        self.url = url
        self.driver.get(url)

    def __reformate_numeric(self,x):
        if x[-1] == 'k':
            x = float(x.replace(",",".").strip("k")) * 1000
        elif x[-1] == 'r':
            x = float(x.replace(",",".").strip("tr")) * 1000000
        else:
            x = float(x)
        return x

    def start_crawling(self):
        self.driver.get(self.url)
        sleep(1)
        total_height = int(self.driver.execute_script("return document.body.scrollHeight"))
        for j in range(1, total_height, 90):
            self.driver.execute_script("window.scrollTo(0, {});".format(j))
            sleep(0.5)

        # name = self.driver.find_element_by_css_selector(CSSSelector.NAME).text
        name = self.driver.find_element_by_css_selector(CSSSelector.NAME).text.replace('\n', ' ')
        if name[:11] == "YÊU ThÍCh+ ":
            name = name[11:] 
        elif name[:10] == "YÊU ThÍCh ":
            name = name[10:]
        
        avg_rating = self.driver.find_element_by_css_selector(CSSSelector.AVG_RATING).text        
        n_reviews = self.driver.find_element_by_css_selector(CSSSelector.N_REVIEWS).text 
        n_sold = self.driver.find_element_by_css_selector(CSSSelector.N_SOLD).text 
        price = self.driver.find_element_by_css_selector(CSSSelector.PRICE).text     
        n_loved = self.driver.find_element_by_css_selector(CSSSelector.N_LOVED).text.split(' ')[-1][1:-1]       
        rate_5 = self.driver.find_element_by_css_selector(CSSSelector.RATE_5).text.split(' ')[-1][1:-1]        
        rate_4 = self.driver.find_element_by_css_selector(CSSSelector.RATE_4).text.split(' ')[-1][1:-1]
        rate_3 = self.driver.find_element_by_css_selector(CSSSelector.RATE_3).text.split(' ')[-1][1:-1]
        rate_2 = self.driver.find_element_by_css_selector(CSSSelector.RATE_2).text.split(' ')[-1][1:-1]
        rate_1 = self.driver.find_element_by_css_selector(CSSSelector.RATE_1).text.split(' ')[-1][1:-1]
        rate_with_cmt = self.driver.find_element_by_css_selector(CSSSelector.RATE_WITH_CMT).text.split(' ')[-1][1:-1]
        rate_with_imgvid = self.driver.find_element_by_css_selector(CSSSelector.RATE_WITH_IMGVID).text.split(' ')[-1][1:-1]
        n_reviews =  self.__reformate_numeric(n_reviews)
        n_sold =  self.__reformate_numeric(n_sold)
        price = price.split(' - ')[0][1:] # remove max price and ₫
        n_loved =  self.__reformate_numeric(n_loved)
        rate_5 =  self.__reformate_numeric(rate_5)
        rate_4 =  self.__reformate_numeric(rate_4)
        rate_3 =  self.__reformate_numeric(rate_3)
        rate_2 =  self.__reformate_numeric(rate_2)
        rate_1 =  self.__reformate_numeric(rate_1)
        rate_with_cmt =  self.__reformate_numeric(rate_with_cmt)
        rate_with_imgvid =  self.__reformate_numeric(rate_with_imgvid)
        
        price = float(price.replace(".",""))
        # shop_name = self.driver.find_element_by_css_selector(CSSSelector.SHOP_NAME).text
        
        # shop_n_review = self.driver.find_element_by_css_selector(CSSSelector.SHOP_N_REVIEW).text
        # shop_n_product = self.driver.find_element_by_css_selector(CSSSelector.SHOP_N_PRODUCT).text
        # shop_rate_feedback = self.driver.find_element_by_css_selector(CSSSelector.SHOP_RATE_FEEDBACK).text
        # shop_time_feedback = self.driver.find_element_by_css_selector(CSSSelector.SHOP_TIME_FEEDBACK).text
        # shop_age = self.driver.find_element_by_css_selector(CSSSelector.SHOP_AGE).text
        # shop_follower = self.driver.find_element_by_css_selector(CSSSelector.SHOP_FOLLOWER).text

        # shop_n_review =  self.__reformate_numeric(shop_n_review)
        # shop_n_product =  self.__reformate_numeric(shop_n_product)
        # shop_follower =  self.__reformate_numeric(shop_follower)
        curl_split = self.url.split('.')
        shopid = curl_split[-2]
        r = requests.get(f'https://shopee.vn/api/v2/shop/get?is_brief=1&shopid={shopid}')

        shop_name, shop_n_review , shop_n_product , shop_rate_feedback, shop_time_feedback, shop_age , shop_follower = r.json()['data']['account']['username'],r.json()['data']['rating_bad'] + r.json()['data']['rating_normal'] + r.json()['data']['rating_good'], r.json()['data']['item_count'], r.json()['data']['response_rate'], r.json()['data']['response_time'], (time.time()  - r.json()['data']['ctime']) ,r.json()['data']['follower_count']   
        res = {
            'name': name,
            'avg_rating':avg_rating,
            'n_reviews':n_reviews,
            'n_sold':n_sold,
            'price':price,
            'n_loved':n_loved,
            'n_rate_5':rate_5,
            'rate_4':rate_4,
            'rate_3':rate_3,
            'rate_2':rate_2,
            'rate_1':rate_1,
            'rate_with_cmt':rate_with_cmt,
            'rate_with_imgvid':rate_with_imgvid,
            'shop_name':shop_name,
            'shop_n_review':shop_n_review,
            'shop_n_product':shop_n_product,
            'shop_rate_feedback':shop_rate_feedback,
            'shop_time_feedback':shop_time_feedback,
            'shop_age':shop_age,
            'shop_follower':shop_follower,
            'comments':[],
            'img_url':[]
        }
        total_cmt = n_reviews
        while len(res['comments']) <= 30 and total_cmt > 0 :
            list_cmt = self.driver.find_elements_by_css_selector(CSSSelector.CMT_LIST)
            total_cmt -= len(list_cmt)
            for it in list_cmt:
                stars = it.find_element_by_css_selector(CSSSelector.CMT_RATING)
                stars = stars.find_elements_by_css_selector(CSSSelector.CMT_STAR_ACTIVE)
                rating = len(stars)
                try:
                    content = it.find_element_by_css_selector(CSSSelector.CMT_CONTENT).text.replace(' \n','. ').replace('\n',' ').replace('\t',' ')
                except:
                    continue        
                res['comments'].append((rating,content))
            self.driver.find_element_by_css_selector('div.shopee-page-controller.product-ratings__page-controller > button.shopee-icon-button.shopee-icon-button--right').click()
            sleep(1.5)

        # try:
        #     os.mkdir('./imgs')
        # except:
        #     pass

        # list_imgs = self.driver.find_elements_by_css_selector('._2Fw7Qu.V1Fpl5')
        # for img in list_imgs:
        #     img_url = img.value_of_css_property("background-image")
        #     img_raw_url = re.split('[()]',img_url)[1]
        #     # try:
        #         print(img_raw_url)
        #         r = requests.get(img_raw_url, allow_redirects=True)
        #         filename = img_raw_url.split('/')[-1]
        #         path = f'./imgs/{filename}.png'
        #         print('?')
        #         open(path, 'wb').write(r.content)
        #         print(f'ok {path}-{img_raw_url}')
        #     # except:
        #     #     print('fail')
        #     #     continue
        list_imgs = self.driver.find_elements_by_css_selector('._2Fw7Qu.V1Fpl5')
        for img in list_imgs:
            img_url = img.value_of_css_property("background-image")
            img_raw_url = re.split('[()]',img_url)[1]
            res['img_url'].append(img_raw_url)
        return res 
        
    def finish_crawling(self):
        self.driver.close()