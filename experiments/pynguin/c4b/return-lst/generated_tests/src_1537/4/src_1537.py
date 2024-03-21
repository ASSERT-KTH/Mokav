def func(*args):
	ret_values = []
	
	letter = 'aAoOyYeEuUiI'
	string = args[0]
	result = ''
	for i in string:
	    if (not (i in letter)):
	        i = i.lower()
	        result += ('.' + i)
	ret_values.append(result)

	return ret_values
