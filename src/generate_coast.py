import csv

inFile = "../data/local/dist2coast.csv"
outFile = "../data/local/coast.csv"

with open(inFile, "r") as f:
    lines = csv.reader(f)
    next(f)
    for line in lines:  
    	if(float(line[3]) < 10):
        	with open(outFile,'a') as fd:
        		wr = csv.writer(fd, quoting=csv.QUOTE_ALL)
        		wr.writerow(line)