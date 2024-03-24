def func(*args):
	ret_values = []
	
	n = int(args[0])
	for i in range((n // 4)):
	    ret_values.append('aabb', end='')
	if ((n % 4) == 1):
	    ret_values.append('a')
	elif ((n % 4) == 2):
	    ret_values.append('aa')
	elif ((n % 4) == 3):
	    ret_values.append('aab')

	return ret_values
