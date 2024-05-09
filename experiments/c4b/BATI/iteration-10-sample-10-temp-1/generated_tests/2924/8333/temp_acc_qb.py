def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	s = [len(st) for st in args[1].split('0')]
	global_list.append(''.join((str(x) for x in s)))
	return global_list