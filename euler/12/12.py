

primes = []
minRange = 9000
maxRange = 15000
#sumPrimesUpTo(5000)

def getTriNum(x):
   z = (x * (x + 1))/2 
   return z 
      
#Method 1: Using division approach -- get the factors via brute force division (upt to half of the number), see function div()  
def ft1():
   global minRange, maxRange
   maxx = 0
   for x in range(minRange, maxRange):
      t = getTriNum(x)
      factors = div(t)
      length = len(factors)
      if length > maxx:
         maxx = length
         print x, t, maxx
       
#Method 2: Using divisino 
def ft2():
   global blist, rlist
   global minRange, maxRange,counter2
   counter2 = 0 
   maxx = 0
   #Max tri number 
   for x in range(minRange, maxRange):
      t = getTriNum(x)
      #magic trick -- only numbers divisible by 6 will have the greatest factors 
      if t%6 != 0:
         continue 
      blist = []
      rlist = []
      getPrimeFactors(t)
      brute_force()
      f = len(set(rlist))
      if f > maxx:
         maxx = f
         print x, t, maxx

#Method 3: Using hueristics
def ft3():
   global blist, rlist
   global minRange, maxRange,counter2
   counter2 = 0
   maxx = 0
   #Max tri number 
   #sumPrimesUpTo(getTriNum(maxRange))
   for x in range(minRange, maxRange):
      t = getTriNum(x)
      if t%2 != 0:
         continue 
      blist = []
      getPrimeFactors(t)
      f = abc(blist)
      if f > maxx:
         maxx = f
         print x, t, maxx

rlist = []
def findNums():
   global l, blist, rlist
   maxx = 0 
   for x in range(590000, 592000):
      blist = []
      rlist = []
      getPrimeFactors(120 * x)
      brute_force()
      f = len(set(rlist))
      if f > maxx:
         maxx = f
         print 'new max: ',f
         if maxx > 500:
            print x * 120 
            break
         
         

      
def div(x):
   counter = 0 
   l = []
   for y in range(1, x/2+1):
      counter = counter + 1
      if x%y == 0:
         l.append(y)
   l.append(x)
   #print len(l), counter
   return l        


counter = 0 

#Gets all the prime factors of x
# ex:  x = 12, then this function returns: 2, 2, 3
def getPrimeFactors(x):
   global blist, counter
   if x <= 1:
      return
   for y in range(0, len(primes)):
      counter = counter + 1
      #print x, primes[y]
      if int(x**0.5) < primes[y]:
         break;
      if x % primes[y] == 0:
         blist.append(primes[y])
         getPrimeFactors(x/primes[y])
         return
   if x != 1:
      blist.append(x)
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


def brute_force():
   global blist
   if len(blist) <= 0:
      print 'blist not defined properly'
      return
   else:
      for x in range(0, len(blist)):
         choose(1, x, 0)

counter2 = 0
def choose(c,d,j):
   global counter2,blist,rlist
  # print d, j, len(blist)-d
   if d == 0:
      for y in range(j, len(blist)):
  #       print '## c:', c,' y: ', y
         rlist.append(c * blist[y])
         counter2 = counter2 + 1
      return
   else:
      for x in range(j, len(blist)-d):
         choose(blist[x]*c,d-1, x+1)





#heuristic approach to solving this problem 
def abc(a):
   global blist, rlist
   #hashmap containing the factors and the number of times they occur
   b = dict()
   factors = []
   summ = 0
   for x in a:
      if b.get(x):
         b.update({x:b.get(x)+1})
      else:
         b.update({x:1})

  # print b
   for x in range(0, len(a)):
      rlist = []
      temp = genList(b, x)
      #print x, temp
      blist = temp[1]
      #print blist
      #print temp[0], temp[1], choose(temp[1], x, 0)
      choose(1,x,0)
      #print 'Rlist is: ', rlist
      summ = summ + temp[0]
      factors.extend(rlist)
      #print x, temp[0]

   return summ+ len(set(factors))
   
   
def genList(l, i):
   b = [] 
   c = 0
   #print l,i
   for x in l:
      #print b, x
      if l.get(x) <= i:
         b.extend([x] * l.get(x))
      else:
         b.extend([x] * i)
         c = c + 1
   return [c,b]

   
sumPrimesUpTo(int(getTriNum(maxRange/8)**0.5))
