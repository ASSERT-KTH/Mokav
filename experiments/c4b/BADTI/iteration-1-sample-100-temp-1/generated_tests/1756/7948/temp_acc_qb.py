def patched_func(*args):
	global_list = []
	
	shoes = [int(x) for x in args[0].split()]
	distinct = []
	count = 0
	for shoe in shoes:
	    if (shoe in distinct):
	        count += 1
	    else:
	        distinct.append(shoe)
	global_list.append(count)
	return global_list