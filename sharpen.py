from PIL import Image
from PIL import ImageFilter
img = Image.open('test.jpg')
post_img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
post_img.save('sharpen.jpg')
