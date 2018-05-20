import os
import shutil
import argparse
from PIL import Image


def merge_file(path, new_folder, N):
    r"""
    args:
        path: the directory we need to merge
    output:
        a merged file.
    """
    
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    else:
        print('new_folder: {} is existed'.format(new_folder))
        
    for parent, dirs, files in os.walk(path):
        for index, _file in enumerate(files):
            old_path = os.path.join(parent, _file)
#            name = old_path.split(sep='/')
#            name = name[0:-1]
#            name = ''.join(name)
            #os.rename(old_path, new_path+'/'+str(index)+'_'+file)
#            new_path = new_folder+'/'+name+'_'+str(index)+'_'+_file
#            shutil.copyfile(old_path, new_path)
#            shutil.copyfile(old_path, new_folder+'/'+str(N)+'_'+_file)
            img = Image.open(old_path)
            img.save(new_folder+str(N)+'.jpg')
            N = N + 1
            if N % 200 == 0:
                print('{} files have been processed'.format(N))


if __name__ == '__main__':
    path = 'walk/'
    new_folder = 'data1/'
    parser = argparse.ArgumentParser("merge_fiel")
    parser.add_argument("--path", type=str, default=path, help="input file")
    parser.add_argument("--new_folder", type=str, default=new_folder, help="output file")
    parser.add_argument("--N", type=int, default=0, help="rename the file begun with N")
    args = parser.parse_args()
    merge_file(args.path, args.new_folder, args.N)
