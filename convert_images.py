from PIL import Image, ImageFilter, ImageEnhance
#import matplotlib.pyplot as plt
import os
init_dir = '/home/gtwell/convert_files/test/wool/'
target_dir = '/home/gtwell/convert_files/testset/wool/'
for index, img in enumerate(os.listdir(init_dir)):
	try:
		img = os.path.join(init_dir,img)
		img = Image.open(img)
		img = img.resize((256,256))
#		img1 = ImageEnhance.Contrast(img).enhance(2.0)
#		img2 = ImageEnhance.Contrast(img).enhance(1.3)
#		img3 = ImageEnhance.Contrast(img).enhance(0.5)
#		img4 = img.transpose(Image.FLIP_LEFT_RIGHT)
#		img5 = img.transpose(Image.FLIP_TOP_BOTTOM)
#		img6 = ImageEnhance.Brightness(img).enhance(0.5)
#		img7 = ImageEnhance.Brightness(img).enhance(1.5)
#		img8 = img.rotate(90)
#		img9 = img.rotate(180)
#		img10 = img.rotate(270)
		img.save(target_dir+'origin_'+str(index)+'.jpg')
#		img1.save(target_dir+'con2_'+str(index)+'.jpg')
#		img2.save(target_dir+'con1.3_'+str(index)+'.jpg')
#		img3.save(target_dir+'con0.5_'+str(index)+'.jpg')
#		img4.save(target_dir+'leftr_'+str(index)+'.jpg')
#		img5.save(target_dir+'topb_'+str(index)+'.jpg')
#		img6.save(target_dir+'bri0.5_'+str(index)+'.jpg')
#		img7.save(target_dir+'bri1.5_'+str(index)+'.jpg')
#		img8.save(target_dir+'ro90_'+str(index)+'.jpg')
#		img9.save(target_dir+'ro180_'+str(index)+'.jpg')
#		img10.save(target_dir+'r0270_'+str(index)+'.jpg')


	#	img = os.path.join(init_dir,img)
		
	#	plt.imshow(img)
	#	plt.show()
	#	img = img.resize((256, 256))
	#	img1 = ImageEnhance.Contrast(img).enhance(2.0)
	#	img2 = img.filter(ImageFilter.GaussianBlur)
	#	img = img.transpose(Image.FLIP_LEFT_RIGHT)
	#	img3 = img.rotate(270)
	#	img.save(target_dir+'cashmere_left'+str(index)+'.jpg')
	except:
		continue	
