def func(*args):
	ret_values = []
	
	s = args[0]
	zeros = '0000000'
	ones = '1111111'
	if ((zeros in s) | (ones in s)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
