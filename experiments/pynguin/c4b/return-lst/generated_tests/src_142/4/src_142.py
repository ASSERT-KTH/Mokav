def func(*args):
	ret_values = []
	
	'input\na4\n'
	p = args[0]
	if (p in ['a8', 'h8', 'a1', 'h1']):
	    ret_values.append(3)
	elif any(((x in p) for x in ['a', 'h', '1', '8'])):
	    ret_values.append(5)
	else:
	    ret_values.append(8)

	return ret_values
