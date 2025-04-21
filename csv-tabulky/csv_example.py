import csv

with open('employee.csv', 'w') as empfile:
    empwr = csv.writer(empfile)
    empwr.writerow(['John Smith', 'Accounting', 'November 2020'])
    empwr.writerow(['Jan'])
    empwr.writerow(['Erica Meyers', 'IT', 'March 2019'])
    empwr.writerow([])
    empwr.writerow(['Johanna "Maxi" Maxe, Ph.D.', 'CEO', 'July 2018'])

# soubor znovu otevreme, ale tentokrat pro cteni
with open('employee.csv', 'r') as empfile:
    empread = csv.reader(empfile) # reader vraci iterator, pres ktery muzeme prochazet
    for record in empread:
        if len(record) < 3:
            continue
        print(record[0],record[1],record[2])
