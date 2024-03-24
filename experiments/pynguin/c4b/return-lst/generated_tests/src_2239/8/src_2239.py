def func(*args):
	ret_values = []
	
	s = args[0]
	result = True
	for c in 'hello':
	    ix = s.find(c)
	    if (ix == (- 1)):
	        result = False
	        break
	    s = s[(ix + 1):]
	if result:
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
