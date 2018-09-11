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

nearest <- fread("./imaginary-continent/data/nearest_coast.csv")
prelim <- fread("./imaginary-continent/data/training_prelim.csv")
prelim <- cbind(prelim, Distance = nearest$Distance, Direction = nearest$Direction)
fwrite(prelim, "./imaginary-continent/data/training_set.csv")

prelim <- fread("./imaginary-continent/data/num_training_set.csv")
shuffled <- prelim[sample(nrow(prelim)),]
fwrite(shuffled, "./imaginary-continent/data/num_training_set_shuffled.csv")

#Remove Longitude col
prelim <- subset(prelim, select = -c(V2))
fwrite(prelim, "./imaginary-continent/data/no_long.csv")

#Strip all but first character of Koppen classes
prelim$Koppen <- substr(prelim$Koppen, 0, 1)

#Convert class to numbers
shuffled$Koppen <- tolower(shuffled$Koppen)
myLetters <- letters[1:26]
shuffled$Koppen <- match(shuffled$Koppen, myLetters)

#Scale values
maxs <- apply(shuffled, 2, max)
mins <- apply(shuffled, 2, min)
new <- scale(shuffled, center = mins, scale = maxs - mins)

out <- as.data.frame(out)