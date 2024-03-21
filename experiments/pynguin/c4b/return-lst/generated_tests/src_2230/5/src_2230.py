def func(*args):
	ret_values = []
	
	
	def hq9():
	    s = list(args[0].strip())
	    d = {'H': True, 'Q': True, '9': True}
	    for c in s:
	        if (c in d):
	            return 'YES'
	    return 'NO'
	ret_values.append(hq9())

	return ret_values
