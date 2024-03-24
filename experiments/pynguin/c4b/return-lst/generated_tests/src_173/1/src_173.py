def func(*args):
	ret_values = []
	
	(a, b, c) = map(int, args[0].split())
	for i in range(((c // a) + (2 if ((c % a) == 0) else 1))):
	    for j in range((((c - (i * a)) // b) + (2 if (((c - (i * a)) % b) == 0) else 1))):
	        if (((c - (i * a)) - (j * b)) == 0):
	            ret_values.append('Yes')
	            quit()
	ret_values.append('No')

	return ret_values
