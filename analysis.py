import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("offers//offers_python job for mid_2020-04-26_18-30-06.csv", sep=';')
df = df.drop('Unnamed: 0', axis=1)

def f_apple(row):
	if 'apple' in row['operating_system']:
		val = 1
	else:
		val = 0
	return val

def f_linux(row):
	if 'linux' in row['operating_system']:
		val = 1
	else:
		val = 0
	return val

def f_windows(row):
	if 'windows' in row['operating_system']:
		val = 1
	else:
		val = 0
	return val

df['op_apple'] = df.apply(f_apple, axis=1)
df['op_linux'] = df.apply(f_linux, axis=1)
df['op_windows'] = df.apply(f_windows, axis=1)

plt.bar([1, 2, 3], [sum(df['op_apple']), sum(df['op_linux']), sum(df['op_windows'])])
plt.xticks([1, 2, 3], ['apple', 'linux', 'windows'])
plt.title('Distribution of wanted operating systems across offers')
plt.show()



def f_avg_salary(row):
	if '+ vat (B2B) per month' in row['salary_1_description'] and row['seniority_2'] is np.nan:
		low, _, high, *_ = row['salary_1'].split(' ')
		avg = (int(low) + int(high))/2

	elif row['salary_2_description'] is not np.nan and '+ vat (B2B) per month' in row['salary_2_description'] and row['seniority_2'] is np.nan:
		low, _, high, *_ = row['salary_2'].split(' ')
		avg = (int(low) + int(high))/2

	else:
		avg = 0	

	return avg

df['avg_salary'] = df.apply(f_avg_salary, axis=1)
df.drop(df[df['avg_salary'] == 0].index , inplace=True)

df = df.sort_values(by=['avg_salary'], ascending=False)

for sen in df.seniority_1.unique():
	temp = df[df['seniority_1'] == sen]
	print(sen, ": ", round(temp['avg_salary'].mean(axis = 0), 2))