from PIL import Image, ImageFile
import time
import os
ImageFile.LOAD_TRUNCATED_IMAGES = True

def imageResizing(fileName):
    imgPath = os.path.join('public/img', fileName)
    image = Image.open(imgPath)
    
    # 원본 이미지 가로, 세로 가져오기
    width, height = image.size
    # 가로 / 세로 비율 계산
    ratio = width / height
    
    # ratio가 1보다 크면 가로가 긴 3사진, 1보다 작으면 세로가 긴 사진
    if ratio >= 1:
        target_width = 700
        target_height = int(target_width / ratio)
    else:
        target_height = 700
        target_width = int(target_height * ratio)
        
    # 이미지 700x700으로 변환
    outputImg = image.resize((target_width, target_height))
    outputImg.save(imgPath)
    
imageResizing('chapter.png')
imageResizing('nz.png')