def patched_func(*args):
	global_list = []
	
	import re
	string = args[0]
	pattern1 = '1?00000000*1?'
	pattern2 = '0?11111111*0?'
	if re.search(pattern1, string):
	    global_list.append('YES')
	elif re.search(pattern2, string):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list