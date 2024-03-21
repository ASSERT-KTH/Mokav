def func(*args):
	ret_values = []
	
	
	def readln():
	    return tuple(map(int, args[0].split()))
	(n,) = readln()
	ret_values.append((pow(3, (n - 1), ((10 ** 6) + 3)) if n else 1))

	return ret_values
