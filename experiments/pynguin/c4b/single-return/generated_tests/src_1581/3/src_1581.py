def func(*args):
	
	feeling_number = int(args[0].strip())
	even = 'I hate'
	odd = 'I love'
	final_feeling = ' '
	for i in range(feeling_number):
	    if (i == 0):
	        final_feeling = even
	    elif ((i % 2) != 0):
	        final_feeling = ((final_feeling + ' that ') + odd)
	    elif ((i % 2) == 0):
	        final_feeling = ((final_feeling + ' that ') + even)
	final_feeling = (final_feeling + ' it')
	return(final_feeling)
