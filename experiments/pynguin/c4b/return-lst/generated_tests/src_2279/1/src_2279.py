def func(*args):
	ret_values = []
	
	s = int(args[0])
	x = str(s)
	count = 0
	for k in range(len(x)):
	    if ((x[k] == '4') or (x[k] == '7')):
	        count += 1
	if ((count == 4) or (count == 7)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
