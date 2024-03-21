def func(*args):
	ret_values = []
	
	word = args[0]
	if ('H' in word):
	    ret_values.append('YES')
	elif ('Q' in word):
	    ret_values.append('YES')
	elif ('9' in word):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
