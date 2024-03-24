def func(*args):
	ret_values = []
	
	p = args[0]
	count = 0
	for x in p:
	    if ((x == 'H') or (x == 'Q') or (x == '9')):
	        ret_values.append('YES')
	        break
	    if (count == (len(p) - 1)):
	        ret_values.append('NO')
	    count += 1

	return ret_values
