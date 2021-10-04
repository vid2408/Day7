import csv

with open('annual-enterprise-survey-2020-financial-year-provisional-size-bands-csv.csv') as file:
    reader = csv.DictReader(file)

    count = 0 
    for row in reader:
        print(row)

        if count > 5:
            break

        count += 1