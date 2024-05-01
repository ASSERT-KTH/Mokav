def original_func(*args):
	global_list = []
	
	s = args[0]
	r = s
	s = s.replace('6', 'a')
	s = s.replace('4', '6')
	s = s.replace('a', '4')
	s = s.replace('5', 'a')
	s = s.replace('9', '5')
	s = s.replace('a', '9')
	s = s.replace('8', 'a')
	s = s.replace('0', '8')
	s = s.replace('a', '0')
	s = s.replace('1', 'a')
	s = s.replace('2', 'a')
	global_list.append('YNeos'[(r != s)::2])
	return global_list