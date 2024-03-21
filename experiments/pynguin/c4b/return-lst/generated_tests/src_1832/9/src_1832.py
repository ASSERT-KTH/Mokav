def func(*args):
	ret_values = []
	
	num_digits = int(args[0])
	digits = args[1]
	u = set(digits)
	l = len(u)
	half = int((num_digits / 2))
	if ((l == 2) and ('7' in u) and ('4' in u)):
	    if (sum([int(x) for x in digits[0:half]]) == sum([int(x) for x in digits[half:]])):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')
	elif ((l == 1) and ('7' in u)):
	    if (sum([int(x) for x in digits[0:half]]) == sum([int(x) for x in digits[half:]])):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')
	elif ((l == 1) and ('4' in u)):
	    if (sum([int(x) for x in digits[0:half]]) == sum([int(x) for x in digits[half:]])):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')
	else:
	    ret_values.append('NO')

	return ret_values
