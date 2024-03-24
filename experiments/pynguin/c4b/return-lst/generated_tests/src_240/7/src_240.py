def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n == 1):
	    ret_values.append('I hate it')
	else:
	    s = ''
	    for i in range((n - 1)):
	        if ((i % 2) == 0):
	            s += 'I hate that'
	        else:
	            s += 'I love that'
	        s += ' '
	    if (((n % 2) == 0) and (n != 1)):
	        s += 'I love it'
	    if (((n % 2) == 1) and (n != 1)):
	        s += 'I hate it'
	    ret_values.append(s)

	return ret_values
