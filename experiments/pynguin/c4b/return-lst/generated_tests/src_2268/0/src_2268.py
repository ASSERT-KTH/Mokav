def func(*args):
	ret_values = []
	
	word = args[0]
	if (('H' in word) or ('Q' in word) or ('9' in word)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
