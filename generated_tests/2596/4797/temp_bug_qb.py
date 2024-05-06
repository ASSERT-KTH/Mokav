def original_func(*args):
	global_list = []
	
	
	def get_len(n):
	    if (n <= 1):
	        return 1
	    return ((get_len((n // 2)) * 2) + 1)
	
	def dvcq(n, ll, rr):
	    if (ll == rr):
	        return 0
	    if (n <= 1):
	        return n
	    mid = get_len((n // 2))
	    if (rr <= mid):
	        return dvcq((n // 2), ll, rr)
	    elif (mid < ll):
	        return dvcq((n // 2), (ll - mid), (rr - mid))
	    else:
	        return (((n & 1) + dvcq((n // 2), ll, mid)) + dvcq((n // 2), 0, (rr - (mid + 1))))
	(N, L, R) = map(int, args[0].split())
	global_list.append(dvcq(N, (L - 1), R))
	return global_list