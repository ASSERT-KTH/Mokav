def func(*args):
	ret_values = []
	
	s = args[0]
	res = 0
	if (len(s) < 2):
	    ret_values.append(0)
	else:
	    for i in range((len(s) - 1)):
	        if ((s[i] == 'V') and (s[(i + 1)] == 'K')):
	            res += 1
	    if (('VVV' in s) or (s[(- 2):] == 'VV')):
	        res += 1
	    elif (('KKK' in s) or (s[:2] == 'KK')):
	        res += 1
	    ret_values.append(res)

	return ret_values
