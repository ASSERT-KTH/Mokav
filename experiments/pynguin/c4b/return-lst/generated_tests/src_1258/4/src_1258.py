def func(*args):
	ret_values = []
	
	n = sum([1 for i in args[0] if (i in ('4', '7'))])
	ret_values.append(('YES' if set(str(n)).issubset(set('47')) else 'NO'))

	return ret_values
