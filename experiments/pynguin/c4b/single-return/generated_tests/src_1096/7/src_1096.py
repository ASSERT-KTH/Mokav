def func(*args):
	
	import collections
	c = collections.Counter(oct(int(args[0]))[2:])
	return(c['1'])
