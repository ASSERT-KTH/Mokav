def func(*args):
	
	p = (int(args[0]) - 1)
	
	def hcf(a, b):
	    if (a is 0):
	        return b
	    else:
	        return hcf((b % a), a)
	cnt = 0
	for i in range(1, (p + 1)):
	    if (hcf(i, p) is 1):
	        cnt += 1
	return(cnt)
