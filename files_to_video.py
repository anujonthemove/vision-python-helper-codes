import cv2
import numpy as np
import os

path_to_images = '<path-to-videos>'

video_name = 'test.avi'
# fps = 30
# w = 720
# h = 576
out = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'MPEG'), fps, (w, h))

for file in sorted(os.listdir(path_to_images)):
	img = cv2.imread(os.path.join(path_to_images, file))
	cv2.imshow('original', img)
	out.write(img)
	cv2.waitKey(1)

out.release()