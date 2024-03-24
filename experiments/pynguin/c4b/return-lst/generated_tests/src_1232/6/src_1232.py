def func(*args):
	ret_values = []
	
	import math
	(n, m) = map(int, args[0].split())
	if ((n == 1) and (m == 1)):
	    ret_values.append('2')
	    exit()
	c = 0
	l = []
	for i in range(45):
	    if (i in l):
	        continue
	    a = ((i ** 2) + i)
	    e = ((m + n) - a)
	    if (e < 0):
	        break
	    d = (1 + (4 * e))
	    v = (((- 1) + math.sqrt(d)) / 2)
	    if ((v - int(v)) == 0):
	        if (((((i ** 2) + v) == m) or (((v ** 2) + i) == m)) and ((((i ** 2) + v) == n) or (((v ** 2) + i) == n))):
	            l.append(v)
	            c += 1
	            continue
	ret_values.append(c)

	return ret_values
