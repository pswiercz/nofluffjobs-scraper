for url in tqdm(urls[:]):
	# offer = get_offer()

	seniority_freq.append(scrap_offer(url))
	time.sleep(2)

print(seniority_freq)

with open('seniority.txt', 'w') as f:
	[f.writelines(str(item)+',') for item in seniority_freq]
