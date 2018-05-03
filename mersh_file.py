import os
import shutil


def mersh_file(path, new_fold):
    r"""
    args:
        path: the directory we need to mersh
    output:
        a mershed file.
    """
    
    if not os.path.exists(new_fold):
        os.makedirs(new_fold)
    else:
        print('new_fold: {} is existed'.format(new_fold))
        
    for parent, dirs, files in os.walk(path):
        for index, _file in enumerate(files):
            old_path = os.path.join(parent, _file)
            name = old_path.split(sep='/')
            name = name[0:-1]
            name = ''.join(name)
            #os.rename(old_path, new_path+'/'+str(index)+'_'+file)
            new_path = new_fold+'/'+name+'_'+str(index)+'_'+_file
            shutil.copyfile(old_path, new_path)


if __name__ == '__main__':
    path = 'walk'
    new_fold = 'data'
    mersh_file(path, new_fold)
