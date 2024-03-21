def func(*args):
	ret_values = []
	
	string = args[0]
	rotation = int(args[1])
	start = string[0]
	cstart = start
	end = string[2]
	if ((rotation % 2) == 0):
	    ret_values.append('undefined')
	    quit()
	if (rotation > 4):
	    rotation = (rotation % 4)
	for i in range(rotation):
	    if (start == '>'):
	        start = 'v'
	    elif (start == 'v'):
	        start = '<'
	    elif (start == '<'):
	        start = '^'
	    elif (start == '^'):
	        start = '>'
	if (start == end):
	    ret_values.append('cw')
	    quit()
	start = cstart
	for i in range(rotation):
	    if (start == '>'):
	        start = '^'
	    elif (start == 'v'):
	        start = '>'
	    elif (start == '<'):
	        start = 'v'
	    elif (start == '^'):
	        start = '<'
	if (start == end):
	    ret_values.append('ccw')
	    quit()
	ret_values.append('undefined')

	return ret_values
