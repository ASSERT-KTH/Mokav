def original_func(*args):
	global_list = []
	
	
	def nod(a, b):
	    maxnod = (- 1)
	    if (a < b):
	        for i in range(1, (a + 1)):
	            if (((a % i) == 0) and ((b % i) == 0)):
	                maxnod = i
	    else:
	        for i in range(1, (b + 1)):
	            if (((a % i) == 0) and ((b % i) == 0)):
	                maxnod = i
	    return maxnod
	(a, b, n) = map(int, args[0].split())
	c = 0
	while (n >= 0):
	    c += 1
	    n -= nod(a, b)
	if ((c % 2) == 0):
	    global_list.append(0)
	else:
	    global_list.append(1)
	return global_list