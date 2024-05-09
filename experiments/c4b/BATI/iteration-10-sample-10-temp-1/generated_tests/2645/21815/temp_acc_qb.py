def patched_func(*args):
	global_list = []
	
	numb = [0, 0, 1, 2, 2, 1]
	chart = [1, 0, 5, 2, 3, 4]
	add = int(args[0])
	start = int(args[1])
	start = (2 * start)
	if ((add % 2) == 0):
	    start += 1
	add = ((add + chart[start]) % 6)
	global_list.append(numb[add])
	return global_list