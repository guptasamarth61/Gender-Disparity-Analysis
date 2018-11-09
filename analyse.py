import pandas as pd
import numpy as np
import ast
import matplotlib.pyplot as plt
data = pd.read_csv("outCsv2.csv")
data = data.dropna()
#print(data['Prob'][0])
timeline = data['Date']
#print(timeline.head(5))
gender = data['Prob']

year = []
var1 = ast.literal_eval(timeline[0])
for j in timeline:
	var1 = ast.literal_eval(j)
	year.append(var1[1])
year_unique1 = list(set(year))
year_unique = sorted(year_unique1, reverse = True)
print(year_unique)



male_auth = []
female_auth = []
for k in gender:
	var = ast.literal_eval(k)
	if (var[0] < 0):
		female_auth.append(1)
		male_auth.append(0)
	elif(var[0] != 696969):
		male_auth.append(1)
		female_auth.append(0)
	else:
		male_auth.append(0)
		female_auth.append(0)

# for j in range(0, len(year_unique)):
# 	for k in gender:
# 		for i in timeline:
# 			var2 = ast.literal_eval(i)[1]
# 			while (var2 == year_unique[j]):
# 				male_auth = 0
# 				female_auth = 0
# 				var = ast.literal_eval(k)
# 				if (var[0] < 0):
# 					female_auth += 1
# 				elif(var[0] != 696969):
# 					male_auth += 1
# 				print(female_auth, male_auth)


male_co_auth = []
female_co_auth = []
for k in gender:
	var1 = ast.literal_eval(k)
	#print(var1)
	m = 0
	f = 0
	for i in range(1, len(var1)):
		if(var1[i]<0):
			f += 1
		elif(var1[i] == 696969):
			continue
		else:
			m += 1
	male_co_auth.append(m)
	female_co_auth.append(f)

def groups(x,y, z):
	sample_data = pd.DataFrame(data = {'Females': x, 'Males': y, 'Year': z})
	grouped = sample_data.groupby('Year')
	females = []
	males = []
	for group in grouped:
		females.append(group[1]['Females'].sum())
		males.append(group[1]['Males'].sum())
	gender_ratio = [a/b for a, b in zip(females, males)]
	return gender_ratio
	
def plot():
	plt.boxplot(year_unique1, ratio_author_coauthor)
	plt.xlabel("Year")
	plt.ylabel("Ratio of Author,Co-Author Gender Ratio")
	plt.title("Gender Ratio")
	plt.grid()
	plt.show()

gender_ratio_authors = groups(female_auth, male_auth, year)
gender_ratio_co_authors = groups(female_co_auth, male_co_auth, year)
ratio_author_coauthor = [a/b for a, b in zip(gender_ratio_authors, gender_ratio_co_authors)]
plot()
