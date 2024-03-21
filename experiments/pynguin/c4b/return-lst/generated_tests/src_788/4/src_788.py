def func(*args):
	ret_values = []
	
	s = args[0]
	length = len(s)
	miss = 0
	for i in range(0, (length // 2)):
	    if (s[i] != s[((length - 1) - i)]):
	        miss += 1
	if ((miss == 1) or ((miss == 0) and ((length % 2) != 0))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
