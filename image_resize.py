from PIL import Image, ImageFile
import time
import os
ImageFile.LOAD_TRUNCATED_IMAGES = True

def imageResizing(fileName):
    imgPath = os.path.join('public/img', fileName)
    inputImg = Image.open(imgPath)

    # 이미지 700x700으로 변환
    output_img = inputImg.resize((700, 700))
    output_img.save(imgPath)
