def original_func(*args):
	global_list = []
	
	from math import sqrt
	
	def sum_digits(x):
	    res = 0
	    while (x > 0):
	        res += (x % 10)
	        x //= 10
	    return res
	n = int(args[0])
	root = int(sqrt(n))
	for i in range((root - 100), (root + 1), 1):
	    sd = sum_digits(i)
	    if ((((i * i) + (sd * i)) - n) == 0):
	        global_list.append(i)
	        exit(0)
	global_list.append('-1')
	return global_list