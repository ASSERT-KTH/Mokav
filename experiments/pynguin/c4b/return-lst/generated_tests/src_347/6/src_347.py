def func(*args):
	ret_values = []
	
	K = int(args[0])
	A = list(map(int, args[1].split()))
	A.sort(reverse=True)
	ans = 0
	now = 0
	for a in A:
	    if (now >= K):
	        break
	    now += a
	    ans += 1
	if (now >= K):
	    ret_values.append(ans)
	else:
	    ret_values.append((- 1))

	return ret_values
