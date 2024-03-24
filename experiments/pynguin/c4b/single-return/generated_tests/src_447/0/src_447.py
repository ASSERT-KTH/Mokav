def func(*args):
	
	n = int(args[0])
	res = ''
	for i in range(n):
	    res += ('I love that ' if (i % 2) else 'I hate that ')
	return((res[:(- 5)] + 'it'))
