import sys
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


sys.stdout.reconfigure(encoding='utf-8')


#img_src에서 날짜를 추출하기위한 정규표현식 패턴
pattern = r'\d{8}'

#li태그에서 정보 가져오기
def liAnalyse(li, id, roastery):
    result = {
        'id': id,
        'name': '',
        'price': '',
        'roastery': roastery,
        'thumbnailUrl': '',
        'productUrl': '',
        'dateAdded': '',
        'best': False,
        'new': False,
        'soldOut': False
    }
    
    img_tag = li.find('img')
    img_src = img_tag.get('src')
    index = img_src.find('?')
    if index != -1:
        img_src = img_src[:index]
        
    result['thumbnailUrl'] = img_src
    result['dateAdded'] = re.findall(pattern, img_src)[0]
    
    a_src = li.find('a').get('href')
    result['productUrl'] = 'https://smartstore.naver.com' + a_src
    
    #array
    # li_texts = li.text.strip().splitlines()
    li_texts = [tag.get_text() for tag in li.find_all()]
    
    strong_text_list = [strong_tag.get_text() for strong_tag in li.find_all('strong')]
    
    if 'BEST' in li_texts: 
        result['best'] = True
        li_texts.remove('BEST')
        
    if 'NEW' in li_texts:
        result['new'] = True
        li_texts.remove('NEW')
        
    if '일시 품절' in li_texts:
        result['soldOut'] = True
        li_texts.remove('일시 품절')
    
    result['name'] = strong_text_list[0]
    result['price'] = strong_text_list[1][:-1]

    return result

# 페이지의 모든 상품이 들어간 li태그 가져온 후 dict형태로 정리해서 return
def getProductsFromStore(roastery, url, id):
    result = []
        
    # Selenium 웹 드라이버 시작
    driver = webdriver.Chrome() 
    
    # 웹 페이지 열기
    driver.get(url)

    # 웹 페이지의 HTML 가져오기
    html = driver.page_source

    # Selenium 웹 드라이버 종료
    driver.quit()
    
    # BeautifulSoup으로 HTML 파싱
    soup = BeautifulSoup(html, 'html.parser')
    
    wholeProducts_element = soup.find('div', class_='whole_products')
    ul_elements = wholeProducts_element.find_all('ul')

    li_elements = ul_elements[-1].find_all('li')
    # print(li_elements)
    
    for li_element in li_elements:
        result.append(liAnalyse(li_element, id, roastery))
        id += 1
    
    
    time.sleep(1)
    
    return result, id