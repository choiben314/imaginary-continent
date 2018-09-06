import pandas as pd

file = "../data/weather_stations_filtered.txt"
ofile = "../data/weather_stations_signed.txt"

weather_stations = open(file, 'r')
out = open(ofile, 'w')

lines = weather_stations.readlines()

for line in lines:
	wl = ''
	if (line[4] == 'N'):
		wl = line[:4]
	else:
		wl = '-' + line[:4]
	wl = wl + ' '
	if (line[11] == 'E'):
		wl = wl + line[6:11]
	else:
		wl = wl + '-' + line[6:11]
	wl = wl + ' ' + line[13:17] + '\n'
	out.write(wl)