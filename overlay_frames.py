import cv2
import numpy as np
import os

roi = (273, 175, 102, 83)
pt1 = (273, 175)
pt2 = (273+102, 175+83)
color = (0, 0, 0)

# ordering of points is very important, see example
# a3 = np.array( [[[10,10],[100,10],[100,100],[10,100]]], dtype=np.int32 ) example
pts = np.array( [[[273, 175], [273+102, 175], [273+102, 175+83], [273, 175+83]]], np.int32)
img_to_mask = cv2.imread('image_3020.jpg')


# crop
height,width,depth = img_to_mask.shape
mask = np.zeros((height,width), np.uint8)
# cv2.rectangle(img_to_mask, pt1, pt2, (255, 255, 255), thickness=cv2.FILLED)
cv2.fillPoly(mask, pts, color=(255,255,255))
# cv2.imshow('mask', mask)

test = cv2.bitwise_and(img_to_mask, img_to_mask, mask=mask)
# cv2.imshow('final', test)


path_to_images = '/home/anuj/git/personal/github/self/vision-python-helper-codes/addimgs/image'
renamed_path = '/home/anuj/git/personal/github/self/vision-python-helper-codes/final/'

# 2. video properties
video_name = 'test.avi'
fps = 30
w = 720
h = 576
out = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'MPEG'), fps, (w, h))

i = 3021
for file in sorted(os.listdir(path_to_images)):
	img1 = cv2.imread(os.path.join(path_to_images, file))
	cv2.imshow('original', img1)
	cv2.rectangle(img1, pt1, pt2, color, thickness=cv2.FILLED)
	cv2.imshow('rectangle', img1)
	cv2.imshow('final', img1+test)
	num = str(i).zfill(4)
	renamed_file = '%s_%s' % (renamed_path+'image', num) + '.jpg'
	cv2.imwrite(renamed_file, img1+test)
	out.write(img1+test)
	i += 1
	cv2.waitKey(1)

# img1 = cv2.imread(path_to_images)
# # use same roi to blacken region	
# cv2.rectangle(img1, (pt1), pt2, color, thickness=cv2.FILLED)
# cv2.imshow('original', img1)
# cv2.imshow('added', img1+test)

# cv2.waitKey()