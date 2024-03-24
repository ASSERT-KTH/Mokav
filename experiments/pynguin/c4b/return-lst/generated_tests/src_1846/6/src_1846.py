def func(*args):
	ret_values = []
	
	a = [int(i) for i in args[0].split()]
	p = int(a[0])
	n = int(a[1])
	if ((p == (n + 1)) or (p == n) or (n == (p + 1))):
	    if ((p == 0) and (n == 0)):
	        ret_values.append('NO')
	    else:
	        ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
