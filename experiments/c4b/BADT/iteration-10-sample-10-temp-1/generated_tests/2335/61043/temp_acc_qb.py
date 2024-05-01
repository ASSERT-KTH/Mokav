def patched_func(*args):
	global_list = []
	
	import re
	global_list.append(('YES' if re.match('.*h.*e.*l.*l.*o.*', str(args[0])) else 'NO'))
	return global_list