def original_func(*args):
	global_list = []
	
	k = int(args[0])
	a = list(map(int, args[1].split()))
	sort = sorted(a, key=int, reverse=True)
	result = 0
	count = 0
	for value in sort:
	    if (result >= k):
	        break
	    result += value
	    count += 1
	global_list.append(count)
	return global_list