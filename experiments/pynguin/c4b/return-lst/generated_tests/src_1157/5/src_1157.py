def func(*args):
	ret_values = []
	
	(a, b, m) = map(int, args[0].split())
	if (a < b):
	    (a, b) = (b, a)
	for i in range(((m + a) // a)):
	    if ((((m - (a * i)) % b) == 0) or ((m - (a * i)) == 0)):
	        ret_values.append('Yes')
	        exit(0)
	ret_values.append('No')

	return ret_values
