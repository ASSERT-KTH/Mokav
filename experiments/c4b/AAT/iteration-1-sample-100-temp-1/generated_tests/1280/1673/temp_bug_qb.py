def original_func(*args):
	global_list = []
	
	k = int(args[0].strip())
	ll = list(map(int, args[1].split()))
	ll = sorted(ll)
	j = 0
	for i in range((- 1), (- 13), (- 1)):
	    if (k <= 0):
	        break
	    else:
	        k = (k - ll[i])
	        j += 1
	global_list.append(j)
	return global_list