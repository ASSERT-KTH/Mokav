def func(*args):
	ret_values = []
	
	a = args[0]
	b = list(a)
	characters = ('H', 'Q', '9')
	j = 0
	while (j < len(b)):
	    if (b[j] in characters):
	        ret_values.append('YES')
	        break
	    else:
	        j += 1
	else:
	    ret_values.append('NO')

	return ret_values
