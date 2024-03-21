def func(*args):
	ret_values = []
	
	girl = list(map(int, args[0].split()))
	boy = list(map(int, args[1].split()))
	
	def compatible(b, g):
	    return ((g - 1) <= b <= ((g + 1) * 2))
	if (compatible(boy[0], girl[1]) or compatible(boy[1], girl[0])):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
