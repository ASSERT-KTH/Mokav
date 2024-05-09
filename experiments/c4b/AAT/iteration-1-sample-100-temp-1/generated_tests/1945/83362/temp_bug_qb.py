def original_func(*args):
	global_list = []
	
	(a, b, n) = [int(x) for x in args[0].split(' ')]
	
	def addingdigits(a, b, n):
	    t = 0
	    for i in range(10):
	        if ((((a * 10) + i) % b) == 0):
	            t = ((a * 10) + i)
	            break
	    if (t == a):
	        return (- 1)
	    else:
	        return (t * pow(10, (n - 1)))
	global_list.append(addingdigits(a, b, n))
	return global_list