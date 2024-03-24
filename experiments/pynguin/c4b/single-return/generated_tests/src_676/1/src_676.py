def func(*args):
	
	
	def fun(n):
	    ln = len(n)
	    tmp = ord(n[0])
	    tmp = (tmp - 47)
	    for i in range((ln - 1)):
	        tmp *= 10
	    return((tmp - int(n)))
	if (__name__ == '__main__'):
	    n = args[0]
	    fun(n)
