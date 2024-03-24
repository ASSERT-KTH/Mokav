def func(*args):
	
	
	def readln():
	    return tuple(map(int, args[0].split()))
	return(('YES' if (readln()[0] in [((n * (n + 1)) // 2) for n in range(1, 50)]) else 'NO'))
