def patched_func(*args):
	global_list = []
	
	N = int(args[0])
	S = ''
	for i in range(1, (N + 1)):
	    if (S != ''):
	        S = (S + ' that ')
	    if ((i % 2) == 0):
	        S = (S + 'I love')
	    else:
	        S = (S + 'I hate')
	S = (S + ' it')
	global_list.append(S)
	return global_list