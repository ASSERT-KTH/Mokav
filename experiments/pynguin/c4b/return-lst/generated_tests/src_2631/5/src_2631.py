def func(*args):
	ret_values = []
	
	n = int(args[0])
	res = ''
	while (n >= 2):
	    n -= 2
	    res += '1'
	if (n == 1):
	    res = ('7' + res[:(- 1)])
	ret_values.append(res)

	return ret_values
