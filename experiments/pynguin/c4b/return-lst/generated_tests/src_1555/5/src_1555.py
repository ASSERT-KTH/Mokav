def func(*args):
	ret_values = []
	
	s = args[0]
	s += '2'
	i = 0
	sum = 1
	while ((i < (len(s) - 1)) and (sum < 7)):
	    if (s[i] == s[(i + 1)]):
	        sum += 1
	    else:
	        sum = 1
	    i += 1
	if (sum >= 7):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
