def original_func(*args):
	global_list = []
	
	
	def pow(base, power, mod):
	    if (power == 1):
	        return (base % mod)
	    if (power == 0):
	        return 1
	    x = (pow(base, (power // 2), mod) % mod)
	    if ((power % 2) == 0):
	        return ((x * x) % mod)
	    else:
	        return (((x * x) * (base % mod)) % mod)
	n = int(args[0])
	if (n < 2):
	    global_list.append('WRONG INPUT!')
	elif (n > 1000000000000000000):
	    global_list.append('WRONG INPUT!')
	elif (n < 10000000):
	    global_list.append(((5 ** n) % 100))
	else:
	    global_list.append((pow(5, n, 100) % 100))
	return global_list