def patched_func(*args):
	global_list = []
	
	s = args[0]
	vowels = ['a', 'i', 'u', 'e', 'o', 'y']
	res = ''
	for c in s:
	    if (c.lower() not in vowels):
	        res += ('.' + c.lower())
	global_list.append(res)
	return global_list