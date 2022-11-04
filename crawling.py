from audioop import add
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import time
import os
import django
url_list = []
datas = []
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alcohol_trip.settings")
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# driver = webdriver(options=options)
django.setup()

from bars.models import Restaurant

def naverMapCrawling(search):
    driver = webdriver.Chrome("./chromedriver.exe") #selenium 사용에 필요한 chromedriver.exe 파일 경로 지정
    driver.get(f"https://m.map.naver.com/search2/search.naver?query={search}") 
    driver.implicitly_wait(3) # 로딩이 끝날 때 까지 10초까지는 기다림

    # 개별 url 접속 안 했을 때
    items = driver.find_elements(By.CSS_SELECTOR, '._item')
    
    my_url_list = []
    for item in items:
        aitem = item.find_element(By.CSS_SELECTOR, '.item_info > .item_common > .naver-splugin')
        sub_url = aitem.get_attribute('data-url')
        my_url_list.append(sub_url)

    cnt=0
    for url in my_url_list:
        cnt+=1
        driver.get(url)
        time.sleep(3)
        try:
            name = driver.find_element(By.CSS_SELECTOR, '.Fc1rA').text
        except:
            name = '이름 없음'
        try:
            address = driver.find_element(By.CSS_SELECTOR,'.IH7VW').text
        except:
            address = '주소 없음'
        try:
            category = driver.find_element(By.CSS_SELECTOR, '.DJJvD').text
        except:
            category = '카테고리 없음'
        try:
            tel = driver.find_element(By.CSS_SELECTOR, '.dry01').text
        except:
            tel = '전화번호 없음'
        map_url = driver.find_element(By.CSS_SELECTOR, '.qPoU1').get_attribute('href')

        try:
            picture1 = driver.find_element(By.CSS_SELECTOR, '#ibu_1').get_attribute('style').replace('width: 100%; height: 100%; background-image: url("', '').replace('"); background-position: 50% 0px;', '')
        except:
            picture1 = driver.find_element(By.CSS_SELECTOR, '#ugc_1').get_attribute('style').replace('width: 100%; height: 100%; background-image: url("', '').replace('"); background-position: 50% 0px;', '')
        try:
            picture2 = driver.find_element(By.CSS_SELECTOR, '#ibu_2').get_attribute('style').replace('width: 100%; height: 100%; background-image: url("', '').replace('"); background-position: 50% 0px;', '')
        except:
            picture2 = driver.find_element(By.CSS_SELECTOR, '#ugc_2').get_attribute('style').replace('width: 100%; height: 100%; background-image: url("', '').replace('"); background-position: 50% 0px;', '')
        try:
            picture3 = driver.find_element(By.CSS_SELECTOR, '#ibu_3').get_attribute('style').replace('width: 100%; height: 100%; background-image: url("', '').replace('"); background-position: 50% 0px;', '')
        except:
            picture3 = driver.find_element(By.CSS_SELECTOR, '#ugc_3').get_attribute('style').replace('width: 100%; height: 100%; background-image: url("', '').replace('"); background-position: 50% 0px;', '')
        
        try:
            driver.find_element(By.CSS_SELECTOR, '.MxgIj').click()
            open_list = driver.find_elements(By.CSS_SELECTOR, '.nNPOq')[1:]
            opening = ''

            for opens in open_list:
                try:
                    day = opens.find_element(By.CSS_SELECTOR, '.X007O > .ob_be > .kGc0c').text
                    times = opens.find_element(By.CSS_SELECTOR, '.X007O > .ob_be > .qo7A2').text
                    opening += day + ' ' + times + '\n'
                except:
                    break
        except:
            opening = '이용시간 없음'

        for character in string.punctuation:
            name = name.replace(character, '') # 특수기호 제거(파이어베이스에 경로로 저장하기 위해서)
        #document.querySelector("#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > a.a_item.a_item_distance._linkSiteview > div > em")
        #ct > div.search_listview._content._ctList > ul >ls li:nth-child(1) > div.item_info > a.a_item.a_item_distance._linkSiteview > div > em
        
        datas.append({
            "name" : name,
            "address" : address,
            "category": category,
            "tel" : tel,
            "map_url" : map_url,
            "opening" : opening,
            "picture1": picture1,
            "picture2": picture2,
            "picture3": picture3,
            })

        if cnt >= 30:
            break   
    # return datas

def add_data():
    result = []

    # 자료 수집 함수 실행
    for data in datas:
        tmp = data
        # 만들어진 dic를 리스트에 저장
        result.append(tmp)

    # DB에 저장
    for item in result:
        Restaurant(
        name=item["name"],
        category=item["category"],
        address=item["address"],
        phone=item["tel"],
        map_url = item["map_url"],
        hours=item["opening"],
        picture1=item["picture1"],
        picture2=item["picture2"],
        picture3=item["picture3"],
        ).save()
    return result

# DB 저장 함수 강제 실행(임시로 실행)

search = input("검색어를 입력해주세요! >> ")

naverMapCrawling(search)
add_data()