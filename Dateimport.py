import datetime
dateinput = input('Enter Starting date in YYYY-MM-DD format')
year, month, day = map(int, dateinput.split('-'))
Starting_date = datetime.date(year, month, day)
dateinput = input('Enter Ending date in YYYY-MM-DD format')
year, month, day = map(int, dateinput.split('-'))
Ending_date = datetime.date(year, month, day)
delta=Starting_date-Ending_date
print(delta.days) 



