def func(*args):
	ret_values = []
	
	s = str(args[0])
	(chk1, chk2) = ('0000000', '1111111')
	if ((s.find(chk1) >= 0) or (s.find(chk2) >= 0)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
