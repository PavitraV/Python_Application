import sys
import os
import csv


filename = 'monthly_csv.csv'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()
		
source = input('Enter the source (GCAG or GISTEMP): ')
year_or_range_of_years = input('Enter a year or a range of years in the form XXXX -- XXXX: ')
month = input('Enter a month: ')
average = 0
years_above_average = []

years = year_or_range_of_years.split('--')
years = [int(i) for i in years]
years.sort()
len1 = len(years)

def months(month):
	months = ['January','February','March','April','May','June','July','August','September','October',
			 'November','December']
	return '{:02d}'.format(months.index(month)+1)

list2 = []
list3 = []

with open(filename, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in csvreader:
		if(row[0] == source):
			list1 = row[1].split('-')
			if(int(list1[0])>=years[0] and int(list1[0])<=years[len1-1] and list1[1] == months(month)):
				list2.append(row[2])
				list3.append(list1[0])
				
	list2 = [float(i) for i in list2]
	average = sum(list2)/float(len(list2))
	for i in range(len(list2)):
		if(average<list2[i]):
			years_above_average.append(list3[i])
			
years_above_average = [int(i) for i in years_above_average]
years_above_average = sorted(years_above_average)

print(f'The average anomaly for {month} in this range of years is: {average:.2f}.')
print('The list of years when the temperature anomaly was above average is:')
print(years_above_average)
