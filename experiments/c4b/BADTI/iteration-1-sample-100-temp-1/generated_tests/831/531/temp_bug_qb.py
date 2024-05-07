def original_func(*args):
	global_list = []
	
	'input\n4\n'
	
	def is_prime(n):
	    if (n < 2):
	        return False
	    elif (n == 2):
	        return True
	    elif ((n % 2) == 0):
	        return False
	    elif all((((n % i) != 0) for i in range(3, (int((n ** 0.5)) + 1), 2))):
	        return True
	    return False
	n = int(args[0])
	if is_prime(n):
	    global_list.append(1)
	elif ((n % 2) == 0):
	    global_list.append(2)
	else:
	    global_list.append(3)
	return global_list