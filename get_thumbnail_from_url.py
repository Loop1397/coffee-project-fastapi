import json
import sys
import re
import requests
import time
import os
from image_resize import imageResizing

# url에서 파일 이름 가져오기
def extract_filename(url):
    # URL에서 파일 이름 추출을 위한 정규표현식
    pattern = r'[^/]+\.jpg|[^/]+\.png|[^/]+\.jpeg'

    # 정규표현식을 사용하여 파일 이름 추출
    match = re.search(pattern, url.lower())
    if match:
        filename = match.group()
        return filename
    else:
        print(f"NONE!!!! {url}")
        return None

sys.stdout.reconfigure(encoding='utf-8')


def getThumbnailFromUrl(productsData):
    for data in productsData:
        # 파일 이름
        fileName = extract_filename(data['thumbnailUrl'])
        # 파일 url
        url = data['thumbnailUrl']

        # 이미지 요청 및 다운로드
        response = requests.get(url)
        with open(os.path.join('public/img/', fileName), 'wb') as file:
            file.write(response.content)
            
        data['filePath'] = os.path.join('./img/', fileName)
        
        imageResizing(fileName)
        break
    
    return productsData

# TEST

# with open('products.json', 'r') as f:
#     json_data = json.load(f)

# json_data = list(json_data)

# # print(getThumbnailFromUrl(json_data))
