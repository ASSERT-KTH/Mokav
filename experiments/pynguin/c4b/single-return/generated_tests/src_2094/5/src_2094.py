def func(*args):
	
	import re
	new = args[0]
	lower = new.lower()
	wovels = 'aeyiou'
	res = ''
	for char in wovels:
	    lower = re.sub(char, '', lower)
	for char in lower:
	    res += ('.' + char)
	return(res)
