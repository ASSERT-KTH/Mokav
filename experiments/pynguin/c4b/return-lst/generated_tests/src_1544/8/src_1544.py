def func(*args):
	ret_values = []
	
	hello = args[0]
	h = hello.find('h')
	e = hello.find('e', h, len(hello))
	l1 = hello.find('l', e, len(hello))
	l2 = hello.find('l', (l1 + 1), len(hello))
	o = hello.find('o', l2, len(hello))
	if ((h >= 0) and (e > 0) and (l1 > 0) and (l2 > 0) and (o > 0)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
