def func(*args):
	ret_values = []
	
	
	def fun(n):
	    ln = len(n)
	    tmp = ord(n[0])
	    tmp = (tmp - 47)
	    for i in range((ln - 1)):
	        tmp *= 10
	    ret_values.append((tmp - int(n)))
	if (__name__ == '__main__'):
	    n = args[0]
	    fun(n)

	return ret_values
