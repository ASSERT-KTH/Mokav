def func(*args):
	ret_values = []
	
	n = int(args[0])
	res = ''
	for i in range(n):
	    res += ('I love that ' if (i % 2) else 'I hate that ')
	ret_values.append((res[:(- 5)] + 'it'))

	return ret_values
