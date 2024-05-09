def original_func(*args):
	global_list = []
	
	
	def readln():
	    return tuple(map(int, args[0].split()))
	global_list.append(('YES' if (readln()[0] in [((n * (n + 1)) // 2) for n in range(1, 25)]) else 'NO'))
	return global_list