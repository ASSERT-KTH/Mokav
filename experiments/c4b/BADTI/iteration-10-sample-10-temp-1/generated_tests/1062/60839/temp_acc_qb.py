def patched_func(*args):
	global_list = []
	
	num = list(args[0])
	lucky = 0
	for i in range(len(num)):
	    if ((num[i] == '4') or (num[i] == '7')):
	        lucky += 1
	if ((lucky in {4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777}) and (lucky != 0)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list