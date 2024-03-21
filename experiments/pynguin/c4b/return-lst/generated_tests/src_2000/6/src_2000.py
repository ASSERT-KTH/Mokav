def func(*args):
	ret_values = []
	
	
	def get_number(k):
	    current = 1
	    div = 1
	    while True:
	        if ((k % div) == 0):
	            current += 1
	            div *= 2
	        else:
	            return (current - 1)
	inp = args[0]
	(n, k) = inp.split(' ')
	ret_values.append(get_number(int(k)))

	return ret_values
