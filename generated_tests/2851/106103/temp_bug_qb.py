def original_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	i = 1
	while True:
	    global_list.append(a, b)
	    a = (a - i)
	    if (a < 0):
	        ans = 'Vladik'
	        break
	    i += 1
	    b = (b - i)
	    if (b < 0):
	        ans = 'Valera'
	        break
	    i += 1
	global_list.append(ans)
	return global_list