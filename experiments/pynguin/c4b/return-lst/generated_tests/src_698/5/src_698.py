def func(*args):
	ret_values = []
	
	(a, b, c) = map(int, args[0].split())
	p = 0
	for i in range(0, 10001):
	    if (((((c - (a * i)) % b) == 0) and ((c - (a * i)) > 0)) or ((c - (a * i)) == 0)):
	        ret_values.append('Yes')
	        exit()
	ret_values.append('No')

	return ret_values
