def patched_func(*args):
	global_list = []
	
	lukcyNumbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
	givenNumber = int(args[0])
	for number in lukcyNumbers:
	    if ((givenNumber % number) == 0):
	        global_list.append('YES')
	        exit()
	global_list.append('NO')
	return global_list