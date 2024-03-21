def func(*args):
	ret_values = []
	
	s = args[0]
	a = 0
	for i in range(len(s)):
	    if ((s[i] == '4') or (s[i] == '7')):
	        a += 1
	if ((a == 4) or (a == 7)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
