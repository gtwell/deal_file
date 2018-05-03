import os

def rename():
	count = 0
	path = '/home/lk/cashmere_slim/slim/clothes/img/suit'
	
	filelist = os.listdir(path)
	for files in filelist:
		Olddir = os.path.join(path, files)
		if os.path.isdir(Olddir):
			continue
		filename = os.path.splitext(files)[0]
		filetype = os.path.splitext(files)[1]
		Newdir = os.path.join(path,'skirt'+str(count)+filetype)
		os.rename(Olddir, Newdir)
		count += 1
rename()
	
