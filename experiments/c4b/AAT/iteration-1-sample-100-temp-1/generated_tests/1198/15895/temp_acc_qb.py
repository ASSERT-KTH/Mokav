def patched_func(*args):
	global_list = []
	
	'\nCreated on Wed Mar 22 17:45:02 2017\n\n@author: lawrenceylong\n'
	(a, b, c) = map(list(args[0]).count, ['H', 'Q', '9'])
	(global_list.append('YES') if ((a > 0) or (b > 0) or (c > 0)) else global_list.append('NO'))
	return global_list