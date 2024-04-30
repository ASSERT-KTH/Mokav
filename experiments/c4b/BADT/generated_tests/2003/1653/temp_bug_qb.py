def original_func(*args):
	global_list = []
	
	x = int(args[0])
	for i in range((x + 1), 9001):
	    a = [str(y) for y in str(i)]
	    if (len(set(a)) == 4):
	        global_list.append(i)
	        break
	    else:
	        continue
	return global_list