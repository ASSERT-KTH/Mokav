def func(*args):
	
	s = args[0]
	vowels = ['a', 'i', 'u', 'e', 'o', 'y']
	res = ''
	for c in s:
	    if (c.lower() not in vowels):
	        res += ('.' + c.lower())
	return(res)
