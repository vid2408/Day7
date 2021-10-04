import csv
with open('mycsv.csv','w',newline='') as f:
    fieldnames = ['column1' , 'column2' , 'column3']
    thewriter = csv.DictWriter(f,fieldnames = fieldnames)

    thewriter.writeheader()
    for i in range(1,100):
        thewriter.writerow({'column1' : 'one' , 'column3' : 'three' , 'column2' : 'two'})
        thewriter.writerow({'column1' : 'four' , 'column3' : 'six' , 'column2' : 'five'})