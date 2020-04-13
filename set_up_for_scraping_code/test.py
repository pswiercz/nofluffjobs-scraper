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

# a= [' s ', ' o ', ' aa ']
# x = ''

# # print([item.strip() for item in a])

# x = ', '.join([item.strip() for item in a])


# # for i, item in enumerate(a):
# # 	x  = x + item.strip()
# # 	if i != len(a)-1:
# # 		x += ', '

# print(x)


# print(' '.join([item.split()[0] for item in a]))

# print('s'.join(a))

# work_methodology_category = ['Integration tests', 'Unit tests', 'Tester', 'Agile management', 'Issue tracking tool', 
# 'Knowledge repository', 'Code reviews', 'Static code analysis', 'Version control system', 
# 'Build server', 'QA manager', 'Distributed team', 'Research and Experimentation', 'Pair programming', 
# 'Workshops', 'e2e tests', 'Commit on the first day', 'One command build possible', 'Up and running within 2h', 
# 'High level and low level designs', 'Feature development and porting', 'Regression testing', 
# 'UAT testing', 'Agile Testing', 'Manual tests', 'Database', 'Virtualization', 'Cloud infrastructure', 
# 'Operating system', 'Databases', 'Network virtualization', 'Provisioning', 'Networking hardware', 'Security', 
# 'Application stack', 'Operating systems']
# print(len(work_methodology_category))


d = {'a': '  ab  ', 'b': ' ss ', 'c': 'sqw '}

# # for key, item in d.items():
# # 	# print(key, item)
# # 	print(d[])
# # 	d[key] = item.split()[0]

# # print(d)

# print(d.keys())

for key, item in d.items():

    if item:
        if item[0] == ' ':
            d[key] = item[1:]
        if item[-1] == ' ':
            d[key] = item[:-1]

print(d)