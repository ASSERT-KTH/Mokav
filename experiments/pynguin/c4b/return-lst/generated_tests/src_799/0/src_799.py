def func(*args):
	ret_values = []
	
	args[0]
	s = args[1]
	for c in s:
	    if ((c != '4') and (c != '7')):
	        ret_values.append('NO')
	        break
	else:
	    if (sum([int(i) for i in s[:(len(s) // 2)]]) == sum([int(i) for i in s[(- 1):((len(s) // 2) - 1):(- 1)]])):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')

	return ret_values
