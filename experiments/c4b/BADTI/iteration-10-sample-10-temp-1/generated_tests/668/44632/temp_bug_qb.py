def original_func(*args):
	global_list = []
	
	N = int(args[0])
	S = ''
	for i in range(N, 0, (- 1)):
	    if (S != ''):
	        S = (S + ' that ')
	    if ((i % 2) == 0):
	        S = (S + 'I love')
	    else:
	        S = (S + 'I hate')
	S = (S + ' it')
	global_list.append(S)
	return global_list