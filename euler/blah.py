primes = [2,3,5,7,11,13,17,19]

def div(x):
   counter = 0 
   l = []
   for y in range(1, x/2+1):
      counter = counter + 1
      if x%y == 0:
         l.append(y)
   l.append(x)
   print len(l), counter
   return l        


counter = 0 
l = [] 
def div2(x):
   global l, counter
   if x <= 1:
      return
   for y in range(0, len(primes)):
      counter = counter + 1
      print x, primes[y]
      if int(x**0.5) < primes[y]:
         break;
      if x % primes[y] == 0:
         l.append(primes[y])
         div2(x/primes[y])
         return
   if x != 1:
      l.append(x)
   return

def sumPrimesUpTo(n):
   global primes
   primes = [2]
   if n < 5:
      return 'Please provide number > than 4'

   for x in range(3, n+1, 2):
      if isPrime(x):
         primes.append(x)

def isPrime(x):
   global primes

   sroot = int(x**0.5)

   for m in primes:
      if m > sroot:
         break;
      if x%m==0:
         return False
   return True

def bf():
   for x in range(1, len(l)):
      find_comb(x)

def find_comb(i,j):
   for y in range(i, j):
      
   
   for 
