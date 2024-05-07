def original_func(*args):
	global_list = []
	
	import re
	global_list.append(('YES' if (re.sub('(l){2,}', 'll', re.sub('(h|e|o)\\1+', '\\1', re.sub('[^h|e|l|o]', '', str(args[0])))) == 'hello') else 'NO'))
	return global_list