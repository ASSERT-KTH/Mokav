def func(*args):
	ret_values = []
	
	odd = 'I hate'
	even = 'I love'
	interm = ' that '
	n = int(args[0])
	for i in range(n):
	    i += 1
	    if (i > 1):
	        ret_values.append(interm, end='')
	    if ((i % 2) == 1):
	        ret_values.append(odd, end='')
	    if ((i % 2) == 0):
	        ret_values.append(even, end='')
	    if (i == n):
	        ret_values.append(' it')

	return ret_values
