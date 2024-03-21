def func(*args):
	ret_values = []
	
	k = int(args[0])
	a = sorted(map(int, args[1].split()))
	a.reverse()
	s = r = 0
	if (k > 0):
	    for i in a:
	        s += i
	        r += 1
	        if (s >= k):
	            ret_values.append(r)
	            break
	    if (s < k):
	        ret_values.append((- 1))
	else:
	    ret_values.append(0)

	return ret_values
