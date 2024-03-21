def func(*args):
	ret_values = []
	
	(a, b) = args[0].split()
	a = int(a)
	b = int(b)
	
	def c(a, b):
	    counter = 0
	    while True:
	        if (a > b):
	            return counter
	        a = (a * 3)
	        b = (b * 2)
	        counter = (counter + 1)
	ret_values.append(c(a, b))

	return ret_values
