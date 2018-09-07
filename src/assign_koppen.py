import numpy as np
import csv

koppen_file = "../data/koppen.csv"
station_file = "../data/stations_normalized.csv"

koppen_orig = np.genfromtxt(koppen_file, delimiter=',', dtype=None, encoding=None)[1:]
station_orig = np.genfromtxt(station_file, delimiter=',', dtype=None, encoding=None)[1:]

koppen = np.genfromtxt(koppen_file, delimiter=',')
station = np.genfromtxt(station_file, delimiter=',')

koppen = np.delete(koppen, 2, 1)[1:]
station = np.delete(station, 2, 1)[1:]

with open('../data/training_prelim.csv', 'w') as out:
	csv_out = csv.writer(out)
	csv_out.writerow(['Latitude', 'Longitude', 'Elevation', 'Koppen'])
	for i, xy in enumerate(station):
		dists_sq = np.sum((xy - koppen) ** 2, axis = 1)
		row = [xy[0], xy[1], station_orig[i][2], koppen_orig[dists_sq.argmin()][2]]
		csv_out.writerow(row)

# mindist=np.zeros((len(station), 1))
# 	mindist[i],minid[i]=dists.min(),dists.argmin()