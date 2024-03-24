def func(*args):
	
	letter = 'aAoOyYeEuUiI'
	string = args[0]
	result = ''
	for i in string:
	    if (not (i in letter)):
	        i = i.lower()
	        result += ('.' + i)
	return(result)
