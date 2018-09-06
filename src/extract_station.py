file = "../data/weather_stations.txt"
ofile = "../data/weather_stations_filtered.txt"

weather_stations = open(file, 'r')
out = open(ofile, 'w')

lines = weather_stations.readlines()

for line in lines:
	if (len(line) == 58):
		out.write(line[37:])