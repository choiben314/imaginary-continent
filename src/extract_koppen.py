import numpy as np 
import csv

koppen = np.genfromtxt("../data/koppen/koppen_1901-2010.tsv", dtype=None, names=True, encoding=None)

with open('koppen.csv', 'w') as out:
	csv_out=csv.writer(out)
	csv_out.writerow(['latitude', 'longitude', 'koppen'])
	for row in koppen:
		csv_out.writerow(row)
