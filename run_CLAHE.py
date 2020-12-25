import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import pdb

#process image enhancemenet by LAB spaces.
#used CLAHE dehaze
def CLAHE(name, contrast):
    colorCorrection = False

    img = cv2.imread('../all_data/0921_113311_hdr_ev-3.0_sef_2995.png')

    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV) 

    img_y = img_yuv[:,:,0] 
    img_u = img_yuv[:,:,1]
    img_v = img_yuv[:,:,2]

    ret_img = np.zeros_like(img)

    #CLAHE
    clahe = cv2.createCLAHE(clipLimit=0.5,
                            tileGridSize=(8, 8))

    # start = time.time()
    clahe = clahe.apply(img_y)
    temp_u = np.zeros_like(img_u)
    temp_v = np.zeros_like(img_v)

    # end = time.time()
    # print ('averge time is:', end-start)

    ret_img[:, :, 0] = clahe
    # pdb.set_trace()

    #orignal
    if not colorCorrection:
        ret_img[:, :, 1] = img_u
        ret_img[:, :, 2] = img_v

    else:
        img_y = img_y.astype(np.float32)/255
        img_u = img_u.astype(np.float32)/255
        img_v = img_v.astype(np.float32)/255

        temp_u = clahe * (img_u / img_y)
        temp_v = clahe * (img_v / img_y)

        temp_u = temp_u * 255
        temp_v = temp_v * 255

        ret_img[:,:,1] = temp_u.astype(np.uint8)
        ret_img[:,:,2] = temp_v.astype(np.uint8)

    #color correction
    result = cv2.cvtColor(ret_img, cv2.COLOR_YUV2BGR)
    cv2.imwrite('../all_data/0921_162047_hdr_ev-3.0_source_sef_2995_dehaze.png', result)
 
