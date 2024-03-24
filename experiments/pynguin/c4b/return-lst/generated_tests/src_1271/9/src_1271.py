def func(*args):
	ret_values = []
	
	k = int(args[0])
	a = args[1].split()
	ans = 0
	for i in range(len(a)):
	    a[i] = int(a[i])
	for i in reversed(sorted(a)):
	    if (k < 1):
	        break
	    k -= i
	    ans += 1
	if (k < 1):
	    ret_values.append(ans)
	else:
	    ret_values.append((- 1))

	return ret_values
