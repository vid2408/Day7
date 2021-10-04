# write a content of 1 file into new file

import csv
with open('mycsv.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_mycsv.csv','w') as new_file:
        fieldnames = ['firstname','lastname','email']

        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames, delimiter=' ')

        csv_writer.writerheader()

        for line in csv_reader:
            csv_writer.writerow(line) 