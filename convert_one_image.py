from PIL import Image, ImageFilter, ImageEnhance
import os 
image = '/home/gtwell/rename_all_file/img/cashmere/cashmere0.jpg'
target_dir = '/home/gtwell/rename_all_file/examples/'

img = Image.open(image)
img = img.resize((256,256))
img1 = ImageEnhance.Contrast(img).enhance(2.0)
img2 = ImageEnhance.Contrast(img).enhance(1.3)
img3 = ImageEnhance.Contrast(img).enhance(0.5)
img4 = img.transpose(Image.FLIP_LEFT_RIGHT)
img5 = img.transpose(Image.FLIP_TOP_BOTTOM)
img6 = ImageEnhance.Brightness(img).enhance(0.5)
img7 = ImageEnhance.Brightness(img).enhance(1.5)
img8 = img.rotate(90)
img9 = img.rotate(180)
img10 = img.rotate(270)
img1.save(target_dir+'con2'+'.jpg')
img2.save(target_dir+'con1.3'+'.jpg')
img3.save(target_dir+'con0.5'+'.jpg')
img4.save(target_dir+'leftr'+'.jpg')
img5.save(target_dir+'topb'+'.jpg')
img6.save(target_dir+'bri0.5'+'.jpg')
img7.save(target_dir+'bri1.5'+'.jpg')
img8.save(target_dir+'ro90'+'.jpg')
img9.save(target_dir+'ro180'+'.jpg')
img10.save(target_dir+'r0270'+'.jpg')
