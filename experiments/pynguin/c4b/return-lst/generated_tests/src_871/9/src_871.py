def func(*args):
	ret_values = []
	
	s = args[0]
	res = 0
	for i in range((len(s) - 1)):
	    if (s[i] == s[(i + 1)]):
	        res += 1
	    else:
	        res = 0
	    if (res >= 6):
	        ret_values.append('YES')
	        break
	else:
	    ret_values.append('NO')

	return ret_values
