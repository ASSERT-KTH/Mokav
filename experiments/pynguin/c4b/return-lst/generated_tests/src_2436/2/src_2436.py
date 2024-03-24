def func(*args):
	ret_values = []
	
	x = int(args[0])
	s = ''
	if ((x % 2) == 0):
	    for i in range((x // 2)):
	        s = (s + '1')
	    ret_values.append(s)
	if ((x % 2) == 1):
	    for i in range(((x // 2) - 1)):
	        s = (s + '1')
	    s = ('7' + s)
	    ret_values.append(s)

	return ret_values
