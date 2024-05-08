def patched_func(*args):
	global_list = []
	
	(l, t) = map(int, args[0].split())
	s = args[1]
	for j in range(t):
	    temp = ''
	    i = 0
	    while (i < (l - 1)):
	        if ((s[i] == 'B') and (s[(i + 1)] == 'G')):
	            temp = (((s[0:i] + s[(i + 1)]) + s[i]) + s[(i + 2):])
	            s = temp
	            i += 1
	        i += 1
	global_list.append(s)
	return global_list