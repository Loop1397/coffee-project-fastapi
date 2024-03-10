# selenium : 브라우저를 제어하는 모듈.
# js를 이용하여 동적으로 로드되는 웹 브라우저를 스크래핑 하기위해 사용.
# 정적인 브라우저는 BeautifulSoup만으로도 해결 가능
from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import time

# 표준 출력 인코딩을 UTF-8로 설정
sys.stdout.reconfigure(encoding='utf-8')

def getStoreUrls():
    result = {}
    
    # Selenium 웹 드라이버 시작
    driver = webdriver.Chrome()

    # 믕스토리 URL
    url = 'https://litt.ly/mungstery'

    # 웹 페이지 열기
    driver.get(url)

    # 웹 페이지의 HTML 가져오기
    html = driver.page_source

    # Selenium 웹 드라이버 종료
    driver.quit()
    
    # BeautifulSoup으로 HTML 파싱
    soup = BeautifulSoup(html, 'html.parser')

    # 가져온 <div> 태그 출력
    a_tags = soup.find_all('a')
    a_tags = a_tags[:-5]
    for a_tag in a_tags:
        # 링크 텍스트와 href 속성 출력
        
        h2_tag = a_tag.find('h2')
        # print(f'카페 이름 : {h2_tag.text}')
        # print(f'URL : {a_tag['href']}')
        result[h2_tag.text] = a_tag['href']

    time.sleep(1)
    print('믕스토리 url 취득')
    
    return result