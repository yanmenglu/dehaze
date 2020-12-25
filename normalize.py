import numpy as np
import cv2
 
# mri_img = np.load('mri_img.npy')
mri_img = cv2.imread('../all_data/0921_143329_hdr_ev-3.0_source_sef_2995.png')
 
# normalization
mri_max = np.amax(mri_img)
mri_min = np.amin(mri_img)
mri_img = ((mri_img-mri_min)/(mri_max-mri_min))*255
mri_img = mri_img.astype('uint8')
 
r, c, h = mri_img.shape
for k in range(h):
 temp = mri_img[:,:,k]
 clahe = cv2.createCLAHE(clipLimit=0.5, tileGridSize=(8,8))
 img = clahe.apply(temp)
 cv2.imwrite('../all_data/0921_143329_hdr_ev-3.0_source_sef_2995_dehaze_0.5.png', img)
#  cv2.imshow('mri', np.concatenate([temp,img], 1))
#  cv2.waitKey(0)