def func(*args):
	ret_values = []
	
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
	if (result < k):
	    ret_values.append((- 1))
	else:
	    ret_values.append(count)

	return ret_values
