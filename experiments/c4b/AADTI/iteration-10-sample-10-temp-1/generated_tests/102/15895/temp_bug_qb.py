def original_func(*args):
	global_list = []
	
	'\nCreated on Tue Apr 11 08:09:05 2017\n\n@author: lawrenceylong\n'
	(a, b, c) = map(int, args[0].split())
	global_list.append(min(((a + b) * 2), ((a + b) + c)))
	return global_list