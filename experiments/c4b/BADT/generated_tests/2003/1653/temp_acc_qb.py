def patched_func(*args):
	global_list = []
	
	x = (int(args[0]) + 1)
	while True:
	    a = [str(y) for y in str(x)]
	    if (len(set(a)) == len(str(x))):
	        global_list.append(x)
	        break
	    else:
	        x += 1
	        continue
	return global_list