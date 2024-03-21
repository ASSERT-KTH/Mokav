def func(*args):
	ret_values = []
	
	
	def answer(n):
	    res = ''
	    for i in range(1, 371):
	        res = (res + str(i))
	    return res[(n - 1)]
	ret_values.append(answer(int(args[0])))

	return ret_values
