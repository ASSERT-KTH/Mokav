def func(*args):
	ret_values = []
	
	s = args[0]
	tmp = 0
	for i in range(len(s)):
	    if ((s[i] == '4') or (s[i] == '7')):
	        tmp += 1
	if ((tmp == 4) or (tmp == 7)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
