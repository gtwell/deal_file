import pandas as pd
import requests

path = 'd://project/classification/fabric.xlsx'
data = pd.read_excel(path, usecols=[0], names=['url'])
target_path = 'd://project/classification/dataset/trash/'

for i in range(len(data)):
    url = data['url'][i]
    r = requests.get(url)
    with open(target_path + str(i)+'.jpg', 'wb') as a:
        a.write(r.content)
