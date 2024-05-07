def original_func(*args):
	global_list = []
	
	
	def readln():
	    return tuple(map(int, args[0].split()))
	(n,) = readln()
	global_list.append((pow(3, (n - 1), ((10 ** 6) + 3)) if n else 0))
	return global_list