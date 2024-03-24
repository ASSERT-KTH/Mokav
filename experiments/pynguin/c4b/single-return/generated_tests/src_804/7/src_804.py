def func(*args):
	
	import re
	s = args[0].strip()
	l = re.split('A|E|I|O|U|Y', s)
	return((1 + max([len(i) for i in l])))
