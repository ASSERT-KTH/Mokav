def func(*args):
	ret_values = []
	
	
	def solve(n):
	    if (n == 1):
	        return '1/1'
	    elif (n == 2):
	        return '5/6'
	    elif (n == 3):
	        return '2/3'
	    elif (n == 4):
	        return '1/2'
	    elif (n == 5):
	        return '1/3'
	    elif (n == 6):
	        return '1/6'
	(y, w) = args[0].strip().split(' ')
	(y, w) = (int(y), int(w))
	ret_values.append(solve(max(y, w)))

	return ret_values
