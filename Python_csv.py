import csv
f = open('annual-enterprise-survey-2020-financial-year-provisional-size-bands-csv.csv', 'rt')
myReader = csv.reader(f)
for row in myReader:
    print(row)

# import csv

# with open('annual-enterprise-survey-2020-financial-year-provisional-csv.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     for line in csv_reader:
#         print(line[3])


# import csv

# with open('annual-enterprise-survey-2020-financial-year-provisional-csv.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     with open('annual-enterprise-survey-2020-financial-year-provisional-csv.csv', 'w') as new_file:
#         fieldnames = ['Year','Industry_name_NZSIOC']

#         csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

#         csv_writer.writeheader()

#         for line in csv_reader:
#             csv_writer.writerow(line)
#             print(line)