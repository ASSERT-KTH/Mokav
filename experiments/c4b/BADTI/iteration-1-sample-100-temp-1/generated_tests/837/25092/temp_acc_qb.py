def patched_func(*args):
	global_list = []
	
	
	def is_prime(m):
	    i = 2
	    while ((i * i) <= m):
	        if ((m % i) == 0):
	            return False
	        i += 1
	    return True
	n = int(args[0])
	if (n == 2):
	    global_list.append(1)
	elif ((n % 2) == 0):
	    global_list.append(2)
	elif is_prime(n):
	    global_list.append(1)
	elif is_prime((n - 2)):
	    global_list.append(2)
	else:
	    global_list.append(3)
	return global_list