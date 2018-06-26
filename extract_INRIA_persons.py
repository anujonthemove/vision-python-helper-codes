"""
This is a very very CRUDE implementation for extracting individual humans from images for INRIAPerson Dataset
Official link: http://pascal.inrialpes.fr/data/human/
Download link: ftp://ftp.inrialpes.fr/pub/lear/douze/data/INRIAPerson.tar
Keywords: INRIA Person dataset, pedestrians, humans
@author: Anuj Khandelwal
NOTE: Code improvement pending! Use wisely or contact me when stuck :)
"""
import os
import cv2
import numpy as np
import re
from pprint import pprint
import pickle

def store_cropped_image(img_path, x1, y1, x2, y2, save_path):
	img = cv2.imread(img_path)
	cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
	crop_img = img[y1:y2, x1:x2]
	# cv2.imshow("test", crop_img)
	cv2.imwrite(save_path, crop_img)
	# cv2.waitKey()



search_label = 'Original label for object'
search_bbox = 'Bounding box for object'
search_imgname= 'Image filename :'
cwd =os.getcwd()

# path = '/home/anuj/Desktop/INRIAPerson/Train/annotations/crop001001.txt'


person_count = 1
data = {}


for file_name in sorted(os.listdir('/home/anuj/Desktop/INRIAPerson/Train/annotations/')):
	
	img_path = ""
	label_list = []
	bbox_list = []
	path_list = []
	# print os.path.join('/home/anuj/Desktop/INRIAPerson/Train/annotations', file_name)
	path = os.path.join('/home/anuj/Desktop/INRIAPerson/Train/annotations', file_name)
	with open(path, 'r') as file:
		for line in file:
			line = line.strip()

			if search_imgname in line:
				img_path = line.split(':')[-1].replace('"', '').strip()

			if search_label in line:
				# print line.split()[-1]
				label_list.append(line.split()[-1])

			if search_bbox in line:
				# print line.split()[-4:]
				# print(re.findall('\d+', line))
				# print [int(x) for x in re.findall('\d+', line)][1:]
				bbox_list.append([int(x) for x in re.findall('\d+', line)][1:])
			

	
	for i in range(len(label_list)):
		save_path = os.path.join(cwd, 'Train/people_cropped/person_'+str(person_count)+'.jpg')
		dir_path = 'Train/people_cropped/person_' + str(person_count)+'.jpg'
		store_cropped_image(os.path.join(cwd, img_path), bbox_list[i][0], bbox_list[i][1], bbox_list[i][2], bbox_list[i][3], save_path)
		print(dir_path + ',' + str(bbox_list[i]))
		data[dir_path] = bbox_list[i]
		person_count += 1

# pickle.dump( data, open( "save.p", "wb" ) )