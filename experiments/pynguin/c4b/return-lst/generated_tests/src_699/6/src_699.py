def func(*args):
	ret_values = []
	
	n = int(args[0])
	a = 0
	c = 0
	while ((a * 1234567) <= n):
	    b = 0
	    v = (a * 1234567)
	    while (((a * 1234567) + (b * 123456)) <= n):
	        if ((((n - v) - (b * 123456)) % 1234) == 0):
	            ret_values.append('YES')
	            c = 1
	            break
	        b = (b + 1)
	    a = (a + 1)
	    if (c == 1):
	        break
	if (c == 0):
	    ret_values.append('NO')
	l = 0

	return ret_values
