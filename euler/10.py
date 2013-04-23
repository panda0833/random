primes = [2]

def testNums(n):
   for x in range(n):
      blah(x)

def blah(x):
   global t
   if x%2 == 0:
      t.append(x)
   else:
      t.append(1)

      
      

def sumPrimesUpTo(n):
   global primes
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
      
