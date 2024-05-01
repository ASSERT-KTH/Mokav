def patched_func(*args):
	global_list = []
	
	from math import log, ceil
	base = int(args[0])
	power = int(args[1])
	a = round((log(power) / log(base)))
	global_list.append((('YES\n' + str((a - 1))) if ((base ** a) == power) else 'NO'))
	return global_list