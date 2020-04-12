import pandas as pd
df = pd.read_csv('text.csv',  sep=';')


# number of existemce
for category in df.columns[1:-1]:
	temp_list = []
	for i in range(0, len(df['must_have'])):
		temp_list.append(len(df[category][i].replace("['", '').replace("']", '').split("', '")))
	# category_len[category] = max(temp_list)
	print(category, ': ', max(temp_list))

print('')

# Index(['Unnamed: 0', 'must_have', 'nice_to_have', 'work_methodology',
#        'equipment_supplied', 'specs', 'perks_in_the_office', 'benefits',
#        'url'],



# category = 'equipment_supplied'
for category in df.columns[1:-1]:
	merged_positions = []

	for i in range(0, len(df['must_have'])):
		merged_positions = merged_positions + df[category][i].replace("['", '').replace("']", '').split("', '")
		
	print(category, ': ', list(dict.fromkeys(merged_positions)), '\n\n')
