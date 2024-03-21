def func(*args):
	ret_values = []
	
	x = args[0]
	s = ''
	s += x[0]
	i = 1
	k = 1
	while (i < (len(x) - 3)):
	    if ((x[i] == 'a') and (x[(i + 1)] == 't') and (k > 0)):
	        s += '@'
	        i += 2
	        k -= 1
	    elif ((x[i] == 'd') and (x[(i + 1)] == 'o') and (x[(i + 2)] == 't')):
	        s += '.'
	        i += 3
	    else:
	        s += x[i]
	        i += 1
	if ((x[i:(len(x) - 1)] == 'at') and (k > 0)):
	    s += '@'
	    i += 2
	s += x[i:len(x)]
	ret_values.append(s)

	return ret_values
