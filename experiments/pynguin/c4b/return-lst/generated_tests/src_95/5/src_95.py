def func(*args):
	ret_values = []
	
	n = int(args[0])
	s = args[1]
	k = ((s[:(n // 2)].count('4') * 4) + (s[:(n // 2)].count('7') * 7))
	l = ((s[(n // 2):].count('4') * 4) + (s[(n // 2):].count('7') * 7))
	if (((n % 2) == 0) and ((s.count('4') + s.count('7')) == n) and (k == l)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
