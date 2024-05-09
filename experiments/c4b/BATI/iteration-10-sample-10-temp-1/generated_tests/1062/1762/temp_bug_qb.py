def original_func(*args):
	global_list = []
	
	s = args[0]
	global_list.append('YNEOS'[len((set(str((s.count('4') + s.count('7')))) - set('47')))::2])
	return global_list