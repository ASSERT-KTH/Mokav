def func(*args):
	ret_values = []
	
	k = set([((i * (i + 1)) // 2) for i in range(1, 45000)])
	n = int(args[0])
	f = set([(n - i) for i in k])
	t = (k & f)
	if t:
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
