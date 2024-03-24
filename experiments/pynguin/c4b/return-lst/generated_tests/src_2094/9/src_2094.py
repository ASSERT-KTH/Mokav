def func(*args):
	ret_values = []
	
	import re
	new = args[0]
	lower = new.lower()
	wovels = 'aeyiou'
	res = ''
	for char in wovels:
	    lower = re.sub(char, '', lower)
	for char in lower:
	    res += ('.' + char)
	ret_values.append(res)

	return ret_values
