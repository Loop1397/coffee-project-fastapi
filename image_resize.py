from PIL import Image

input_img = Image.open("103178096062351735_1015449818.jpg")
print("input image size:", input_img.size)

output_img = input_img.resize((700, 700))
print("output image size:", output_img.size)
output_img.save("103178096062351735_1015449818New.jpg")