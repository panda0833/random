#days in a month (not leap year)
day = ['', 'M', 'T', 'W', 'H','F','S', 'U']


#iy: initial year; the first year to start counting (ex: 1900)
#ey (end year); last year to include in counting for sundays
# (ex: 2000) 
def find_sundays(days_in_month, iy, ey, ci):
   if days_in_month == None:
      days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
   #count of months beginning with sundays
   count = 0
   #current day in the 'day' list, set default to Monday 
   if ci == None:
      ci = 1 
   for x in range(iy, ey+1):
      for y in days_in_month:
         if day[ci] == 'U':
            count = count + 1
         ci = calc_ci(ci, y) #if next year is a leap year, change feb
      if (x+1) % 4 == 0:
         days_in_month[1] = 29
      else:
         days_in_month[1] = 28

   print 'Months beginning with sundays: ', count, 'Last day: ', ci
   return count
   
#sets the current index (ci) to the beginning day of the next month 
def calc_ci(ci, days_this_month):
   #include plus one for starting at first day 
   x = (days_this_month % 7)
   if ci + x > 7:
      ci = x - (7-ci)
   else:
      ci = ci + x
   return ci



def test_find_sundays():
   #change days in month to sample input
   days_in_month = [6, 7, 7,1]
   count = find_sundays(days_in_month,3,4, None)
   if count == 4:
      print 'Tests passed'
   else:
      print 'Test failed'
