# import csv

# inFile = "../data/training_set.csv"
# outFile = "../data/num_training_set.csv"

# out = open(outFile, 'w')

# classes = []

# with open(inFile, "r") as f:
#     lines = csv.reader(f)
#     next(f)
#     for line in lines:
#     	if(not (line[5] in classes)):
#     		classes.append(line[5])
#     classes = sorted(classes)


# with open(inFile, "r") as f:
#     lines = csv.reader(f)
#     csv_writer = csv.writer(out)
#     next(f)
#     for line in lines: 
#     	row = line[0:5]
#     	row.append(str(classes.index(line[5])))
#     	csv_writer.writerow(row)

import csv

inFile = "../data/training_set_primary.csv"
outFile = "../data/num_training_set_primary.csv"

out = open(outFile, 'w')

classes = []

idx_koppen = 0;

with open(inFile, "r") as f:
    lines = csv.reader(f)
    next(f)
    for line in lines:
        idx_koppen = len(line) - 1
        if(not (line[idx_koppen] in classes)):
            classes.append(line[idx_koppen])
    classes = sorted(classes)


with open(inFile, "r") as f:
    lines = csv.reader(f)
    csv_writer = csv.writer(out)
    next(f)
    for line in lines: 
        row = line[0:idx_koppen]
        row.append(str(classes.index(line[idx_koppen]) + 1))
        csv_writer.writerow(row)