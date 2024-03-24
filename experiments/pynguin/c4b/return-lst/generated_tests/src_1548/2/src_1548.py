def func(*args):
	ret_values = []
	
	s = args[0]
	a = []
	for i in range(len(s)):
	    a.append(s[i])
	if (('H' in a) or ('Q' in a) or ('9' in a)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
