def func(*args):
	ret_values = []
	
	data = args[0].split()
	(Y, K, N) = (int(data[0]), int(data[1]), int(data[2]))
	answer = []
	i = K
	while (i <= N):
	    if (i > Y):
	        answer.append((i - Y))
	    i += K
	if (len(answer) == 0):
	    ret_values.append('-1')
	else:
	    ret_values.append(' '.join(map(str, answer)))

	return ret_values
