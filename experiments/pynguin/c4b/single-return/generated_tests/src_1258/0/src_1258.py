def func(*args):
	
	n = sum([1 for i in args[0] if (i in ('4', '7'))])
	return(('YES' if set(str(n)).issubset(set('47')) else 'NO'))
