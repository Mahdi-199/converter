import json
import os
from traceback import print_tb
import numpy as np
import glob
from PIL import Image





def ReadImage(im_name):
	im = Image.open(im_name)  # open image
	width, height = im.size
	return width, height


def ReadJson(js_name):
	with open(js_name) as f:
		data = json.load(f)
		if data['imageData'] ==  '':
			print('Image data not available! ')
		
		# class_name = []
		# for i in range(0, len(data['shapes'])):
		# 	class_name.append(data['shapes'][i]['label'])
		
		# for name in class_name:
		# 	repetitions = class_name.count(name)
		# 	different_obj = len(data['shapes']) - repetitions
			
		
		
		
		
		object_num = len(data['shapes'])
		# for i in range(0, object_num):
		# 	label_name = data['shapes'][i]['label']
		# 	label_list.append(label_name)
		
		# points = (data['shapes'][0]['points'])
		# print(points)
		return data, object_num


def SaveTxt(label_txt, name, object_num):
	current_path = os.getcwd()
	print('*'*40, current_path)
	if object_num == 0:
		with open(name, 'w') as file:
			print('*'*10,'salam', '*'*10, name)
			file.write(label_txt + '\n')
			file.close()
	elif object_num > 0:
		with open(name, 'a') as file:
			print('*'*10,'salam', '*'*10, name)
			file.write(label_txt + '\n')
			file.close()		 


def ConvertTxt(image_path, txt_path):
	for txt_name in glob.glob(txt_path + '*.txt*'):
		print(txt_name)
		data, object_num = ReadJson(txt_name)
		im_path = txt_name.replace(txt_path, txt_path)
		im_name = os.path.splitext(im_path)[0]+'.jpg'
		width, height = ReadImage(im_name)
		if width == data['imageWidth'] and height == data['imageHeight']:
			print('The photo corresponding to txt\'s file was found! ')


	
		for object in range (0, object_num):
			print('0*'*10, object)
			label_name = data['shapes'][object]['label']
			label_list.append(label_name)
			points = (data['shapes'][object]['points'])
			polygon_label = ''
			for point in points:
				polygon_label += str(f'{(point[0]/width):.6f}') + ' ' + str(f'{(point[1]/height):.6f}') + ' '	
				print(polygon_label)
			polygon_label = str(label_list.index(label_name)) + ' ' + polygon_label
			txt_name = os.path.splitext(js_name)[0]+'.txt'
			print('----------------*-*-*-*-*****************label_name', label_name)
			SaveTxt(polygon_label, txt_name, object_num)




if __name__ == '__main__':
	label_list = []
	image_path = "/home/muhammad/Desktop/pipe_image/1-50/"
	json_path = "/home/muhammad/Desktop/pipe_image/1-50/"

	#image_path = "/home/muhammad/Downloads/ronaldo_dataset/images/data/train/images/"
	#txt_path = "/home/muhammad/Downloads/ronaldo_dataset/images/data/train/labels/"

	# convert image label json file to .txt
	ConvertTxt(image_path, json_path)
