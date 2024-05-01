def original_func(*args):
	global_list = []
	
	global_list.append(('Charlar con ella!:!', '¡IGNORALO!!')[(len(set(args[0])) % 2)])
	return global_list