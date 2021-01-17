class DateDiff:
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year
        
daysofmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
          
def datedifference(date1,date2):
    if(date2.day>=date1.day):
        noofdays=((date2.year-date1.year)*365)+(date2.day-date1.day)
    else:
        noofdays=((date2.year-date1.year)*365)-(date1.day-date2.day) 

    if(date2.month>=date1.month):
        for i in range(date1.month-1,date2.month-1):
            noofdays=noofdays+daysofmonth[i]
    else:
        for i in range(date2.month-1,date1.month-1):
            noofdays=noofdays-daysofmonth[i]
    leap=0
    for j in range(date2.year,date1.year-1,-1):
        if j%4==0:
            if j==date2.year:
                if date2.month>2:
                    leap=leap+1 
            elif j==date1.year:
                if date1.month<=2:
                    leap=leap+1
            elif ((j<date2.year) & (j>date1.year)):
                leap=leap+1
    return(noofdays+leap)
     
def dateval1(date1):
    dateinput = input('Enter Ending date in DD-MM-YYYY format')
    day, month, year = map(int, dateinput.split('-'))
    if((day>31)|(month>12)):
        print("Ending Date or month is out of range,Enter valid date")
        dateval1(date1) 
    else:
        date2=DateDiff(day,month,year)
        print(datedifference(date1,date2),"days")

def dateval():
    dateinput = input('Enter Starting date in DD-MM-YYYY format')
    day, month, year = map(int, dateinput.split('-'))
    if((day>31)|(month>12)):
        print("Starting Date or month is out of range,Enter valid date")
        dateval()
    else:
        date1=DateDiff(day,month,year)
        dateval1(date1)

dateval()




