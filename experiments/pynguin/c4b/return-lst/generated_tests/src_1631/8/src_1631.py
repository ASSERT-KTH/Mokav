def func(*args):
	ret_values = []
	
	n = 'aiouey'
	ss = args[0]
	s = ss.lower()
	for c in s:
	    if (not (c in n)):
	        ret_values.append(('.' + c), end='')

	return ret_values
