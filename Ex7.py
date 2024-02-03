string = 'January February March April May June July August September October November December'
months_first = tuple(month for month in string.split())
print(months_first)

#7.1
month_second = tuple(month for month in string.split() if month.startswith("J"))
print(month_second)
#7.2
month_third = tuple(month for month in string.split() if month.startswith("J") and len(month)<5)
print(month_third)

