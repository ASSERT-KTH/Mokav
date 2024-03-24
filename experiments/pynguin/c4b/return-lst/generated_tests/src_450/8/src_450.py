def func(*args):
	ret_values = []
	
	s = args[0]
	ret_values.append('YNEOS'[(len((set(str((s.count('4') + s.count('7')))) - set('47'))) > 0)::2])

	return ret_values
