def func(*args):
	ret_values = []
	
	
	def readln():
	    return tuple(map(int, args[0].split()))
	ret_values.append(('YES' if (readln()[0] in [((n * (n + 1)) // 2) for n in range(1, 50)]) else 'NO'))

	return ret_values
