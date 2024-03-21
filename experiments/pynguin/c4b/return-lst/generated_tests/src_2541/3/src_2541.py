def func(*args):
	ret_values = []
	
	import re
	str = args[0]
	if (len(str) < 7):
	    ret_values.append('NO')
	    exit()
	res0 = re.search('0000000', str)
	res1 = re.search('1111111', str)
	if ((res0 != None) or (res1 != None)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
