def func(*args):
	ret_values = []
	
	n = int(args[0])
	s = args[1]
	t = 0
	for i in s:
	    if (i == '1'):
	        t += 1
	    else:
	        ret_values.append(t, sep='', end='')
	        t = 0
	ret_values.append(t, sep='', end='')

	return ret_values
