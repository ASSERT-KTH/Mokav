def original_func(*args):
	global_list = []
	
	data = args[0].split()
	(Y, K, N) = (int(data[0]), int(data[1]), int(data[2]))
	answer = []
	counter = ((K - Y) % K)
	if ((counter <= (N - Y)) and (counter > 0)):
	    answer.append(counter)
	    counter += K
	    while (counter <= (N - Y)):
	        answer.append(counter)
	        counter += K
	    global_list.append(' '.join(map(str, answer)))
	else:
	    global_list.append('-1')
	return global_list