def func(*args):
	ret_values = []
	
	import re
	string = args[0]
	pattern1 = '1?00000000*1?'
	pattern2 = '0?11111111*0?'
	if re.search(pattern1, string):
	    ret_values.append('YES')
	elif re.search(pattern2, string):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
