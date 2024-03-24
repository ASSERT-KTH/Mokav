def func(*args):
	ret_values = []
	
	
	def bigyears(a, b):
	    n = 0
	    while (a <= b):
	        a = (a * 3)
	        b = (b * 2)
	        n = (n + 1)
	    return n
	(a, b) = args[0].split(' ')
	a = int(a)
	b = int(b)
	ret_values.append(bigyears(a, b))

	return ret_values
