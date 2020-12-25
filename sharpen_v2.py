import cv2

class sharpen():
	def __init__():
		pass
	def sharpen():
		pass

img = cv2.imread('./IMG_20190422_141408.jpg')
img_blur = cv2.GaussianBlur(img, (37,37), 0)
cv2.imwrite('img_gauss.jpg', img_blur)

img_unsharp = img - img_blur
cv2.imwrite('img_unsharpen.jpg', img_unsharp)

k = 0.05
img_sharp = img + k*(img_unsharp)

cv2.imwrite('sharpen_v2.jpg', img_sharp)
