def func(*args):
	ret_values = []
	
	word = []
	word = list(args[0])
	toggle = False
	if ('Q' in word):
	    toggle = True
	if ('9' in word):
	    toggle = True
	if ('H' in word):
	    toggle = True
	if (toggle == True):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
