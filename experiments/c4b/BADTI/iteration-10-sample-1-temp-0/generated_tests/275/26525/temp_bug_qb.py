def original_func(*args):
	global_list = []
	
	n = args[0]
	temp = [0 for i in range(5)]
	temp[0] = n[0]
	temp[1] = n[2]
	temp[2] = n[4]
	temp[3] = n[3]
	temp[4] = n[1]
	n = int(''.join(map(str, temp)))
	global_list.append(((n ** 5) % 100000))
	return global_list