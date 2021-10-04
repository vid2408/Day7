# write a content of 1 file into new file

import csv
with open('mycsv.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_mycsv.csv','w') as new_file:
        csv_writer = csv.writer(new_file, delimiter=' ')

        for line in csv_reader:
            csv_writer.writerow(line) 