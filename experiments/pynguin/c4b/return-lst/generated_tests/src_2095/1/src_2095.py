def func(*args):
	ret_values = []
	
	import re
	char = str(args[0])
	cmd = ['H', 'Q', '9']
	time = 0
	for c in cmd:
	    if (c in char):
	        time += 1
	if (time > 0):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
