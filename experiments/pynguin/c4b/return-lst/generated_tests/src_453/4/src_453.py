def func(*args):
	ret_values = []
	
	k = int(args[0])
	a = sorted(map(int, args[1].split()), reverse=True)
	if (sum(a) < k):
	    ret_values.append((- 1))
	else:
	    ret_values.append(min((i for i in range(13) if (sum(a[:i]) >= k))))

	return ret_values
