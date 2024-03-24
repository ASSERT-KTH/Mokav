def func(*args):
	ret_values = []
	
	(n, t) = map(int, args[0].split())
	pp = args[1].strip()
	ll = []
	for j in pp:
	    ll.append(j)
	for i in range(t):
	    k = 0
	    while (k < (n - 1)):
	        if ((ll[k] == 'B') and (ll[(k + 1)] == 'G')):
	            ll[k] = 'G'
	            ll[(k + 1)] = 'B'
	            k += 1
	        k += 1
	ret_values.append(''.join(ll))

	return ret_values
