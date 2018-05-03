import pandas as pd
import os

def make_dataset(input_file, split_rate, new_fold):
    """a total csv file to different types file

    Args:
        input: the needed csv file
        split_rate: train and validation rate
        new_fold: to store processed file

    """ 
    if not os.path.exists(new_fold):
        os.makedirs(new_fold)
    else:
        print('new_fold: {} is existed'.format(new_fold))

    data = pd.read_csv(input_file, names=['images', 'types', 'labels'])
    data = data.sample(frac=1).reset_index(drop=True)
    types = list(set(data['types']))
    for i in types:
        subdata = data[data['types']==i].sample(frac=1).reset_index(drop=True)
        train = subdata.iloc[:int(split_rate*len(subdata))]
        test = subdata.iloc[int(split_rate*len(subdata)):]
        train.to_csv(os.path.join(new_fold, '{}_train.csv'.format(i)),
                index=False,
                header=False)

        test.to_csv(os.path.join(new_fold, '{}_test.csv'.format(i)),
                index=False,
                header=False)

def concat_dataset(file1, file2):
    data1 = pd.read_csv(file1)
    data2 = pd.read_csv(file2)
    data = [data1, data2]
    data = pd.concat(data)
    data.to_csv(os.path.join('data','train.csv'),
                                index=False,
                                header=False)

if __name__ == '__main__':
    input_file = 'Annotations/label.csv'
    new_fold = 'data1'
    split_rate = 0.8
    make_dataset(input_file, split_rate, new_fold)
    #concat_dataset('data/coat_length_labels_train.csv', 'data/coat_length_labels_test.csv')  
