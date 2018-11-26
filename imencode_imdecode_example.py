import cv2
import numpy as np


img = cv2.imread('/home/anuj/Desktop/39454616_2623182871055519_4601753674627153920_n.jpg')

_, imenc_img = cv2.imencode('.jpg', img)

print(imenc_img.shape)

imdec_img = cv2.imdecode(np.fromstring(imenc_img, dtype=np.uint8), 1)

print(imdec_img.shape)
cv2.imwrite('cvimg.jpg', imdec_img)

