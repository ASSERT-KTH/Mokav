def func(*args):
	ret_values = []
	
	(n, t, k, d) = (int(x) for x in args[0].split(' '))
	time1 = ((n // k) * t)
	if ((n % k) != 0):
	    time1 = (time1 + t)
	(a, b) = (0, d)
	while (n > 0):
	    if (a < b):
	        a = (a + t)
	    else:
	        b = (b + t)
	    n = (n - k)
	time2 = max(a, b)
	if (time1 > time2):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
