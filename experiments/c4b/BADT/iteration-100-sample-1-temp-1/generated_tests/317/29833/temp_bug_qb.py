def original_func(*args):
	global_list = []
	
	
	def drive(n, a):
	    time = 0
	    if (a == n):
	        return 1
	    while ((time != a) and (time != (n - a))):
	        time = (time + 1)
	    return time
	(x, y) = map(int, args[0].split())
	global_list.append(drive(x, y))
	return global_list