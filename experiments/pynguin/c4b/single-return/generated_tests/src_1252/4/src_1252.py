def func(*args):
	
	
	def answer(n):
	    res = ''
	    for i in range(1, 371):
	        res = (res + str(i))
	    return res[(n - 1)]
	return(answer(int(args[0])))
