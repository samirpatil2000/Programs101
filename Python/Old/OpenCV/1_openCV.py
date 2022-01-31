import cv2
import numpy as np


img_path='rich.jpg'
img=cv2.imread(img_path)


if img is not None:
    print ('Image Read Successfully!')
    print(img)
    print(img.shape)
else:
    print ('Error Reading Image')

def get_image(img):
    cv2.imshow('Rich BHai', img)
    cv2.waitKey(0) # wait for keyboard input before continuing
    cv2.destroyAllWindows()
    return None
#get_image(img)


# color_changes=cv2.cvtColor(img,cv2.COLOR_BAYER_BG2BGR)
get_image(img)


