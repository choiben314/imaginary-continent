library("GSODR")
library(data.table)

gsod2016 = get_GSOD(years = "2016")
fwrite(gsod2016, "gsod_2016.csv")

dist2coast <- fread("./imaginary-continent/data/local/dist2coast.csv")
dist2coast <- dist2coast[which(dist2coast$V3 < 0.5)]
dist2coast.fwrite(dist2coast, "./imaginary-continent/data/coast0.5.csv")

stations <- fread("./imaginary-continent/data/weather_stations_signed_csv.csv")
stations$Latitude <- stations$Latitude / 100
stations$Longitude <- stations$Longitude / 100
fwrite(stations, "./imaginary-continent/data/stations_normalized.csv")