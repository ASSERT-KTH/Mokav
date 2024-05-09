def original_func(*args):
	global_list = []
	
	var = list(map(int, args[0].split()))
	i = 0
	while 1:
	    i += 1
	    var[0] *= 3
	    var[1] *= 2
	    if (var[0] >= var[1]):
	        break
	global_list.append(i)
	return global_list