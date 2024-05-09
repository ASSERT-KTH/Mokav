def original_func(*args):
	global_list = []
	
	'\nCreated on Fri Jul 21 11:25:33 2017\n\n@author: forgeguest\n'
	global_list.append(''.join(('.{}'.format(c) for c in [char for char in str(args[0]).lower() if (char not in 'aeiou')])))
	return global_list