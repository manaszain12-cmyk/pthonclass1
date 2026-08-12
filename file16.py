                     #Python Tuples

# weekdays = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon')

# print(weekdays)
# print(type(weekdays))
# print(weekdays[2:4])
# print(weekdays[-3])

# ramadan = ('fast',)
# print(ramadan)
# print(type(ramadan))

# month = tuple(('Jan', 'Feb', 'Mar'))
# print(month)
# print(type(month))

#Error
# weekdays = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')
# print[2] = 'Sun'
# print(weekdays)

# weekdays = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')
# weekdays_list = list(weekdays)
# print(weekdays_list)
# weekdays_list.append("Sat")
# weekdays_list.append("Sun")
# print(weekdays_list)
# weekdays = tuple(weekdays_list)
# print(weekdays)

# print(type(weekdays_list))
# print(type(weekdays))

# month1 = tuple(('Jan', 'Feb', 'Mar'))
# month2 = tuple(('Jan', 'Feb', 'Mar'))
# month = month1 + month2
# print(month)

#Unpacking
# weekdays = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')
# (day1, day2, day3, day4, day5,) = weekdays 
# print(day1)
# print(day2)
# print(day3)
# print(day4)
# print(day5)

weekdays = ('Mon', 'Tue', 'Wed', 'Thu', 'Tue', 'Fri')
print(weekdays.count('Tue'))
print(weekdays.index('Thu'))



