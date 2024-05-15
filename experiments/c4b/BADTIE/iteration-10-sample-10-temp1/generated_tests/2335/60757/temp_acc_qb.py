def patched_func(*args):
	global_list = []
	
	s = args[0]
	result = True
	for c in 'hello':
	    ix = s.find(c)
	    if (ix == (- 1)):
	        result = False
	        break
	    s = s[(ix + 1):]
	if result:
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list