# f.writelines([a2 + '\n' for a2 in a])
# a2 = [a[:-2] for a in f.readlines()]
from scrapy import Selector
from urllib import request
import pandas as pd
import time
from tqdm import tqdm

# column_names = ['col1', 'col2']

# data = pd.DataFrame(columns = column_names)


# artist = {'col1':'sss', 'col2':'ddd'}
# data = data.append(artist, ignore_index = True)


# data.to_csv('text.csv', mode='a', header=False, sep=';')


# x = pd.read_csv('text.csv',  sep=';')
# print(x.columns)
# print(x['benefits'])

a= [1, 2]
b= [2, *a]
print(b)