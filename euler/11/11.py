n = len(p)
max1 = 0
mxd = []
#number of elemends we need to add in the grid 
E = 4
print 'Executing first loop'
for x in range(0, n):
   for y in range(0, n-E):
      sum1 = p[x][y] + p[x][y+1] + p[x][y+2] + p[x][y+3]
      if sum1 > max1:
         max1 = sum1
         mxd = [ p[x][y], p[x][y+1] , p[x][y+2] , p[x][y+3] ]

print 'Executing second loop'
for y in range(0, n):
   for x in range(0, n-E):
      sum1 = p[x][y] + p[x+1][y] + p[x+2][y] + p[x+3][y]
      if sum1 > max1:
         max1 = sum1
         mxd = [p[x][y] , p[x+1][y] , p[x+2][y] , p[x+3][y]]

print 'Executing third loop'
#get diagonal left end only
for x in range(0, E):
   for y in range(0, n-E):
      sum1 = p[x][y] + p[x+1][y+1] + p[x+2][y+2] + p[x+3][y+3]
      if sum1 > max1:
         max1 = sum1
         mxd = [p[x][y] , p[x+1][y+1] , p[x+2][y+2] , p[x+3][y+3]]

print 'Executing fourth loop'
#get diagonal right end only
for x in range(n-E, n):
   for y in range(0, n-E):
      sum1 = p[x][y] + p[x-1][y+1] + p[x-2][y+2] + p[x-3][y+3]
      if sum1 > max1:
         max1 = sum1
         mxd = [p[x][y] , p[x+1][y-1] , p[x+2][y-2] , p[x+3][y-3]]

print 'Executing fifth loop'
#get diagonal middle only
for x in range(E, n-E):
   for y in range(0, n-E):
      sum1 = p[x][y] + p[x+1][y+1] + p[x+2][y+2] + p[x+3][y+3]
      sum2 = p[x][y] + p[x-1][y+1] + p[x-2][y+2] + p[x-3][y+3]
      if sum1 > max1:
         max1 = sum1
         mxd = [p[x][y] , p[x+1][y+1] , p[x+2][y+2] , p[x+3][y+3]]
      if sum2 > max1:
         max1 = sum2
         mxd = [p[x][y] , p[x-1][y+1] , p[x-2][y+2] , p[x-3][y+3]]

      

         
