# -*- coding: utf-8 -*-
from PIL import Image

img1 = Image.open('images\\échiquier.jpg')
img2 = Image.open('images\\Dame_blanc.png')

image_new = Image.new('RGB',(img1.width,img1.height))
image_new.paste(img1,(0,0))
image_new.paste(img2,(195,185),img2)
image_new.paste(img2,(2215,2200),img2)




image_new.save('images\\mergedImages.png')
