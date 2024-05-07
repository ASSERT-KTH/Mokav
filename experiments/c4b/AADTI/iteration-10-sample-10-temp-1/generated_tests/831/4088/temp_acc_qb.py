def patched_func(*args):
	global_list = []
	
	
	def Prime(x):
	    if (x < 2):
	        return True
	    for i in range(2, (int((x ** 0.5)) + 1)):
	        if ((x % i) == 0):
	            return False
	    return True
	n = int(args[0])
	if Prime(n):
	    global_list.append(1)
	elif (((n % 2) == 0) or Prime((n - 2))):
	    global_list.append(2)
	else:
	    global_list.append(3)
	return global_list