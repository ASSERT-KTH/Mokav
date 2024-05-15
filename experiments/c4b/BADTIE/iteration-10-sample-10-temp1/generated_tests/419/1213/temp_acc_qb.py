def patched_func(*args):
	global_list = []
	
	(n, a, b) = args[0].split()
	(n, a, b) = (int(n), int(a), int(b))
	if (b > 0):
	    Sum = (a + (b % n))
	    if (Sum > n):
	        Sum = (Sum - n)
	    global_list.append(Sum)
	elif (b < 0):
	    Sum = (a - (abs(b) % n))
	    if (Sum <= 0):
	        Sum = (Sum + n)
	    global_list.append(Sum)
	elif (b == 0):
	    global_list.append(a)
	return global_list