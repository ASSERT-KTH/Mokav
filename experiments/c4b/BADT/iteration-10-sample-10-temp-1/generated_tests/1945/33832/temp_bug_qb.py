def original_func(*args):
	global_list = []
	
	(a, b, n) = map(int, args[0].split())
	for i in range(10):
	    k = int((str(a) + str(i)))
	    if ((k % b) == 0):
	        break
	final_len = (n + len(str(a)))
	remaining = (final_len - len(str(k)))
	global_list.append((k * (10 ** remaining)))
	return global_list