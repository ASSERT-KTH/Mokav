def func(*args):
	ret_values = []
	
	s = args[0]
	ans = False
	for a in s:
	    if ((a == 'H') or (a == 'Q') or (a == '9')):
	        ret_values.append('YES')
	        ans = True
	        break
	if (not ans):
	    ret_values.append('NO')

	return ret_values
