import numpy as np
import csv
import math
from geopy import distance

coast_file = "../data/coast0.5.csv"
station_file = "../data/stations_normalized.csv"

coast_orig = np.genfromtxt(coast_file, delimiter=',', dtype=None, encoding=None)[1:]
station_orig = np.genfromtxt(station_file, delimiter=',', dtype=None, encoding=None)[1:]

coast = np.genfromtxt(coast_file, delimiter=',')
station = np.genfromtxt(station_file, delimiter=',')

coast = np.delete(coast, 2, 1)[1:]
station = np.delete(station, 2, 1)[1:]

rad = 6371

with open('../data/nearest_coast.csv', 'w') as out:
	csv_out = csv.writer(out)
	csv_out.writerow(['Latitude', 'Longitude', 'Distance', 'Direction'])
	for i, xy in enumerate(station):
		dists_sq = []
		lat1, lon1 = math.radians(xy[0]), math.radians(xy[1])
		for j, xy_coast in enumerate(coast):
			lat2, lon2 = math.radians(xy_coast[0]), math.radians(xy_coast[1])
			dlat = lat2 - lat1
			dlon = lon2 - lon1
			sin_lat = math.sin(dlat / 2)
			sin_lon = math.sin(dlon / 2)
			a = sin_lat ** 2 + math.cos(lat1) * math.cos(lat2) * (sin_lon ** 2)
			c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
			dists_sq.append(rad * c)
			# dists_sq.append(distance.distance(xy, xy_coast).km)
		min_val, min_idx = min((val, idx) for (idx, val) in enumerate(dists_sq))
		
		lat2, lon2 = math.radians(coast[min_idx][0]), math.radians(coast[min_idx][1])
		diffLong = lon2 - lon1

		x = math.sin(diffLong) * math.cos(lat2)
		y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1) * math.cos(lat2) * math.cos(diffLong))

		initial_bearing = math.atan2(x, y)
		initial_bearing = math.degrees(initial_bearing)
		compass_bearing = (initial_bearing + 360) % 360
		
		row = [xy[0], xy[1], min_val, compass_bearing]
		csv_out.writerow(row)

# mindist=np.zeros((len(station), 1))
# 	mindist[i],minid[i]=dists.min(),dists.argmin()