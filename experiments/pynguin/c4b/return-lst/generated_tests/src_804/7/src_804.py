def func(*args):
	ret_values = []
	
	import re
	s = args[0].strip()
	l = re.split('A|E|I|O|U|Y', s)
	ret_values.append((1 + max([len(i) for i in l])))

	return ret_values
