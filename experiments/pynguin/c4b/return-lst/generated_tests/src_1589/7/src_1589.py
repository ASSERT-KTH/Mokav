def func(*args):
	ret_values = []
	
	(n, k) = args[0].split(' ')
	k = int(k)
	cur = 0
	ans = 0
	great = False
	for c in reversed(n):
	    if (cur >= k):
	        great = True
	        break
	    if (c == '0'):
	        cur += 1
	    else:
	        ans += 1
	if great:
	    ret_values.append(ans)
	else:
	    ret_values.append((len(n) - 1))

	return ret_values
