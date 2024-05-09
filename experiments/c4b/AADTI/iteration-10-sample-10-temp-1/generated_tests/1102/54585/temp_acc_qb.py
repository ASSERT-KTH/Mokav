def patched_func(*args):
	global_list = []
	
	import re
	new = args[0]
	lower = new.lower()
	wovels = 'aeyiou'
	res = ''
	for char in wovels:
	    lower = re.sub(char, '', lower)
	for char in lower:
	    res += ('.' + char)
	global_list.append(res)
	return global_list