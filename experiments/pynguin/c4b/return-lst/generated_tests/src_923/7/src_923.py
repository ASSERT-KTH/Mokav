def func(*args):
	ret_values = []
	
	
	def is_pri(n):
	    f = 0
	    for i in range(2, (int((n ** 0.5)) + 1)):
	        if ((n % i) == 0):
	            f = 1
	            break
	    return f
	
	def prime(n):
	    pri = []
	    m = 1
	    p = 1
	    while (m <= n):
	        p = (p + 1)
	        if (is_pri(p) == 0):
	            pri.append(p)
	            m = (m + 1)
	    return pri
	(x, y) = args[0].split()
	x = int(x)
	y = int(y)
	a = prime(x)
	c = 0
	for i in range((len(a) - 1)):
	    if ((a[i] + a[(i + 1)]) > x):
	        break
	    if (is_pri(((a[i] + a[(i + 1)]) + 1)) == 0):
	        c += 1
	if (c < y):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
