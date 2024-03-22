import sys
import json
from mung_pashing import getStoreUrls
from products_pashing import getProductsFromStore
from get_thumbnail_from_url import getThumbnailFromUrl

# 표준 출력 인코딩을 UTF-8로 설정
sys.stdout.reconfigure(encoding='utf-8')
id = 1

# 믕스토리에서 각 로스터리의 모든 url을 가져옴
storeUrls = getStoreUrls()

products = []

# 각 스토어에서 product의 목록을 list로 가져옴
for roastery, url in storeUrls.items():
    result, id = getProductsFromStore(roastery, url, id)
    products.append(result)

#가져온 상품 데이터를 1차원 리스트로 변환
productsData = [item for sublist in products for item in sublist]

productsData = getThumbnailFromUrl(productsData)

# JSON 파일로 데이터를 저장합니다.
with open('products.json', 'w') as json_file:
    json.dump(productsData, json_file, indent=4)