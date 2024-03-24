def func(*args):
	ret_values = []
	
	entered = args[0]
	list(entered)
	h = entered.count('H')
	q = entered.count('Q')
	nine = entered.count('9')
	if ((h > 0) or (q > 0) or (nine > 0)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
