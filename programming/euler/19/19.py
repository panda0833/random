#days in a month (not leap year)
days_in_month = [6,7,7,7]
day = ['', 'M', 'T', 'W', 'H','F','S', 'U']

#current index
ci = 1 

#initial year; the first year to start counting (ex: 1900)
iy = 0

#end year; last year to include in counting for sundays
# (ex: 2000) 
ey = 100

#count of months beginning with sundays
count = 0

def find_sundays():
   global ci, count
   for x in range(iy, ey+1):
      for y in days_in_month:
         if day[ci] == 'U':
            count = count + 1
         calc_ci(y)
      #if next year is a leap year, change feb
      if (x+1) % 4 == 0:
         days_in_month[2] = 1
      else:
         days_in_month[2] = 7
   
#sets the current index (ci) to the beginning day of the next month 
def calc_ci(days_this_month):
   global ci
   #include plus one for starting at first day 
   x = (days_this_month % 7)
   if ci + x > 7:
      ci = x - (7-ci)
   else:
      ci = ci + x



def test_find_sundays():
   global days_in_month,iy,ey
   iy = 3
   ey = 5
   #change days in month to sample input
   days_in_month = [6, 7, 7,1]
   find_sundays()
   if count == 5:
      print 'Tests passed'
   else:
      print 'Test failed'
   
