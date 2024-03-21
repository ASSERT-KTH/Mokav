def func(*args):
	ret_values = []
	
	str = args[0]
	zeros = '0000000'
	ones = '1111111'
	if ((zeros in str) or (ones in str)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
