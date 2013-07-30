def multiply(x, y):
   lenx = len(str(x))
   if len(str(x)) <= 1 and len(str(y)) <= 1:
      print 'got here:' + str(x) + ':' + str(y)
      return (x*y)

   a = str(x)[:lenx/2]
   print ':'+a
   b = str(x)[lenx/2:]
   print ':'+b
   c = str(y)[:lenx/2]
   print ':'+c
   d = str(y)[lenx/2:]
   print ':'+d
   ac = multiply(int(a),int(c))
   print 'returned from ac: ' + str(ac)
   bd = multiply(int(b),int(d))
   print 'returned from bd: ' + str(bd)
   adbc = multiply(int(a)+int(b), int(c)+int(d))-ac-bd

   return 10**(lenx)*ac + 10**(lenx/2)*adbc + bd
   


   



   
