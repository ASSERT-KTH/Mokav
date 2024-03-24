def func(*args):
	
	
	def hq9():
	    s = list(args[0].strip())
	    d = {'H': True, 'Q': True, '9': True}
	    for c in s:
	        if (c in d):
	            return 'YES'
	    return 'NO'
	return(hq9())
