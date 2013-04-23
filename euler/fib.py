def fib(a,b):
	global x
	if b>4000000:
		return x
	if b%2==0:
		x = x + b
	fib(b, a+b)

