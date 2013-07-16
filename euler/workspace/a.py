
stack = [] 
def choose(n,x):
   #n = 5, x = 3
   stack = []
   r(0,0,n,x)

def r(p, c, n,x):
   if x-c == 0:
      print stack
      return
   #print p,n-(x-1)+c-1,x-c
   for i in range(p, n-(x-1)+c):
      stack.append(i)
      r(i+1,c+1,n,x)
      stack.pop()
