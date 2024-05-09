def original_func(*args):
	global_list = []
	
	arr = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	n = int(args[0])
	global_list.append(arr[((n - 1) % 5)])
	return global_list