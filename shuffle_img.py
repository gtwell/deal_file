import os
import random
from PIL import Image
init_dir = '/home/gtwell/convert_files/img622/img/cashmere/'
target_dir = '/home/gtwell/convert_files/shuffle/img/cashmere/'
file_list = os.listdir(init_dir)
random.shuffle(file_list)
for index, img in enumerate(file_list):
	try:
		img = os.path.join(init_dir,img)
		img = Image.open(img)
		img.save(target_dir+'cashmere_'+str(index)+'.jpg')
	except:
		continue	
