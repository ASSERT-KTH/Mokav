def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].split())
	x = args[1]
	while m:
	    x = x.replace('BG', 'GB')
	    m -= 1
	ret_values.append(x)

	return ret_values
