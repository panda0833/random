i# Red of Euler problem 67, without using dijikstra and a bit more efficient?
#    0
#   4 2
#  1 2 3
# 3 1 7 9

def ac(x):
   global b
   p = map(lambda x,y: x+y, x,b)
   b = []
   reduce(ab, p)

def ab(x,y):
   global b
   if x>y:
      b.append(x)
   else:
      b.append(y)
   return y

def run(l):
   b = []
   reduce(ab, l[0])
   map(lambda x: ac(x), l[1:-1])
   print 'Biggest sum is: ', b[0] + l[-1][0] 
