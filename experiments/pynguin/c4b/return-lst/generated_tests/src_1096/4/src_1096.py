def func(*args):
	ret_values = []
	
	import collections
	c = collections.Counter(oct(int(args[0]))[2:])
	ret_values.append(c['1'])

	return ret_values
