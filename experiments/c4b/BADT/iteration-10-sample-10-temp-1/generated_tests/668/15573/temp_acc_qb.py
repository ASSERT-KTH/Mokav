def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	S = ''
	for i in range(1, (n + 1)):
	    if ((i % 2) != 0):
	        S = (S + 'I hate')
	    else:
	        S = (S + 'I love')
	    if (i == n):
	        S = (S + ' it ')
	    else:
	        S = (S + ' that ')
	global_list.append(S)
	return global_list