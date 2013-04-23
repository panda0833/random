factors = []
import collections 
def factor(x):
   """Fills up the 'factors' list with list of prime factors """ 
   # number is odd, so we need to divide by primes
   #get list of primes up to this number
   sroot = int(x**0.5)
   for m in range(0, len(primes)):
      p = primes[m]
      if p <= sroot:
         while x%p==0:
            x = x/p
            factors.append(p)
            sroot = int(x**0.5)
      else:
         factors.append(x)
         break

def count_factors(x):
   """Counts the number of factors given a list of prime factors, ex.
      given 2,2,2,3 being factors of 24, this will the total number of factors
      starting with 2,3, 2*2=4, 2*2*2=8, 3*2=6... etc."""
   counter = collections.Counter(x)
   #Example list (can't be one) : [2,2,2,3,3,5,6]
   #only get the count of each value in the list (2,2,2= 3, 3,3 = 2, 5=1.. etc) 
   #For the ex list this will be [3,2,1]
   values = counter.values() 
   #count all the 1s, for ex list this will be 2 since only 1 element of 5 and 1 of element 6
   ones = values.count(1)

   #only need to 2^n - 1 for values that are not duplicates, hence have
   #count value = 1 (ex list will be 2 namely 5 and 6) 
   non_duplicates = 2**ones-1

   #remove the 1 values, so we can use the duplicates for calculations
   values.remove(1)

   #First we need to add permutation of non duplicates (2^(ones) -1)  + all duplicate values
   #for ex this will be 2^2-1 + 5  = 8 
   total = reduce(lambda x, y: x+y, values) + non_duplicates

   #Next we need to calculate permutation of permutation of the non duplicates and add these to the multiplcations of all duplicates 
   #for ex this will be 2^(2^ones-1)-1  * (3*2) = x 
   total =  total + reduce(lambda x,y: x*y, values)  * (2**non_duplicates-1)

   return total
   
         
   

   
   
