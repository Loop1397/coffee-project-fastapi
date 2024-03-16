import json
import sys
import re

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
with open('products.json', 'r') as f:

    json_data = json.load(f)

json_data = list(json_data)

for data in json_data:
    print(extract_filename(data['thumbnailUrl']))