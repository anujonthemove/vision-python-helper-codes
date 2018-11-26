import cv2
import numpy as np
import base64
import time


start = time.time()

img = cv2.imread('/home/anuj/Desktop/46511410_517363538765212_2374887477535047680_n.jpg')

cv2.imshow('org', img)

print(img.shape)

w, h, c = img.shape
img_dtype = img.dtype
print(img_dtype)
print(w, h, c)


res_img = img.reshape(1, w*h*c)

enc_img = base64.b64encode(res_img).decode("utf-8")
dec_img = np.frombuffer(base64.decodestring(enc_img), dtype=img_dtype)
 
# print(dec_img.shape)
test_img = dec_img.reshape(w, h, c)

cv2.imshow('test_img', test_img)
cv2.waitKey()
print(test_img.shape)
# cv2.imwrite('conv.jpg', test_img)
end = time.time()

print(end-start)

