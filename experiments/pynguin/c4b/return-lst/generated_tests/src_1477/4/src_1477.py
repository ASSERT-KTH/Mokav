def func(*args):
	ret_values = []
	
	s = args[0]
	count = 0
	for i in range(len(s)):
	    if ((s[i] == '4') or (s[i] == '7')):
	        count += 1
	if ((count == 4) or (count == 7)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
