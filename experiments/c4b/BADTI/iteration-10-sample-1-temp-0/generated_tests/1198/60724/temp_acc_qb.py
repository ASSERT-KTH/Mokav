def patched_func(*args):
	global_list = []
	
	
	def hq9():
	    s = list(args[0].strip())
	    d = {'H': True, 'Q': True, '9': True}
	    for c in s:
	        if (c in d):
	            return 'YES'
	    return 'NO'
	global_list.append(hq9())
	return global_list