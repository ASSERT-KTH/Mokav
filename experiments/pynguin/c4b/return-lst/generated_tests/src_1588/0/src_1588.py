def func(*args):
	ret_values = []
	
	
	def is_prime(m):
	    i = 2
	    while ((i * i) <= m):
	        if ((m % i) == 0):
	            return False
	        i += 1
	    return True
	n = int(args[0])
	if (n == 2):
	    ret_values.append(1)
	elif ((n % 2) == 0):
	    ret_values.append(2)
	elif is_prime(n):
	    ret_values.append(1)
	elif is_prime((n - 2)):
	    ret_values.append(2)
	else:
	    ret_values.append(3)

	return ret_values
