def func(*args):
	ret_values = []
	
	(n, m, k) = map(int, args[0].split())
	ans = 1
	m -= n
	osn = 0
	while (m > 1):
	    if (osn == max((k - 1), (n - k))):
	        break
	    ans += 1
	    m -= 1
	    (osnl, osnr) = (min((k - 1), osn), min((n - k), osn))
	    osn += 1
	    m -= (osnl + osnr)
	ans += (m // n)
	ret_values.append(ans)

	return ret_values
