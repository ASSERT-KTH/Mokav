def func(*args):
	ret_values = []
	
	
	def Lucky(m):
	    s = list(str(m))
	    for i in s:
	        if ((i != '4') and (i != '7')):
	            return False
	    return True
	n = int(args[0])
	if Lucky(n):
	    ret_values.append('YES')
	else:
	    k = int((n / 2))
	    f = 1
	    for i in range(0, (k + 1)):
	        if Lucky(i):
	            if ((n % i) == 0):
	                f = 0
	                ret_values.append('YES')
	                break
	    if (f == 1):
	        ret_values.append('NO')

	return ret_values
