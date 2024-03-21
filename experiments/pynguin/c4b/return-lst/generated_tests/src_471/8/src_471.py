def func(*args):
	ret_values = []
	
	s = args[0].strip()
	pi = (72, 81, 57)
	for i in s:
	    if (ord(i) in pi):
	        f = True
	        ret_values.append('YES')
	        quit()
	    else:
	        f = False
	if (f == False):
	    ret_values.append('NO')

	return ret_values
