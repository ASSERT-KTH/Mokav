def func(*args):
	ret_values = []
	
	n = int(args[0])
	hate_str = 'I hate '
	love_str = 'I love '
	feeling = ''
	for i in range(0, n):
	    if (i % 2):
	        feeling += love_str
	    else:
	        feeling += hate_str
	    if (i != (n - 1)):
	        feeling += 'that '
	feeling += 'it'
	ret_values.append(feeling)

	return ret_values
