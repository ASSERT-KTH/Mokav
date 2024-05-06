def original_func(*args):
	global_list = []
	
	(n, a) = map(int, args[0].split())
	
	def odd(a):
	    c = 0
	    i = 1
	    while (i <= (n - 2)):
	        i += 2
	        c += 1
	    return c
	
	def even(a):
	    c = 0
	    i = n
	    while (i >= 2):
	        i -= 2
	        c += 1
	    return c
	if ((a % 2) == 0):
	    global_list.append(even(a))
	else:
	    global_list.append(odd(a))
	return global_list