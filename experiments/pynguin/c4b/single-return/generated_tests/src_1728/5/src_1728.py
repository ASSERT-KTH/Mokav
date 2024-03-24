def func(*args):
	
	
	def readln():
	    return tuple(map(int, args[0].split()))
	(n,) = readln()
	return((pow(3, (n - 1), ((10 ** 6) + 3)) if n else 1))
