def patched_func(*args):
	global_list = []
	
	a = args[0]
	b = list(a)
	characters = ('H', 'Q', '9')
	j = 0
	while (j < len(b)):
	    if (b[j] in characters):
	        global_list.append('YES')
	        break
	    else:
	        j += 1
	else:
	    global_list.append('NO')
	return global_list