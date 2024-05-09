def patched_func(*args):
	global_list = []
	
	data = args[0].split()
	(Y, K, N) = (int(data[0]), int(data[1]), int(data[2]))
	answer = []
	i = K
	while (i <= N):
	    if (i > Y):
	        answer.append((i - Y))
	    i += K
	if (len(answer) == 0):
	    global_list.append('-1')
	else:
	    global_list.append(' '.join(map(str, answer)))
	return global_list