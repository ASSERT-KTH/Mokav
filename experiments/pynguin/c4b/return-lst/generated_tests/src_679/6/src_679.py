def func(*args):
	ret_values = []
	
	(x, y, l, r) = map(int, args[0].split())
	s1 = 1
	s2 = 1
	ans = 0
	ll = []
	while (s1 <= r):
	    while (s2 <= r):
	        if (((s1 + s2) <= r) and ((s1 + s2) >= l)):
	            ll.append((s1 + s2))
	            ans += 1
	        s2 *= y
	    s1 *= x
	    s2 = 1
	ll.sort()
	maxi = 0
	for i in range((len(ll) - 1)):
	    if (maxi < ((ll[(i + 1)] - ll[i]) - 1)):
	        maxi = ((ll[(i + 1)] - ll[i]) - 1)
	if (len(ll) == 0):
	    ret_values.append(((r - l) + 1))
	else:
	    if (maxi < (r - ll[(len(ll) - 1)])):
	        maxi = (r - ll[(len(ll) - 1)])
	    if (maxi < (ll[0] - l)):
	        maxi = (ll[0] - l)
	    ret_values.append(maxi)

	return ret_values
