def func(*args):
	ret_values = []
	
	from math import log
	a = int(args[0])
	b = int(args[1])
	s = False
	n = 0
	for i in range(1, 64):
	    m = (a ** i)
	    if (m == b):
	        s = True
	        n = (i - 1)
	        if (s or (m > b)):
	            break
	if s:
	    ret_values.append('YES\n{}'.format(n))
	else:
	    ret_values.append('NO')

	return ret_values
