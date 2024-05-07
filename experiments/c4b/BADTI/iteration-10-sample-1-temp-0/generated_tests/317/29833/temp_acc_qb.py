def patched_func(*args):
	global_list = []
	
	
	def drive(n, a):
	    if (a == n):
	        return 1
	    elif ((a % 2) != 0):
	        time = ((a // 2) + 1)
	    elif ((a % 2) == 0):
	        time = (((n - a) // 2) + 1)
	    return time
	(x, y) = map(int, args[0].split())
	global_list.append(drive(x, y))
	return global_list