from datetime import date,time,datetime,timedelta


my_date = date(2100,4,15 )
print(my_date.day)
print(my_date.isocalendar())
my_time = time(18,10,45)
print(my_time)
print(my_time.minute)
datee= datetime(2222,11,12,10,45,12)
print(datee)
print(datee.strftime('%d/%b/%Y %H:%M:%S'))

date_str = '10/12/2222'
conver_date = datetime.strptime(date_str, '%d/%m/%Y')
print(conver_date)

print(datee + timedelta(days = 10))


print(time.ctime(465327896))