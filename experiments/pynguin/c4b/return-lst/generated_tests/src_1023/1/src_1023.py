def func(*args):
	ret_values = []
	
	n = 0
	
	def rec(i):
	    global n
	    j = ((i * 10) + 4)
	    k = ((i * 10) + 7)
	    if ((j > n) and (k > n)):
	        return False
	    if (((n % k) == 0) or ((n % j) == 0)):
	        return True
	    if ((j < n) and (k < n)):
	        return (rec(j) or rec(k))
	    if (j < n):
	        return rec(j)
	    if (k < n):
	        return rec(k)
	n = int(args[0])
	if rec(0):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
